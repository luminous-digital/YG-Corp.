"""Flexible page."""

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks


class AbstractFlexPage(Page):
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("quotation_block", blocks.QuotationBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("video_block", blocks.VideoBlock()),
            ('image_block', blocks.ImageBlock()),
            ('image_person_block', blocks.ImagePersonBlock()),
            ('image_people_block', blocks.ImagePeopleBlock()),
            ('image_content_block', blocks.ImageContentBlock()),
            ('callout_stream_block', blocks.CalloutStreamBlock()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content")
    ]

    class Meta:
        abstract = True


class FlexPage(AbstractFlexPage):
    """Flexible page class"""
    template = "flex/flex_page.html"

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
