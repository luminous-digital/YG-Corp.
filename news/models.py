"""News page."""

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.timezone import now


class NewsLandingPage(Page):
    custom_title = models.CharField(max_length=255, blank=False, null=False)

    content_panels = Page.content_panels + [
        FieldPanel('custom_title')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        per_page = 6
        page = int(request.GET.get('page')) if request.GET.get('page') else 1
        news = NewsPage.objects.live().public()
        context['load_more'] = news.count() > page * per_page
        context['news'] = news[((page - 1) * per_page):((page - 1) * per_page) + per_page]
        return context

    def get_template(self, request):
        if request.GET.get('ajax'):
            return "news/news_landing_page_ajax.html"
        return "news/news_landing_page.html"

    class Meta:
        verbose_name = "News Landing Page"
        verbose_name_plural = "News Landing Page"


class NewsPage(Page):
    NEW_TAB = "_blank"
    CURRENT_TAB = "_self"
    TAB_CHOOSER = (
        (NEW_TAB, "New tab"),
        (CURRENT_TAB, "Current tab"),
    )

    image = models.ForeignKey("wagtailimages.Image", blank=False, null=True, on_delete=models.SET_NULL)
    article_title = models.CharField(max_length=255, blank=False, null=False)
    publication_date = models.DateField(default=now, blank=False, null=False)
    article_description = models.TextField(max_length=255, blank=False, null=False)
    article_link = models.URLField(max_length=255, blank=False, null=False)
    link_tab_chooser = models.CharField(max_length=6, choices=TAB_CHOOSER, default=CURRENT_TAB)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('article_title'),
        FieldPanel('publication_date'),
        FieldPanel('article_description'),
        FieldPanel('article_link'),
        FieldPanel('link_tab_chooser'),
    ]

    template = "news/news_page.html"

    class Meta:
        verbose_name = "News Page"
        verbose_name_plural = "News Page"
