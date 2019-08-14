"""News page."""

from django.db import models
from django.http import JsonResponse
from django.template.loader import render_to_string
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils.timezone import now
from wagtail.search import index


class NewsLandingPage(Page):
    custom_title = models.CharField(max_length=255, blank=False, null=False)

    content_panels = Page.content_panels + [
        FieldPanel('custom_title')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        per_page = 6
        page = self.get_current_page(request)
        news = NewsPage.objects.live().public()
        context['next_url'] = news.count() > page * per_page
        context['news'] = news[((page - 1) * per_page):((page - 1) * per_page) + per_page]
        return context

    def get_template(self, request):
        if request.GET.get('ajax'):
            return "news/news_landing_page_ajax.html"
        return "news/news_landing_page.html"

    @staticmethod
    def get_current_page(request):
        return int(request.GET.get('page')) if request.GET.get('page') else 1

    def serve(self, request, *args, **kwargs):
        if request.GET.get('ajax'):
            current_page = self.get_current_page(request)
            next_page = current_page + 1
            next_url = False
            is_next_url = self.get_context(request, *args, **kwargs)['next_url']
            current_url = request.get_full_path()
            if is_next_url:
                next_url = f'{current_url.split("?")[0]}?ajax=1&page={next_page}'
            return JsonResponse({
                'html': render_to_string(self.get_template(request), self.get_context(request, *args, **kwargs)),
                'next_url': next_url,
            }, safe=False)
        return super().serve(request, *args, **kwargs)

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

    search_fields = Page.search_fields + [
        index.SearchField('article_title'),
        index.FilterField('publication_date'),
        index.SearchField('article_description'),
        index.SearchField('article_link'),
    ]

    template = "news/news_page.html"

    class Meta:
        verbose_name = "News Page"
        verbose_name_plural = "News Page"
