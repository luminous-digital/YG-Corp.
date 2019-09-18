from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

from .doc_download_or_open import DocumentDownloadOrOpen
from .link_tab_chooser import LinkTabChooserBlock


class MenuExternalURL(blocks.StructBlock):
    displayed_name = blocks.CharBlock(required=True, max_length=32)
    url = blocks.URLBlock(required=True, help_text="add url")

    class Meta:
        icon = "site"


class MenuLinkChooser(blocks.StreamBlock):
    menu_external_url = MenuExternalURL(required=True, help_text="choose url")
    menu_internal_page = blocks.PageChooserBlock(required=True, help_text="choose page")


class MenuLinkChooserLevelOne(MenuLinkChooser):
    class Meta:
        max_num = 1


class GlobalNavigationBar(blocks.StructBlock):
    global_link = MenuLinkChooserLevelOne()
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        icon = "site"


class MenuLinkWithDocumentChooser(MenuLinkChooser):
    document = DocumentChooserBlock(required=True, help_text="choose doc file")

    class Meta:
        max_num = 1


class MenuLevelTwoImageLink(blocks.StructBlock):
    text = blocks.CharBlock(required=True, max_length=255, help_text="Link or file title")
    image = ImageChooserBlock(required=True)
    link = MenuLinkWithDocumentChooser(required=True)
    if_document_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                             help_text="choose either download or open pdf file")


class MenuLinkChooserLevelTwo(blocks.StructBlock):
    menu_sub_page = MenuLinkChooser(required=False, help_text="add nested pages")


class MenuNavigationLevelOne(blocks.StructBlock):
    menu_navigation_level_1 = MenuLinkChooserLevelOne(required=True, help_text="choose page")
    navigation_html_id = blocks.CharBlock(required=True, max_length=16)
    link = MenuLevelTwoImageLink()
    menu_navigation_level_2 = MenuLinkChooser(required=False, help_text="add nested pages")

    class Meta:
        icon = "site"
