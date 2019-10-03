from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TimeLineBlock(blocks.StructBlock):
    year_field = blocks.CharBlock(required=True, max_length=256)
    text_editor = blocks.RichTextBlock(required=True)
    image = ImageChooserBlock(required=True)
    panel_field = blocks.CharBlock(required=True, max_length=256)
    employees_field = blocks.CharBlock(required=True, max_length=256)
    offices_field = blocks.CharBlock(required=True, max_length=256)


class TimeLineModuleBlock(blocks.StructBlock):
    timeline = blocks.ListBlock(
        TimeLineBlock()
    )

    class Meta:
        template = "streams/timeline_block.html"
        icon = "time"
        label = "Timeline panel"
