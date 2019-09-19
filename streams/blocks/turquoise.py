from wagtail.core import blocks

from .doc_download_or_open import DocumentDownloadOrOpen
from .link_choosers import LinkAndDocChooserBlock
from .link_tab_chooser import LinkTabChooserBlock


class TurquoiseBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255)
    link_text = blocks.CharBlock(required=False, max_length=255)
    link_or_doc = LinkAndDocChooserBlock(required=False)
    if_document_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                             help_text="choose either download or open pdf file")
    link_tab_chooser = LinkTabChooserBlock(required=False, )


class TurquoiseListBlocks(blocks.StructBlock):
    blocks = blocks.ListBlock(
        TurquoiseBlock()
    )

    class Meta:
        template = "streams/turquoise_block.html"
        icon = "grip"
        label = "Turquoise blocks"
