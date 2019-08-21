from django.db import models

from wagtail.core.models import Orderable, Page
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel


class OfficeComponent(Page):
    @property
    def offices(self):
        return [
            n.office for n in self.related_offices.all()
        ]

    content_panels = Page.content_panels + [
        InlinePanel('related_offices', label="Related Offices")
    ]


class Office(Orderable):
    office_component = ParentalKey(
        'OfficeComponent',
        related_name='related_offices'
    )
    lat = models.FloatField()
    lng = models.FloatField()
    is_headquarter = models.NullBooleanField()
    region = models.CharField(null=True, blank=True, max_length=255)
    country = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    address_line_1 = models.CharField(null=True, blank=True, max_length=255)
    address_line_2 = models.CharField(null=True, blank=True, max_length=255)
    address_line_3 = models.CharField(null=True, blank=True, max_length=255)
    tel = models.CharField(null=True, blank=True, max_length=255)
    mail = models.EmailField(null=True, blank=True)
    web = models.URLField(null=True, blank=True,)
    did_you_know = models.TextField(null=True, blank=True,)

    panels = [
        FieldPanel('lat'),
        FieldPanel('lng'),
        FieldPanel('is_headquarter'),
        FieldPanel('region'),
        FieldPanel('country'),
        FieldPanel('city'),
        FieldPanel('address_line_1'),
        FieldPanel('address_line_2'),
        FieldPanel('address_line_3'),
        FieldPanel('tel'),
        FieldPanel('mail'),
        FieldPanel('web'),
        FieldPanel('did_you_know'),
    ]
