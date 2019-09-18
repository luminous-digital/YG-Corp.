from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from .link_choosers import LinkChooserBlock
from .link_tab_chooser import LinkTabChooserBlock


class LogoAlignmentBlock(blocks.ChoiceBlock):
    LEFT = 'single'
    CENTERED = 'centered'

    choices = (
        (LEFT, 'Left'),
        (CENTERED, 'Centered')
    )


class LogoStyleBlock(blocks.ChoiceBlock):
    NORMAL = 'Normal'
    RTE = 'RTE'

    choices = (
        (NORMAL, 'Normal'),
        (RTE, 'RTE'),
    )


class LogoBlock(blocks.StructBlock):
    logo_image = ImageChooserBlock(required=True, help_text="Choose only svg files")
    logo_alt_text = blocks.CharBlock(required=False, max_length=255,
                                     help_text="text that will appear if logo won't show")
    logo_link = LinkChooserBlock(required=False)
    link_tab_chooser = LinkTabChooserBlock(required=False)


class LogosListBlock(blocks.StructBlock):
    logos = blocks.ListBlock(
        LogoBlock()
    )
    logo_style = LogoStyleBlock(required=True, default=LogoStyleBlock.choices[0], )
    logo_alignment = LogoAlignmentBlock(required=True, default=LogoAlignmentBlock.choices[1])

    class Meta:
        template = "streams/logo_block.html"
        icon = "wagtail-inverse"
        label = "Logos panel"
