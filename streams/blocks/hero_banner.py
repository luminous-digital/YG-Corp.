from wagtail.core import blocks

from .doc_download_or_open import DocumentDownloadOrOpen
from .link_choosers import LinkAndDocChooserBlock
from .link_tab_chooser import LinkTabChooserBlock
from .title_color_chooser import TitleColorChooserBlock
from .rte import RichTextBlock


class HeroBannerBlock(blocks.StructBlock):
    banner_text = RichTextBlock(required=True, label="Hero banner text")
    banner_color = TitleColorChooserBlock(required=False)
    hyperlink = LinkAndDocChooserBlock(required=False, help_text="add link")
    if_hyperlink_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                              help_text="choose either download or open pdf file")
    link_text = blocks.CharBlock(required=False, max_length=255)
    link_tab_chooser = LinkTabChooserBlock(required=False, help_text="choose either open image on new or current tab")

    class Meta:
        template = "streams/hero_banner_block.html"
        icon = "doc-full"
        label = "Hero banner"
