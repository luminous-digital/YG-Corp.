from wagtail.core import blocks


class LinkContainerBackgroundColorChooserBlock(blocks.ChoiceBlock):
    choices = [
        ('#00b7b5', 'Cyan'),
        ('#9078d7', 'Violet'),
        ('#605a70', 'Grey'),
        ('#241d36', 'Dark'),
        ('#DC4C81', 'Pink'),
    ]
