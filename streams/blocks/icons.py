from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from .doc_download_or_open import DocumentDownloadOrOpen
from .link_choosers import LinkAndDocChooserBlock
from .link_tab_chooser import LinkTabChooserBlock
from .numbering import NumberIconBgColourChoooserBlock
from .title_color_chooser import TitleColorChooserBlock


class IconBlock(blocks.StructBlock):
    icon_image = ImageChooserBlock(required=True)
    icon_alt_text = blocks.CharBlock(required=False, max_length=64)
    title = blocks.CharBlock(required=False, max_length=255)
    text = blocks.TextBlock(required=False)
    link_text = blocks.CharBlock(required=False)
    link = LinkAndDocChooserBlock(required=False)
    if_document_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                             help_text="choose either download or open pdf file")
    link_tab_chooser = LinkTabChooserBlock(required=True, default=LinkTabChooserBlock.choices[0])


class IconsListBlock(blocks.StructBlock):
    main_title = blocks.TextBlock(required=False)
    background_colour = NumberIconBgColourChoooserBlock(required=True,
                                                        default=NumberIconBgColourChoooserBlock.choices[0])
    icons_colour = TitleColorChooserBlock(required=True, default=TitleColorChooserBlock.choices[4])
    icons = blocks.ListBlock(
        IconBlock()
    )

    class Meta:
        template = "streams/icon_block.html"
        icon = "list-ul"
        label = "Icon panel"
