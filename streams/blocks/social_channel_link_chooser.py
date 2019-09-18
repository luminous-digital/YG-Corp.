from wagtail.core import blocks


class SocialLinkChooserBlock(blocks.ChoiceBlock):
    choices = [
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('instagram', 'instagram'),
        ('rss', 'rss'),
        ('linkedin', 'linkedin')
    ]


class SocialChannelsLinks(blocks.StructBlock):
    social_channel_logo = SocialLinkChooserBlock(required=True, help_text="choose social channel logo")
    social_channel_url = blocks.URLBlock(required=True, help_text="add url")

    class Meta:
        icon = "link"
