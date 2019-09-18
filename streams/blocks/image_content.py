from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageContentBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text="choose image")
    caption = blocks.TextBlock(required=False)

    class Meta:
        template = "streams/image_content_block.html"
        icon = "image"
        label = "Image Content"
