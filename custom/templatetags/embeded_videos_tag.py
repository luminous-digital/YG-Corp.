import re
from django import template
from wagtail.embeds.embeds import get_embed
from wagtail.embeds.exceptions import EmbedException


register = template.Library()


@register.filter
def embeded_videos(video_url):
    try:
        embed = get_embed(video_url)
        embed = embed.html.replace('<iframe', '<iframe class="c-video__player c-video__player--iframe js-viewer js-video-module"')
        embeded_url = re.search("(?P<url>https?://[^\s'\"]+)", embed).group("url")
        delimiter = '?'
        if '?' in embeded_url:
            delimiter = '&'
        embed = embed.replace(embeded_url, "{}{}autoplay=1".format(embeded_url, delimiter))
        embed = embed.replace('allowfullscreen', '')
        embed = embed.replace('fullscreen', '')
        return embed
    except EmbedException:
        # Cannot find embed
        return
