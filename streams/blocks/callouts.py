from wagtail.core import blocks


class CalloutsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    callout = blocks.CharBlock(required=True, max_length=255)
    subcopy = blocks.CharBlock(required=False, max_length=255)


class CalloutsModuleBlock(blocks.StructBlock):
    headline = blocks.CharBlock(required=False, max_length=255)
    callouts = blocks.ListBlock(
        CalloutsBlock()
    )

    class Meta:
        template = "streams/callout_module_block.html"
        icon = "spinner"
        label = "Callouts"


class ThreeColumnCalloutsModuleBlock(CalloutsModuleBlock):
    class Meta:
        template = "streams/three_column_callout_module_block.html"
        label = "3 Column Callout"
