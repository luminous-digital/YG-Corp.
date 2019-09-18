from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from .link_tab_chooser import LinkTabChooserBlock


class ImageColorTypeChooserBlock(blocks.ChoiceBlock):
    choices = [
        ('#FFFFFF', 'White'),
        ('#000000', 'Black'),
    ]


class ImageBlock(blocks.StructBlock):
    header = blocks.TextBlock(required=True, help_text="add your header")
    header_color = ImageColorTypeChooserBlock(required=True, help_text="choose header color")
    sub_copy = blocks.TextBlock(required=True, help_text="add your sub_copy")
    sub_copy_color = ImageColorTypeChooserBlock(required=True, help_text="choose sub copy color")
    link_text = blocks.CharBlock(required=True, max_length=255)
    link_url = blocks.URLBlock(required=True, help_text="add url")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")
    link_media_content = blocks.TextBlock(help_text="for now idk for what")

    image = ImageChooserBlock(required=True, help_text="choose image")

    class Meta:
        template = "streams/image_block.html"
        icon = "image"
        label = "Image"
