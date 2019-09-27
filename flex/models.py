"""Flexible page."""

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.search import index

from streams import blocks


class AbstractFlexPage(Page):

    # commented image_block because of https://luminousweb.atlassian.net/browse/YOUG-16
    # for now it is not necessary and creates misunderstanding with image_content_block

    # commented accordion_block and person_block because of https://luminousweb.atlassian.net/browse/YOUG-234
    # as a duplicate module to accordion_list_block and not used person_block

    content = StreamField(
        [
            # ('accordion_block', blocks.AccordionBlock()),
            ('accordion_list_block', blocks.AccordionListBlock()),
            ('advisor_analyst_block', blocks.AdvisorsBlock()),
            ('turquoise_block', blocks.TurquoiseListBlocks()),
            ('callout_module_block', blocks.CalloutsModuleBlock()),
            ('three_column_callout_module_block', blocks.ThreeColumnCalloutsModuleBlock()),
            ('contact_block', blocks.ContactInfoBlock()),
            ('download_block', blocks.DownloadBlock()),
            ('icon_block', blocks.IconsListBlock()),
            ('iframe_block', blocks.IframeBlock()),
            ('image_content_block', blocks.ImageContentBlock()),
            ('image_full_bleed_block', blocks.ImageFullBleedBlock()),
            # ('image_person_block', blocks.ImagePersonBlock()),
            ('image_people_block', blocks.ImagePeopleBlock()),
            ('newsfeed_block', blocks.NewsFeedModuleBlock()),
            ('number_block', blocks.NumberingListBlock()),
            ('event_module_block', blocks.EventListBlock()),
            ('form_module_block', blocks.FormModuleBlock()),
            ("full_rte_editor", blocks.RichTextBlockFull()),
            ('hero_banner_block', blocks.HeroBannerBlock()),
            ('padding_block', blocks.PaddingBlock()),
            ("quotation_block", blocks.QuotationBlock()),
            ('table_block', blocks.TableModuleBlock()),
            ('timeline_block', blocks.TimeLineModuleBlock()),
            ("title_and_text", blocks.TitleAndTextBlock()),
            ('two_columns_block', blocks.TwoColumnModuleBlock()),
            ("video_block", blocks.VideoBlock()),
            ('widget_block', blocks.WidgetChooserBlock()),
            ('right_widget_block', blocks.RightWidgetChooserBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("rss_block", blocks.RssBlock()),
            ("rss_news_block", blocks.RssNewsBlock()),
            ("back_page_block", blocks.BackPageLinkBlock()),
            ("Logos_block", blocks.LogosListBlock()),
            # ('image_block', blocks.ImageBlock()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    is_timestamp_displayed = models.BooleanField(default=False, blank=True, null=True,
                                                 verbose_name='Display published date')

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("is_timestamp_displayed"),
        StreamFieldPanel("content")
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content')
    ]

    class Meta:
        abstract = True


class FlexPage(AbstractFlexPage):
    """Flexible page class"""
    template = "flex/flex_page.html"

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"


class ErrorPage(AbstractFlexPage):
    """ Error page class"""
    template = "flex/flex_page.html"

    max_count = 1

    class Meta:
        verbose_name = "404 Error Page"
        verbose_name_plural = "404 Error Pages"
