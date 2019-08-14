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
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("quotation_block", blocks.QuotationBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("video_block", blocks.VideoBlock()),
            # ('image_block', blocks.ImageBlock()),
            ('image_person_block', blocks.ImagePersonBlock()),
            ('image_people_block', blocks.ImagePeopleBlock()),
            ('image_content_block', blocks.ImageContentBlock()),
            ('callout_module_block', blocks.CalloutsModuleBlock()),
            ('download_block', blocks.DownloadBlock()),
            ('contact_block', blocks.ContactInfoBlock()),
            ('advisor_analyst_block', blocks.AdvisorsBlock()),
            ('iframe_block', blocks.IframeBlock()),
            ('hero_banner_block', blocks.HeroBannerBlock()),
            ('accordion_block', blocks.AccordionBlock()),
            ('accordion_list_block', blocks.AccordionListBlock()),
            ('table_block', blocks.TableModuleBlock()),
            ('widget_block', blocks.WidgetChooserBlock()),
            ('two_columns_block', blocks.TwoColumnModuleBlock()),
            ('form_module_block', blocks.FormModuleBlock()),
            ('event_module_block', blocks.EventListBlock()),
            ('newsfeed_block', blocks.NewsFeedModuleBlock()),
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
