from wagtail.core import blocks

from .social_channel_link_chooser import SocialChannelsLinks
from .widgets import WidgetChooserBlock


class TwoColumnWidgetChooserBlock(WidgetChooserBlock):
    class Meta:
        template = "streams/widget_block_base.html"


class TwoColumnTypeBlock(blocks.ChoiceBlock):
    TOP = 'l-decor-wrapper--top'
    BOTTOM = 'l-decor-wrapper--mobile-bottom'
    choices = (
        (TOP, 'Top'),
        (BOTTOM, 'Bottom')
    )


class TwoColumnWidgetDecor(blocks.ChoiceBlock):
    LEFT = 'l-two-cols__box l-two-cols__box--with-decor-left'
    SIMPLE = 'l-two-cols__box l-two-cols__box--simple-widget'
    BASIC = 'l-two-cols__col'
    CENTER = 'l-two-cols__col l-two-cols__col--center'
    choices = (
        (LEFT, 'With decor left'),
        (SIMPLE, 'Simple widget'),
        (BASIC, 'Basic widget'),
        (CENTER, 'Center widget'),
    )


class TwoColumnBottomWidgets(WidgetChooserBlock):
    class Meta:
        template = "streams/two_cols_widget_block.html"
        icon = "cog"
        label = "Two cols bottom widget"


class TwoColumnModuleBlock(blocks.StructBlock):
    type = TwoColumnTypeBlock(required=False, default=TwoColumnTypeBlock.choices[1])
    social_links = blocks.ListBlock(SocialChannelsLinks(required=False))
    left_widget_decor = TwoColumnWidgetDecor(required=False, default=TwoColumnWidgetDecor.choices[0])
    left_widget = TwoColumnWidgetChooserBlock(required=False, label="Left widget")
    right_widget_decor = TwoColumnWidgetDecor(required=False, default=TwoColumnWidgetDecor.choices[1])
    right_widget = TwoColumnWidgetChooserBlock(required=False, label="Right widget")
    bottom_widgets = TwoColumnBottomWidgets(required=False)

    class Meta:
        template = "streams/two_columns_block.html"
        icon = "cogs"
        label = "Two columns module"
