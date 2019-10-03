from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks


class TableModuleBlock(blocks.StructBlock):
    table = TableBlock()

    class Meta:
        template = "streams/table_block.html"
        icon = "list-ul"
        label = "Table module"
