from wagtail.core import blocks

from .link_choosers import LinkChooserBlock
from .link_tab_chooser import LinkTabChooserBlock


class PolicyLinks(blocks.StructBlock):
    link_name = blocks.TextBlock(required=True, help_text="add your link name")
    link_page = blocks.PageChooserBlock(required=True, help_text="choose internal page")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        icon = "link"


class SiteLinks(PolicyLinks):
    link_page = LinkChooserBlock(required=True, help_text="choose one type of url you want to use")


class GlobalSitesLinks(PolicyLinks):
    link_page = blocks.URLBlock(required=True, help_text="add url")
