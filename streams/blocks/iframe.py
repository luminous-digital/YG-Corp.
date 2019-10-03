from wagtail.core import blocks


class IframeBlock(blocks.StructBlock):
    hyperlink = blocks.URLBlock(required=True, help_text="add url")
    padding = blocks.BooleanBlock(required=False, label="Add padding")

    class Meta:
        template = "streams/iframe_block.html"
        icon = "link"
        label = "Iframe panel"
