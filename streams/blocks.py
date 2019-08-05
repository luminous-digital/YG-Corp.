"""StreamFields"""
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from django.utils.html import format_html
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

from wagtailmedia.blocks import AbstractMediaChooserBlock


# wont be used. Everything on video_block template

class TestMediaBlock(AbstractMediaChooserBlock):
    def render_basic(self, value, context=None):
        if not value:
            return ''

        if value.type == 'video':
            player_code = '''
            <div>
                <video width="320" height="240" controls>
                    <source src="{0}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            '''
        else:
            player_code = '''
            <div>
                <audio controls>
                    <source src="{0}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
            '''

        return format_html(player_code, value.file.url)


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text"""
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add addition text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class WhiteGreyBackgroundChooserBlock(blocks.ChoiceBlock):

    choices = [
        ('#F5F6F7', 'Grey'),
        ('#FFFFFF', 'White'),
    ]


class LinkTabChooserBlock(blocks.ChoiceBlock):

    choices = [
        ('_self', 'Current Tab'),
        ('_blank', 'New Tab'),
    ]


class QuotationBlock(blocks.StructBlock):
    """Quotation block"""
    quote_author = blocks.TextBlock(required=True)
    author_title = blocks.TextBlock(required=True)
    quote_text = blocks.TextBlock(required=True)
    link_text = blocks.CharBlock(required=True, max_length=128)
    link_url = blocks.URLBlock(required=True)
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")
    optional_padding_above = blocks.BooleanBlock(required=False, help_text="add padding above field")

    class Meta:
        template = "streams/quotation_block.html"
        icon = "openquote"
        label = "Quotation"


class RichTextBlock(blocks.RichTextBlock):
    """RichText Block"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.features = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'bold', 'italic', 'link', 'hr',
                         'document-link', 'image', 'embed']

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "Full Rich Text"


class ChooserBlock(blocks.StreamBlock):

    class Meta:
        max_num = 1


class VideoMediaChooserBlock(ChooserBlock):
    video_url = EmbedBlock()
    video_file = AbstractMediaChooserBlock(icon="media")


class VideoBlock(blocks.StructBlock):
    """ Video block"""

    header = blocks.TextBlock(required=True, help_text="add your header")
    sub_copy = blocks.TextBlock(required=True, help_text="add your sub_copy")
    video_thumbnail = ImageChooserBlock(required=True, help_text="choose video thumbnail image")
    media_chooser = VideoMediaChooserBlock(max_num=1)

    class Meta:
        template = "streams/video_block.html"
        icon = "media"
        label = "Video"


class ImageColorTypeChooserBlock(blocks.ChoiceBlock):

    choices = [
        ('#FFFFFF', 'White'),
        ('#000000', 'Black'),
    ]


class ImageBlock(blocks.StructBlock):
    header = blocks.TextBlock(required=True, help_text="add your header")
    header_color = ImageColorTypeChooserBlock(required=True, help_text="choose header color")
    sub_copy = blocks.TextBlock(required=True, help_text="add your sub_copy")
    sub_copy_color = ImageColorTypeChooserBlock(required=True, help_text="choose sub copy color")
    link_text = blocks.CharBlock(required=True, max_length=128)
    link_url = blocks.URLBlock(required=True, help_text="add url")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")
    link_media_content = blocks.TextBlock(help_text="for now idk for what")

    image = ImageChooserBlock(required=True, help_text="choose image")

    class Meta:
        template = "streams/image_block.html"
        icon = "image"
        label = "Image"


class CalloutContentBlock(blocks.StructBlock):
    callout = blocks.TextBlock(required=True, help_text="add your callout")
    header = blocks.TextBlock(required=True, help_text="add your header")
    sub_copy = blocks.TextBlock(required=True, help_text="add your sub_copy")
    background = WhiteGreyBackgroundChooserBlock(required=True, help_text="choose color")

    class Meta:
        icon = "spinner"
        label = "Callout Content"


class CalloutStreamBlock(blocks.StreamBlock):
    content = CalloutContentBlock(required=True, help_text="You can add max 3 callouts")

    class Meta:
        template = "streams/callout_block.html"
        icon = "spinner"
        label = "Callout Stream"
        max_num = 3


class ImageContentBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text="choose image")
    caption = blocks.TextBlock(required=True, help_text="add caption")

    class Meta:
        template = "streams/image_content_block.html"
        icon = "image"
        label = "Image Content"


"""Footer snippet blocks"""


class SocialLinkChooserBlock(blocks.ChoiceBlock):

    choices = [
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('instagram', 'instagram'),
        ('rss', 'rss'),
    ]


class LinkChooserBlock(ChooserBlock):
    link_external_url = blocks.URLBlock(required=True, help_text="add url")
    link_internal_page = blocks.PageChooserBlock(required=True, help_text="choose page")


class PolicyLinks(blocks.StructBlock):
    link_name = blocks.TextBlock(required=True, help_text="add your link name")
    link_page = blocks.PageChooserBlock(required=True, help_text="choose internal page")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        icon = "link"


class SiteLinks(PolicyLinks):
    link_page = LinkChooserBlock(required=True, help_text="choose one type of url you want to use")


class GlobalSitesLinks(PolicyLinks):
    link_page = blocks.URLBlock(required=True, help_text="add url")


class SocialChannelsLinks(blocks.StructBlock):
    social_channel_logo = SocialLinkChooserBlock(required=True, help_text="choose social channel logo")
    social_channel_url = blocks.URLBlock(required=True, help_text="add url")

    class Meta:
        icon = "link"


"""Website menu snippets blocks"""


class MenuExternalURL(blocks.StructBlock):
    displayed_name = blocks.CharBlock(required=True, max_length=16)
    url = blocks.URLBlock(required=True, help_text="add url")

    class Meta:
        icon = "site"


class MenuLinkChooser(blocks.StreamBlock):
    menu_external_url = MenuExternalURL(required=True, help_text="choose url")
    menu_internal_page = blocks.PageChooserBlock(required=True, help_text="choose page")


class MenuLinkChooserLevelOne(MenuLinkChooser):

    class Meta:
        max_num = 1


class MenuNavigationLevelOne(blocks.StructBlock):
    menu_navigation_level_1 = MenuLinkChooserLevelOne(required=True, help_text="choose page")
    navigation_html_id = blocks.CharBlock(required=True, max_length=16)
    menu_navigation_level_2 = MenuLinkChooser(required=False, help_text="add nested pages")

    class Meta:
        icon = "site"


""" Image panel block"""


class ImagePersonBlock(blocks.StructBlock):

    image = ImageChooserBlock(required=True, help_text="choose image")
    name = blocks.CharBlock(required=True, max_length=32, help_text="add name and surname")
    title = blocks.CharBlock(required=True, max_length=32, help_text="add title")
    biography = blocks.TextBlock(required=True, help_text="biography about")

    class Meta:
        template = "streams/image_person_block.html"
        icon = "user"
        label = "Person panel"


class ImagePeopleBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        ImagePersonBlock()
    )

    class Meta:
        template = "streams/image_people_block.html"
        icon = "group"
        label = "People panel"


"""Download Blocks"""


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

    source_name = blocks.CharBlock(required=True, max_length=128, help_text="choose source name")
    item_relevant_tag = DownloadItemTagBlock(required=True,
                                             help_text="choose relevant tag associated with download item")


class DownloadAudioVideoBlock(DownloadSourceBaseBlock):
    audio_video = AbstractMediaChooserBlock(required=True, help_text="choose audio or video file")

    class Meta:
        icon = "media"


class DownloadHyperLinkBlock(DownloadSourceBaseBlock):
    hyper_link_url = blocks.URLBlock(required=True, help_text="choose url")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        icon = "site"


class DownloadDocumentBlock(DownloadSourceBaseBlock):
    document = DocumentChooserBlock(required=True, help_text="choose file eg. PDF")

    class Meta:
        icon = "doc-full"


class DownloadSourceTypeBlock(blocks.StreamBlock):

    audio_video = DownloadAudioVideoBlock(required=True)
    hyperlink = DownloadHyperLinkBlock(required=True)
    document = DownloadDocumentBlock(required=True)


