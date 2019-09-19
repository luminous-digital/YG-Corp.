from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class ChooserBlock(blocks.StreamBlock):
    class Meta:
        max_num = 1


class LinkChooserBlock(ChooserBlock):
    link_external_url = blocks.URLBlock(required=True, help_text="add url")
    link_internal_page = blocks.PageChooserBlock(required=True, help_text="choose page")


class LinkAndDocChooserBlock(LinkChooserBlock):
    document = DocumentChooserBlock(required=True, help_text="choose file eg. PDF")
