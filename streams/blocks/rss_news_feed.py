import re
from datetime import date

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from html import unescape
from urllib.request import urlopen
from xml.dom import minidom

from .edison_news_feed import NewsFeedModuleBlock
from yougov.settings.base import YOUGOV_NEWS_XML_URL


class RssBlock(NewsFeedModuleBlock):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        key = make_template_fragment_key('rss', [context['self']['number_of_news']])
        rows = cache.get(key)
        if not rows:
            xmldoc = minidom.parse(urlopen(YOUGOV_NEWS_XML_URL))
            entries = xmldoc.getElementsByTagName('entry')
            rows = []
            for entry in entries[:context['self']['number_of_news']]:
                row = {'title': self.get_value_from(entry, 'title'),
                       'summary': unescape(self.get_news_text_from_paragraphs(entry, 'summary')),
                       'id': self.get_value_from(entry, 'id'),
                       'date': self.get_news_date(entry, 'id'),
                       'image': self.get_hero_image(entry, 'link'),
                       }
                rows.append(row)
            cache.set(key, rows)
        context['rows'] = rows
        return context

    def get_news_text_from_paragraphs(self, source, index):
        regex_to_remove = ['<iframe.*?</iframe>', '<script.*?</script>', '<.*?>']
        text = self.get_value_from(source, index)
        for regex in regex_to_remove:
            clean_regex = re.compile(regex)
            text = re.sub(clean_regex, '', text)
        return text

    def get_news_date(self, source, index):
        date_data = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', self.get_value_from(source, index))
        date_object = date(year=int(date_data[0][0]), month=int(date_data[0][1]), day=int(date_data[0][2]))
        return date_object

    @staticmethod
    def get_hero_image(source, index):
        return source.getElementsByTagName(index)[-2]._attrs['href'].nodeValue

    class Meta:
        template = "streams/rss_block.html"
        icon = "doc-full-inverse"
        label = "Rss feed"


class RssNewsBlock(RssBlock):
    class Meta:
        template = "streams/rss_news_block.html"
        icon = "doc-full-inverse"
        label = "Rss news feed"


class RssWidgetBlock(RssBlock):
    class Meta:
        template = "streams/rss_widget_block.html"
        icon = "doc-full-inverse"
        label = "Rss news feed"
