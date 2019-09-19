from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from .callouts import CalloutsModuleBlock
from .doc_download_or_open import DocumentDownloadOrOpen
from .edison_news_feed import NewsFeedWidgetBlock
from .link_choosers import LinkAndDocChooserBlock
from .link_container import LinkContainerBlock
from .link_container_bg_color_chooser import LinkContainerBackgroundColorChooserBlock
from .link_tab_chooser import LinkTabChooserBlock
from .quotation import QuotationBlock
from .rss_news_feed import RssWidgetBlock
from .title_color_chooser import TitleColorChooserBlock
from .twitter_news_feed import TwitterNewsWidgetBlock


class TwoColumnsBlock(blocks.StructBlock):
    left = LinkContainerBlock(required=False)
    right = LinkContainerBlock(required=False)

    class Meta:
        template = "streams/two_columns_base_block.html"
        icon = "doc-full"
        label = "Two columns"


class IframeWidgetBlock(blocks.StructBlock):
    hyperlink = blocks.URLBlock(required=False, help_text="add url")
    padding = blocks.BooleanBlock(required=False, label="Add padding")
    background_colour = LinkContainerBackgroundColorChooserBlock(required=True, help_text="background color")

    class Meta:
        template = "streams/iframe_base_block.html"
        icon = "link"
        label = "Iframe"


class QuickLinksBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255)
    title_color = TitleColorChooserBlock(required=True)
    subtitle = blocks.TextBlock(required=False)
    link_text = blocks.CharBlock(required=False, max_length=255)
    link_or_doc = LinkAndDocChooserBlock(required=False, help_text="choose page or doc")
    if_document_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                             help_text="choose either download or open pdf file")
    link_tab_chooser = LinkTabChooserBlock(required=False, help_text="choose either open page on new or current tab")


class QuickLinksListBlock(blocks.StructBlock):
    headline = blocks.CharBlock(required=False, max_length=255)
    links = blocks.ListBlock(
        QuickLinksBlock()
    )

    class Meta:
        template = "streams/quick_links_block.html"
        icon = "arrow-right"
        label = "Quick Links"


class QuotationWidgetBlock(QuotationBlock):
    class Meta:
        template = "streams/quotation_widget_block.html"


class CalloutsWidgetBlock(CalloutsModuleBlock):
    class Meta:
        template = "streams/callouts_widget_block.html"


class BoardOfDirectors(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255)
    link_text = blocks.CharBlock(required=False, max_length=255)
    link_or_doc = LinkAndDocChooserBlock(required=False)
    if_document_pdf = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                             help_text="choose either download or open pdf file")
    link_tab_chooser = LinkTabChooserBlock(required=False)
    image = ImageChooserBlock(required=True)

    class Meta:
        template = "streams/board_of_directors_block.html"
        icon = "image"
        label = "Board of directors"


class WidgetChooserBlock(blocks.StreamBlock):
    link_container = LinkContainerBlock(required=False)
    two_columns = TwoColumnsBlock(required=False)
    iframe = IframeWidgetBlock(required=False)
    news_feed = NewsFeedWidgetBlock(required=False)
    rss_feed = RssWidgetBlock(required=False)
    twitter_feed = TwitterNewsWidgetBlock(required=False)
    quick_links = QuickLinksListBlock(required=False)
    quote = QuotationWidgetBlock(required=False)
    callouts = CalloutsWidgetBlock(required=False)
    board_of_directors = BoardOfDirectors(required=False)

    class Meta:
        template = "streams/widget_block.html"
        icon = "cog"
        label = "Widget left module"


class RightWidgetChooserBlock(WidgetChooserBlock):
    class Meta:
        template = "streams/widget_block_right_align.html"
        icon = "cog"
        label = "Widget right module"
