from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from .doc_download_or_open import DocumentDownloadOrOpen
from .link_choosers import LinkAndDocChooserBlock
from .link_container_bg_color_chooser import LinkContainerBackgroundColorChooserBlock
from .link_tab_chooser import LinkTabChooserBlock


class LinkContainerImageSideBlock(blocks.ChoiceBlock):
    LEFT = 'left'
    RIGHT = 'right'
    choices = (
        (LEFT, 'left'),
        (RIGHT, 'right')
    )


class LinkContainerBlock(blocks.StructBlock):
    background_colour = LinkContainerBackgroundColorChooserBlock(required=False, help_text="background color")
    title = blocks.CharBlock(required=False, max_length=255, help_text="add title")
    content = blocks.CharBlock(required=False, max_length=255)
    image = ImageChooserBlock(required=False, help_text="choose image")
    image_position = LinkContainerImageSideBlock(required=False, default=LinkContainerImageSideBlock.choices[1])
    link_text = blocks.CharBlock(required=False, max_length=255)
    link_or_doc = LinkAndDocChooserBlock(required=False, help_text="choose page or doc")
    if_document_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                             help_text="choose either download or open pdf file")
    link_tab_chooser = LinkTabChooserBlock(required=False, help_text="choose either open page on new or current tab")

    class Meta:
        template = "streams/link_container_block.html"
        icon = "doc-empty"
        label = "Link container"
