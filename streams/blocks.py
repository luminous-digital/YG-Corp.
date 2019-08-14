"""StreamFields"""
from xml.dom import minidom

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from django.utils.html import format_html
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

from wagtailmedia.blocks import AbstractMediaChooserBlock
from wagtailstreamforms.blocks import WagtailFormBlock
from urllib.request import urlopen
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from yougov.settings.base import EDISONINVESTMENTSEARCH_XML_URL

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
    link_text = blocks.CharBlock(required=True, max_length=255)
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
    link_text = blocks.CharBlock(required=True, max_length=255)
    link_url = blocks.URLBlock(required=True, help_text="add url")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")
    link_media_content = blocks.TextBlock(help_text="for now idk for what")

    image = ImageChooserBlock(required=True, help_text="choose image")

    class Meta:
        template = "streams/image_block.html"
        icon = "image"
        label = "Image"


class CalloutsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=255)
    callout = blocks.CharBlock(required=True, max_length=255)
    subcopy = blocks.CharBlock(required=True, max_length=255)


class CalloutsModuleBlock(blocks.StructBlock):
    callouts = blocks.ListBlock(
        CalloutsBlock()
    )

    class Meta:
        template = "streams/callout_module_block.html"
        icon = "spinner"
        label = "Callouts"


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
        ('linkedin', 'linkedin')
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
    displayed_name = blocks.CharBlock(required=True, max_length=32)
    url = blocks.URLBlock(required=True, help_text="add url")

    class Meta:
        icon = "site"


class MenuLinkChooser(blocks.StreamBlock):
    menu_external_url = MenuExternalURL(required=True, help_text="choose url")
    menu_internal_page = blocks.PageChooserBlock(required=True, help_text="choose page")


class MenuLinkChooserLevelOne(MenuLinkChooser):
    class Meta:
        max_num = 1


class GlobalNavigationBar(blocks.StructBlock):
    global_link = MenuLinkChooserLevelOne()
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        icon = "site"


class MenuLinkWithDocumentChooser(MenuLinkChooser):
    document = DocumentChooserBlock(required=True, help_text="choose doc file")

    class Meta:
        max_num = 1


class MenuLevelTwoImageLink(blocks.StructBlock):
    text = blocks.CharBlock(required=True, max_length=255, help_text="Link or file title")
    image = ImageChooserBlock(required=True)
    link = MenuLinkWithDocumentChooser(required=True)


class MenuLinkChooserLevelTwo(blocks.StructBlock):
    menu_sub_page = MenuLinkChooser(required=False, help_text="add nested pages")


class MenuNavigationLevelOne(blocks.StructBlock):
    menu_navigation_level_1 = MenuLinkChooserLevelOne(required=True, help_text="choose page")
    navigation_html_id = blocks.CharBlock(required=True, max_length=16)
    link = MenuLevelTwoImageLink()
    menu_navigation_level_2 = MenuLinkChooser(required=False, help_text="add nested pages")

    class Meta:
        icon = "site"


""" Image panel block"""


class ImagePersonBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text="choose image")
    name = blocks.CharBlock(required=True, max_length=255, help_text="add name and surname")
    title = blocks.CharBlock(required=True, max_length=255, help_text="add title")
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
    source_name = blocks.CharBlock(required=True, max_length=255, help_text="choose source name")
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
                ('file_name', blocks.CharBlock(required=True, max_length=255, help_text="file name")),
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
    title = blocks.CharBlock(required=True, max_length=255, help_text="add title")
    email = blocks.CharBlock(required=True, max_length=255, help_text="add email")


class LeftColumnContact(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255, help_text="add title")
    sub_title = blocks.CharBlock(required=True, max_length=255, help_text="add sub title")

    items = blocks.ListBlock(
        LeftColumnItemBlock(required=True)
    )


