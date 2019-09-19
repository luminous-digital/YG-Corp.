from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageFullBleedHeightChoiceBlock(blocks.ChoiceBlock):
    HEIGHT_1 = '800'
    HEIGHT_2 = '600'
    HEIGHT_3 = '366'
    choices = (
        (HEIGHT_1, '800px'),
        (HEIGHT_2, '600px'),
        (HEIGHT_3, '366px'),
    )


class ImageFullBleedBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text="choose image")
    image_height = ImageFullBleedHeightChoiceBlock(required=True)

    class Meta:
        template = 'streams/image_full_bleed_block.html'
        icon = 'image'
        label = 'Full Bleed Image'
