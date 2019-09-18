import re

import tweepy
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from streams.blocks import NewsFeedModuleBlock
from yougov.settings.base import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET_KEY, TWITTER_ACCESS_TOKEN_KEY, \
    TWITTER_ACCESS_SECRET_TOKEN_KEY


class TwitterNewsFeedBlock(NewsFeedModuleBlock):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        key = make_template_fragment_key('twitter', [context['self']['number_of_news']])
        tweets = cache.get(key)
        if not tweets:
            tweets = self.get_all_tweets(context['self']['number_of_news'], 'yougov')
            cache.set(key, tweets)
        context['tweets'] = tweets
        return context

    def get_all_tweets(self, number_of_tweets, screen_name=None, ):
        if not screen_name:
            screen_name = 'yougov'
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET_KEY)
        auth.set_access_token(TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_SECRET_TOKEN_KEY)
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name=screen_name, count=number_of_tweets, truncated=False,
                                       tweet_mode='extended')
        tweets = []
        for tweet in new_tweets:
            tweet_text = self.remove_url_from_tweet_text(tweet.full_text)

            tweet = {
                'full_text': tweet_text,
                'user_name': tweet.user.name,
                'created_at': tweet.created_at,
                'tweet_url': tweet.entities['urls'],
            }
            tweets.append(tweet)
        return tweets

    @staticmethod
    def remove_url_from_tweet_text(tweet_text):
        return re.sub(r'http\S+', '', tweet_text)

    class Meta:
        template = "streams/twitter_block.html"
        icon = "doc-full-inverse"
        label = "Twitter feed"


class TwitterNewsWidgetBlock(TwitterNewsFeedBlock):
    class Meta:
        template = "streams/twitter_widget_block.html"
        icon = "doc-full-inverse"
        label = "Twitter news feed"
