from wagtail.core import blocks

from .link_tab_chooser import LinkTabChooserBlock
from .link_choosers import LinkChooserBlock


class QuotationBlock(blocks.StructBlock):
    """Quotation block"""
    quote_author = blocks.TextBlock(required=False)
    author_title = blocks.TextBlock(required=False)
    quote_text = blocks.TextBlock(required=True)
    link_text = blocks.CharBlock(required=False, max_length=255)
    link_url = LinkChooserBlock(required=False)
    link_tab_chooser = LinkTabChooserBlock(required=False, help_text="choose either open image on new or current tab")
    optional_padding_above = blocks.BooleanBlock(required=False, help_text="add padding above field")

    class Meta:
        template = "streams/quotation_block.html"
        icon = "openquote"
        label = "Quotation"
