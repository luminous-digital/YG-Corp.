from wagtail.core import blocks


class TitleColorChooserBlock(blocks.ChoiceBlock):
    WHITE = '#FFFFFF'
    CYAN = '#00B7B4'
    BLUE = '#00B7B5'
    VIOLET = '#9078D7'
    ORANGE = '#FF6352'
    GREY = '#605A70'
    LIGHT_GREY = '#E6E3EC'
    DARK_BLUE_PURPLE = '#241D36'
    BLACK = '#000000'

    choices = (
        (WHITE, 'White'),
        (CYAN, "Cyan"),
        (BLUE, "Blue"),
        (VIOLET, "Violet"),
        (ORANGE, "Orange"),
        (GREY, "Grey"),
        (LIGHT_GREY, "Light grey"),
        (DARK_BLUE_PURPLE, "Dark blue / Purple"),
        (BLACK, 'Black'),
    )
