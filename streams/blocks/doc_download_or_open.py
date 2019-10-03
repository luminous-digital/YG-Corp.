from wagtail.core import blocks


class DocumentDownloadOrOpen(blocks.ChoiceBlock):
    OPEN = 'Open'
    DOWNLOAD = 'Download'

    choices = (
        (DOWNLOAD, 'Download'),
        (OPEN, 'Open')
    )
