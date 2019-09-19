from wagtail.core import blocks


class BackPageLinkStyle(blocks.ChoiceBlock):
    NORMAL = 'Normal'
    RTE = 'RTE'
    RTE_FULL = 'RTE_FULL'

    choices = (
        (NORMAL, 'Normal'),
        (RTE, 'RTE'),
        (RTE_FULL, 'RTE FULL'),
    )


class BackPageLinkBlock(blocks.StructBlock):
    link = blocks.PageChooserBlock(required=True, help_text="choose page")
    link_style = BackPageLinkStyle(required=True)

    class Meta:
        template = "streams/back_page_block.html"
        icon = "site"
        label = "Back Page panel"
