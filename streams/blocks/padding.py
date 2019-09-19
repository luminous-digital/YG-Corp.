from wagtail.core import blocks


class PaddingChoiceBlock(blocks.ChoiceBlock):
    LARGE = 'l'
    MEDIUM = 'm'
    SMALL = 's'

    choices = (
        (LARGE, 'Large'),
        (MEDIUM, 'Medium'),
        (SMALL, 'Small'),
    )


class PaddingBlock(blocks.StructBlock):
    padding = PaddingChoiceBlock()

    class Meta:
        template = "streams/padding_block.html"
        icon = "arrows-up-down"
        label = "Padding"