class RightColumnItemBlock(blocks.StructBlock):
    city = blocks.CharBlock(required=True, max_length=255, help_text="add city")
    address_line_1 = blocks.CharBlock(required=True, max_length=255, help_text="add address")
    address_line_2 = blocks.CharBlock(required=True, max_length=255, help_text="add address")
    address_line_3 = blocks.CharBlock(required=True, max_length=255, help_text="add address")
    country = blocks.CharBlock(required=True, max_length=255, help_text="add country")
    right_column_text_editor = RichTextBlock(required=False, label="Right column text")
    telephone = blocks.CharBlock(required=False, max_length=255, help_text="add telephone")
    email_address = blocks.CharBlock(required=False, max_length=255, help_text="add email")
    website = blocks.URLBlock(required=False, help_text="add website address")


class RightColumnContact(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=255, help_text="add title")
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
    title = blocks.CharBlock(required=True, max_length=255, help_text="add job title")
    company_name = blocks.CharBlock(required=True, max_length=255, help_text="add company name")
    address_field_1 = blocks.CharBlock(required=True, max_length=255, help_text="")
    address_field_2 = blocks.CharBlock(required=True, max_length=255, help_text="")
    address_field_3 = blocks.CharBlock(required=True, max_length=255, help_text="")
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
    link_text = blocks.CharBlock(required=True, max_length=255)
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


"""Table module blocks"""


class TableModuleBlock(blocks.StructBlock):
    table = TableBlock()

    class Meta:
        template = "streams/table_block.html"
        icon = "list-ul"
        label = "Table module"


class LinkContainerBackgroundColorChooserBlock(blocks.ChoiceBlock):
    choices = [
        ('#00b7b5', 'Cyan'),
        ('#9078d7', 'Violet'),
        ('#605a70', 'Grey'),
        ('#241d36', 'Dark'),
    ]


""" News Feed module blocks"""


class NewsFeedModuleBlock(blocks.StructBlock):
    number_of_news = blocks.IntegerBlock(required=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        key = make_template_fragment_key('newsfeed', [context['self']['number_of_news']])
        rows = cache.get(key)
        if not rows:
            xmldoc = minidom.parse(urlopen(EDISONINVESTMENTSEARCH_XML_URL))
            publications = xmldoc.getElementsByTagName('publication')
            rows = []
            for publication in publications[:context['self']['number_of_news']]:
                row = {'headline': self.get_value_from(publication, 'headline'),
                       'description': self.get_value_from(publication, 'description'),
                       'research_link': self.get_value_from(publication, 'research_link')}
                rows.append(row)
            cache.set(key, rows)
        context['rows'] = rows
        return context

    @staticmethod
    def get_value_from(source, index):
        return source.getElementsByTagName(index)[0].firstChild.nodeValue

    class Meta:
        template = "streams/newsfeed_block.html"
        icon = "doc-full-inverse"
        label = "Edison news feed panel"


class NewsFeedWidgetBlock(NewsFeedModuleBlock):
    class Meta:
        template = "streams/newsfeed_widget_block.html"
        icon = "doc-full-inverse"
        label = "Edison news feed"


"""Widget/Two columns module blocks"""


class LinkContainerBlock(blocks.StructBlock):
    background_colour = LinkContainerBackgroundColorChooserBlock(required=True, help_text="background color")
    title = blocks.CharBlock(required=True, max_length=255, help_text="add title")
    content = blocks.CharBlock(required=True, max_length=255, help_text="add content")
    image = ImageChooserBlock(required=False, help_text="choose image")
    link_text = blocks.CharBlock(required=True, max_length=255)
    link_url = blocks.URLBlock(required=True, help_text="add url")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open page on new or current tab")

    class Meta:
        template = "streams/link_container_block.html"
        icon = "doc-empty"
        label = "Link container"


class TwoColumnsBlock(blocks.StructBlock):
    left = LinkContainerBlock(required=False)
    right = LinkContainerBlock(required=False)

    class Meta:
        template = "streams/two_columns_base_block.html"
        icon = "doc-full"
        label = "Two columns"


class IframeWidgetBlock(blocks.StructBlock):
    hyperlink = blocks.URLBlock(required=True, help_text="add url")

    class Meta:
        template = "streams/iframe_base_block.html"
        icon = "link"
        label = "Iframe"


class WidgetChooserBlock(blocks.StreamBlock):
    link_container = LinkContainerBlock(required=False)
    two_columns = TwoColumnsBlock(required=False)
    iframe = IframeWidgetBlock(required=False)
    news_feed = NewsFeedWidgetBlock(required=False)

    class Meta:
        template = "streams/widget_block.html"
        icon = "cog"
        label = "Widget module"


class TwoColumnModuleBlock(blocks.StructBlock):
    social_links = blocks.ListBlock(SocialChannelsLinks())
    left_widget = WidgetChooserBlock(required=False, label="Left widget")
    right_widget = WidgetChooserBlock(required=False, label="Right widget")

    class Meta:
        template = "streams/two_columns_block.html"
        icon = "cogs"
        label = "Two columns module"


""" Form module blocks """


class FormPageBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock(required=True, help_text="choose page")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open page on new or current tab")

    class Meta:
        icon = "site"


class FormDocumentBlock(blocks.StructBlock):
    document = DocumentChooserBlock(required=True, help_text="choose file eg. PDF")

    class Meta:
        icon = "doc-full"


class FormPageDocBlock(blocks.StreamBlock):
    internal_page = FormPageBlock()
    doc = FormDocumentBlock()

    class Meta:
        max_num = 1
        icon = "link"


class FormLink(blocks.StructBlock):
    link_text = blocks.CharBlock(required=True, max_length=256, help_text="add text")
    link = FormPageDocBlock(required=True, help_text="choose page or document")
    error_message = blocks.CharBlock(required=True, max_length=256, help_text="add message")
    success_message = blocks.CharBlock(required=True, max_length=256, help_text="add message")
    sub_copy = blocks.CharBlock(required=True, max_length=256, help_text="add sub copy")


class FormModuleBlock(WagtailFormBlock):
    link_data = FormLink(required=True)


""" Event Calendar blocks"""


class EventConfirmBlock(blocks.ChoiceBlock):
    CONFIRMATION_YES = 1
    CONFIRMATION_NO = 0

    choices = (
        (CONFIRMATION_YES, "Yes"),
        (CONFIRMATION_NO, "No"),
    )


class EventBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True, max_length=264, help_text="event name")
    date = blocks.DateBlock(required=True)
    to_be_confirmed = EventConfirmBlock(required=True)


