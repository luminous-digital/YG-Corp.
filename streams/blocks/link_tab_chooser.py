from wagtail.core import blocks


class LinkTabChooserBlock(blocks.ChoiceBlock):
    choices = [
        ('_self', 'Current Tab'),
        ('_blank', 'New Tab'),
    ]
