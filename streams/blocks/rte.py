from wagtail.core import blocks

from .title_color_chooser import TitleColorChooserBlock


class RichTextBlock(blocks.RichTextBlock):
    """RichText Block"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.features = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'bold', 'italic', 'link', 'hr',
                         'document-link', 'image', 'embed', 'left', 'center', 'right']

    class Meta:
        template = "streams/full_rich_text.html"
        icon = "doc-full"
        label = "RTE"


class RichTextBlockFull(blocks.StructBlock):
    rich_text = RichTextBlock(required=True)
    text_colour = TitleColorChooserBlock(required=True)
    full_size = blocks.BooleanBlock(required=False)

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "doc-full-inverse"
        label = "Full RTE"
