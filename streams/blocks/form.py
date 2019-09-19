from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtailstreamforms.blocks import WagtailFormBlock

from .link_tab_chooser import LinkTabChooserBlock


class FormPageBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock(required=True, help_text="choose page")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open page on new or current tab")

    class Meta:
        icon = "site"


class FormDocumentBlock(blocks.StructBlock):
    document = DocumentChooserBlock(required=True, help_text="choose file eg. PDF")

    class Meta:
        icon = "doc-full"


class FormPageDocBlock(blocks.StreamBlock):
    internal_page = FormPageBlock()
    doc = FormDocumentBlock()

    class Meta:
        max_num = 1
        icon = "link"


class FormLink(blocks.StructBlock):
    link_text = blocks.CharBlock(required=True, max_length=256, help_text="add text")
    link = FormPageDocBlock(required=True, help_text="choose page or document")
    error_message = blocks.CharBlock(required=True, max_length=256, help_text="add message")
    success_message = blocks.CharBlock(required=True, max_length=256, help_text="add message")
    sub_copy = blocks.CharBlock(required=True, max_length=256, help_text="add sub copy")


class FormModuleBlock(WagtailFormBlock):
    link_data = FormLink(required=True)
