"""News page."""

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.timezone import now


class NewsLandingPage(Page):
    custom_title = models.CharField(max_length=255, blank=False, null=False)

    content_panels = Page.content_panels + [
        FieldPanel('custom_title')
    ]

    def get_context(self, request, *args, **kwargs):
        context=super().get_context(request, *args, **kwargs)
        context['news'] = NewsPage.objects.live().public()
        return context

    template = "news/news_landing_page.html"

    class Meta:
        verbose_name = "News Landing Page"
        verbose_name_plural = "News Landing Page"


class NewsPage(Page):
    image = models.ForeignKey("wagtailimages.Image", blank=False, null=True, on_delete=models.SET_NULL)
    article_title = models.CharField(max_length=255, blank=False, null=False)
    publication_date = models.DateField(default=now,blank=False, null=False)
    article_description = models.TextField(max_length=255, blank=False, null=False)
    article_link = models.URLField(max_length=255, blank=False, null=False)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('article_title'),
        FieldPanel('publication_date'),
        FieldPanel('article_description'),
        FieldPanel('article_link'),
    ]

    template = "news/news_page.html"

    class Meta:
        verbose_name = "News Page"
        verbose_name_plural = "News Page"