class EventListBlock(blocks.StructBlock):
    events = blocks.ListBlock(
        EventBlock()
    )

    class Meta:
        template = "streams/event_list_block.html"
        icon = "date"
        label = "Event list panel"


class TimeLineBlock(blocks.StructBlock):
    year_field = blocks.CharBlock(required=True, max_length=256)
    text_editor = blocks.RichTextBlock(required=True)
    image = ImageChooserBlock(required=True)
    panel_field = blocks.CharBlock(required=True, max_length=256)
    employees_field = blocks.CharBlock(required=True, max_length=256)
    offices_field = blocks.CharBlock(required=True, max_length=256)


class TimeLineModuleBlock(blocks.StructBlock):

    timeline = blocks.ListBlock(
        TimeLineBlock()
    )

    class Meta:
        template = "streams/timeline_block.html"
        icon = "time"
        label = "Timeline panel"


""" Office location blocks """


class OfficeLocationDetailBlock(blocks.StructBlock):
    office_name = blocks.CharBlock(required=True, max_length=255)
    address_line_1 = blocks.CharBlock(required=True, max_length=255)
    address_line_2 = blocks.CharBlock(required=True, max_length=255)
    address_line_3 = blocks.CharBlock(required=True, max_length=255)


class CountryDetailsOfficeBlock(blocks.StructBlock):
    country_name = blocks.CharBlock(required=True, max_length=255)
    address = OfficeLocationDetailBlock(required=True)
    telephone = blocks.CharBlock(required=False, max_length=255)
    email = blocks.EmailBlock(required=True)
    website = blocks.URLBlock()
    did_you_know = blocks.TextBlock(required=False)


class OfficeLocationListBlock(blocks.StructBlock):
    hq_office = CountryDetailsOfficeBlock()
    additional_offices = blocks.ListBlock(
        OfficeLocationDetailBlock()
    )


class OfficeLocationBlock(blocks.StructBlock):
    countries = blocks.ListBlock(
        OfficeLocationListBlock()
    )

    class Meta:
        template = "streams/office_location_block.html"
        icon = "home"
        label = "Location office panel"


