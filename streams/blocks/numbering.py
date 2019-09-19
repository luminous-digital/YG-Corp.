from wagtail.core import blocks

from .doc_download_or_open import DocumentDownloadOrOpen
from .link_choosers import LinkAndDocChooserBlock
from .link_tab_chooser import LinkTabChooserBlock
from .title_color_chooser import TitleColorChooserBlock


class NumberIconBgColourChoooserBlock(blocks.ChoiceBlock):
    GREY = '--alt'
    WHITE = ' '

    choices = (
        (GREY, 'Grey'),
        (WHITE, 'White'),
    )


class NumberBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255)
    text = blocks.TextBlock(required=False)
    link_text = blocks.CharBlock(required=False)
    link = LinkAndDocChooserBlock(required=False)
    if_document_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                             help_text="choose either download or open pdf file")
    link_tab_chooser = LinkTabChooserBlock(required=True, default=LinkTabChooserBlock.choices[0])


class NumberingListBlock(blocks.StructBlock):
    main_title = blocks.TextBlock(required=False)
    background_colour = NumberIconBgColourChoooserBlock(required=True,
                                                        default=NumberIconBgColourChoooserBlock.choices[0])
    numbers_colour = TitleColorChooserBlock(required=False)
    numbers = blocks.ListBlock(
        NumberBlock()
    )

    class Meta:
        template = "streams/numbers_block.html"
        icon = "list-ol"
        label = "Numbering panel"
