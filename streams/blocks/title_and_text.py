from wagtail.core import blocks

from .title_color_chooser import TitleColorChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text"""
    title = blocks.CharBlock(required=True, help_text='Add your title')
    title_colour = TitleColorChooserBlock(required=True)
    text = blocks.TextBlock(required=False, help_text='Add addition text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"
