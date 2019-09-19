from wagtail.core import blocks

from .rte import RichTextBlock


class AccordionExpandChooserBlock(blocks.ChoiceBlock):
    choices = [
        ('expand', 'Expand'),
        ('collapse', 'Collapse'),
    ]


class AccordionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255, help_text="add title")
    subtitle = blocks.CharBlock(required=False, max_length=255, help_text="add subtitle")
    content = RichTextBlock(required=True, label="Content")
    expand = AccordionExpandChooserBlock(required=True, help_text="expand/collapse region")

    class Meta:
        template = "streams/accordion_block.html"
        icon = "arrow-down"
        label = "Accordion panel"


class AccordionListBlock(blocks.StructBlock):
    accordions = blocks.ListBlock(
        AccordionBlock()
    )

    class Meta:
        template = "streams/accordion_list_block.html"
        icon = "arrow-down-big"
        label = "Accordion list panel"
