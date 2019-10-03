from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from wagtail.core import blocks

from html import unescape
from urllib.request import urlopen
from xml.dom import minidom

from .link_choosers import LinkChooserBlock
from .link_container_bg_color_chooser import LinkContainerBackgroundColorChooserBlock
from .link_tab_chooser import LinkTabChooserBlock
from yougov.settings.base import EDISONINVESTMENTSEARCH_XML_URL


class NewsFeedModuleBlock(blocks.StructBlock):
    headline = blocks.CharBlock(required=False, default="Company research", max_length=255)
    number_of_news = blocks.IntegerBlock(required=True)
    background_colour = LinkContainerBackgroundColorChooserBlock(required=False, help_text="background color")
    link_text = blocks.CharBlock(required=False, default="Read more", max_length=255)
    link_feed = LinkChooserBlock(required=False)
    link_tab_chooser = LinkTabChooserBlock(required=False, help_text="choose either open image on new or current tab")

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        key = make_template_fragment_key('newsfeed', [context['self']['number_of_news']])
        rows = cache.get(key)
        if not rows:
            xmldoc = minidom.parse(urlopen(EDISONINVESTMENTSEARCH_XML_URL))
            publications = xmldoc.getElementsByTagName('publication')
            rows = []
            for publication in publications[:context['self']['number_of_news']]:
                row = {'headline': self.get_value_from(publication, 'headline'),
                       'description': unescape(self.get_value_from(publication, 'description')),
                       'research_link': self.get_value_from(publication, 'research_link')}
                rows.append(row)
            cache.set(key, rows)
        context['rows'] = rows
        return context

    @staticmethod
    def get_value_from(source, index):
        return source.getElementsByTagName(index)[0].firstChild.nodeValue

    class Meta:
        template = "streams/edison_block.html"
        icon = "doc-full-inverse"
        label = "Edison news feed panel"


class NewsFeedWidgetBlock(NewsFeedModuleBlock):
    class Meta:
        template = "streams/edison_widget_block.html"
        icon = "doc-full-inverse"
        label = "Edison news feed"
