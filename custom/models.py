from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from streams import blocks


@register_snippet
class FooterSnippet(models.Model):

    name = models.CharField(null=False, blank=False, max_length=16, help_text="Name of a footer")

    logo = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL,
                             related_name="+")
    footer_text = RichTextField(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'ul', 'ol', 'hr'], null=True,
                                blank=True)
    copyright_message = models.TextField(null=True, blank=False)

    policy_links = StreamField([
        ('policy_link', blocks.PolicyLinks()),
        ],
        null=True,
        blank=True,
    )
    site_links = StreamField([
        ('site_link', blocks.SiteLinks()),
        ],
        null=True,
        blank=True,
    )
    global_links = StreamField([
        ('global_link', blocks.GlobalSitesLinks()),
        ],
        null=True,
        blank=True,
    )
    social_channel_links = StreamField([
        ('social_channel_links', blocks.SocialChannelsLinks()),
        ],
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo'),
        FieldPanel('footer_text'),
        FieldPanel('copyright_message'),
        StreamFieldPanel('policy_links'),
        StreamFieldPanel('social_channel_links'),
        StreamFieldPanel('site_links'),
        StreamFieldPanel('global_links'),
    ]

    def __str__(self):
        return self.name


@register_snippet
class MenuSnippet(models.Model):

    CURRENT_TAB = "_self"
    NEW_TAB = "_blank"
    MENU_TAB_CHOOSER_CHOICES = [
        (CURRENT_TAB, "Current tab"),
        (NEW_TAB, "New tab")
    ]

    name = models.CharField(null=False, blank=False, max_length=16, help_text="Name of a footer")
    logo = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL,
                             related_name="+")

    menu_tab_chooser = models.CharField(max_length=16, choices=MENU_TAB_CHOOSER_CHOICES, default=CURRENT_TAB)
    menu_links = StreamField([
        ('social_channel_links', blocks.MenuNavigationLevelOne()),
        ],
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo'),
        FieldPanel('menu_tab_chooser'),
        StreamFieldPanel('menu_links'),
    ]

    def __str__(self):
        return self.name
