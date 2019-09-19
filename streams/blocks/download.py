from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock

from .doc_download_or_open import DocumentDownloadOrOpen
from .link_tab_chooser import LinkTabChooserBlock
from .title_color_chooser import TitleColorChooserBlock


class DownloadItemTagBlock(blocks.ChoiceBlock):
    PRESS_RELEASE = "press_release"
    WEBCAST = "webcast"
    PRESENTATION = "presentation"
    REPORT = "report"
    PDF = "pdf"

    choices = (
        (PRESS_RELEASE, "Press release"),
        (WEBCAST, "Webcast"),
        (PRESENTATION, "Presentation"),
        (REPORT, "Report"),
        (PDF, "PDF"),
    )


class DownloadSourceBaseBlock(blocks.StructBlock):
    source_name = blocks.CharBlock(required=True, max_length=255, help_text="choose source name")
    item_relevant_tag = DownloadItemTagBlock(required=True,
                                             help_text="choose relevant tag associated with download item")


class DownloadAudioVideoBlock(DownloadSourceBaseBlock):
    audio_video = AbstractMediaChooserBlock(required=True, help_text="choose audio or video file")
    download_or_open = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                              help_text="choose either download or open pdf file")

    class Meta:
        icon = "media"


class DownloadHyperLinkBlock(DownloadSourceBaseBlock):
    hyper_link_url = blocks.URLBlock(required=True, help_text="choose url")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        icon = "site"


class DownloadPageLinkBlock(DownloadSourceBaseBlock):
    page_link = blocks.PageChooserBlock(required=True, help_text="choose page")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        icon = "redirect"


class DownloadDocumentBlock(DownloadSourceBaseBlock):
    document = DocumentChooserBlock(required=True, help_text="choose file eg. PDF")
    download_or_open = DocumentDownloadOrOpen(required=False, default=DocumentDownloadOrOpen.choices[0],
                                              help_text="choose either download or open pdf file")

    class Meta:
        icon = "doc-full"


class DownloadSourceTypeBlock(blocks.StreamBlock):
    audio_video = DownloadAudioVideoBlock(required=True)
    hyperlink = DownloadHyperLinkBlock(required=True)
    page_link = DownloadPageLinkBlock(required=True)
    document = DownloadDocumentBlock(required=True)


class DownloadBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255)
    headings_text_colour = TitleColorChooserBlock(required=False)
    news = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('date', blocks.DateBlock(required=True)),
                ('file_name', blocks.CharBlock(required=True, max_length=255, help_text="file name")),
                ('source_type', DownloadSourceTypeBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = "streams/download_block.html"
        icon = "download"
        label = "Download panel"
