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

    content = StreamField(
        [
            ('accordion_block', blocks.AccordionBlock()),
            ('accordion_list_block', blocks.AccordionListBlock()),
            ('advisor_analyst_block', blocks.AdvisorsBlock()),
            ('callout_module_block', blocks.CalloutsModuleBlock()),
            ('three_column_callout_module_block', blocks.ThreeColumnCalloutsModuleBlock()),
            ('contact_block', blocks.ContactInfoBlock()),
            ('download_block', blocks.DownloadBlock()),
            ('iframe_block', blocks.IframeBlock()),
            ('image_content_block', blocks.ImageContentBlock()),
            ('image_person_block', blocks.ImagePersonBlock()),
            ('image_people_block', blocks.ImagePeopleBlock()),
            ('newsfeed_block', blocks.NewsFeedModuleBlock()),
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
            # ('image_block', blocks.ImageBlock()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
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