class DownloadBlock(blocks.StructBlock):

    news = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('date', blocks.DateBlock(required=True)),
                ('file_name', blocks.CharBlock(required=True, max_length=128, help_text="file name")),
                ('source_type', DownloadSourceTypeBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = "streams/download_block.html"
        icon = "download"
        label = "Download panel"


""" Contact Blocks """


class LeftColumnItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=64, help_text="add title")
    email = blocks.CharBlock(required=True, max_length=32, help_text="add email")


class LeftColumnContact(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=64, help_text="add title")
    sub_title = blocks.CharBlock(required=True, max_length=128, help_text="add sub title")

    items = blocks.ListBlock(
        LeftColumnItemBlock(required=True)
    )


class RightColumnItemBlock(blocks.StructBlock):
    city = blocks.CharBlock(required=True, max_length=32, help_text="add city")
    address_line_1 = blocks.CharBlock(required=True, max_length=32, help_text="add address")
    address_line_2 = blocks.CharBlock(required=True, max_length=32, help_text="add address")
    address_line_3 = blocks.CharBlock(required=True, max_length=32, help_text="add address")
    country = blocks.CharBlock(required=True, max_length=32, help_text="add country")
    right_column_text_editor = RichTextBlock(required=False, label="Right column text")
    telephone = blocks.CharBlock(required=False, max_length=32, help_text="add telephone")
    email_address = blocks.CharBlock(required=False, max_length=64, help_text="add email")
    website = blocks.URLBlock(required=False, help_text="add website address")


class RightColumnContact(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=64, help_text="add title")
    items = blocks.ListBlock(
        RightColumnItemBlock(required=True)
    )


class ContactInfoBlock(blocks.StructBlock):

    left_column = LeftColumnContact(required=True)
    right_column = RightColumnContact(required=True)
    contact_text_editor = RichTextBlock(required=False, label="Contact text editor")

    class Meta:
        template = "streams/contact_block.html"
        icon = "mail"
        label = "Contact panel"


""" Advisor/Analyst blocks """


class AdvisorListContentBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, max_length=64, help_text="add job title")
    company_name = blocks.CharBlock(required=True, max_length=64, help_text="add company name")
    address_field_1 = blocks.CharBlock(required=True, max_length=64, help_text="")
    address_field_2 = blocks.CharBlock(required=True, max_length=64, help_text="")
    address_field_3 = blocks.CharBlock(required=True, max_length=64, help_text="")
    hyperlink = blocks.URLBlock(required=True, help_text="add url")


class AdvisorsBlock(blocks.StructBlock):

    advisors = blocks.ListBlock(
        AdvisorListContentBlock(required=True)
    )

    class Meta:
        template = "streams/advisor_block.html"
        icon = "form"
        label = "Advisor panel"


""" Iframe block """


class IframeBlock(blocks.StructBlock):
    hyperlink = blocks.URLBlock(required=True, help_text="add url")

    class Meta:
        template = "streams/iframe_block.html"
        icon = "link"
        label = "Iframe panel"


""" Hero banner blocks"""


class HeroBannerLinkBlock(blocks.StreamBlock):
    link_external_page = blocks.URLBlock(required=True, help_text="add url")
    link_internal_page = blocks.PageChooserBlock(required=True, help_text="choose page")
    link_document = DocumentChooserBlock(required=True, help_text="choose file eg. PDF")

    class Meta:
        max_num = 1


class HeroBannerBlock(blocks.StructBlock):
    banner_text = RichTextBlock(required=False, label="Hero banner text")
    hyperlink = HeroBannerLinkBlock(required=True, help_text="add link")
    link_text = blocks.CharBlock(required=True, max_length=128)
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        template = "streams/hero_banner_block.html"
        icon = "doc-full"
        label = "Hero banner"


class AccordionExpandChooserBlock(blocks.ChoiceBlock):

    choices = [
        ('expand', 'Expand'),
        ('collapse', 'Collapse'),
    ]


""" Accordion module blocks"""


class AccordionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=32, help_text="add title")
    subtitle = blocks.CharBlock(required=False, max_length=32, help_text="add subtitle")
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
