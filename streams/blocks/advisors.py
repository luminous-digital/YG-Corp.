from wagtail.core import blocks

from .doc_download_or_open import DocumentDownloadOrOpen
from .link_choosers import LinkAndDocChooserBlock
from .link_tab_chooser import LinkTabChooserBlock


class AdvisorListContentBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255, help_text="add job title")
    company_name = blocks.CharBlock(required=True, max_length=255, help_text="add company name")
    address_field_1 = blocks.CharBlock(required=True, max_length=255, help_text="")
    address_field_2 = blocks.CharBlock(required=True, max_length=255, help_text="")
    address_field_3 = blocks.CharBlock(required=True, max_length=255, help_text="")
    link_text = blocks.CharBlock(required=False, max_length=255, default="Find out more")
    link = LinkAndDocChooserBlock(required=False, )
    if_document_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                             help_text="choose either download or open pdf file")
    link_tab_chooser = LinkTabChooserBlock(required=False, help_text="choose either open link on new or current tab")


class AdvisorsBlock(blocks.StructBlock):
    advisors = blocks.ListBlock(
        AdvisorListContentBlock(required=True)
    )

    class Meta:
        template = "streams/advisor_block.html"
        icon = "form"
        label = "Advisor panel"
