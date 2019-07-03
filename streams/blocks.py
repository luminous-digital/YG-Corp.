"""StreamFields"""
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from django.utils.html import format_html
from wagtail.images.blocks import ImageChooserBlock

from wagtailmedia.blocks import AbstractMediaChooserBlock


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


class QuotationBlock(blocks.StructBlock):
    """Quotation block"""
    quotation = blocks.TextBlock(required=True, help_text="Add your quote")
    citation = blocks.TextBlock(required=True, help_text="add citation")
    background = WhiteGreyBackgroundChooserBlock(required=True, help_text="choose color")

    class Meta:
        template = "streams/quotation_block.html"
        icon = "openquote"
        label = "Quotation"


class RichTextBlock(blocks.RichTextBlock):
    """RichText Block"""

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "Full Rich Text"


class ChooserBlock(blocks.StreamBlock):

    class Meta:
        max_num = 1


class VideoMediaChooserBlock(ChooserBlock):
    video_url = EmbedBlock()
    video_file = TestMediaBlock(icon="media")


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


class LinkTabChooserBlock(blocks.ChoiceBlock):

    choices = [
        ('_self', 'Current Tab'),
        ('_blank', 'New Tab'),
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


"""Footer snippet blocks"""


class LinkChooserBlock(ChooserBlock):
    link_external_url = blocks.URLBlock(required=True, help_text="add url")
    link_internal_page = blocks.PageChooserBlock(required=True, help_text="choose page")


class PolicyLinks(blocks.StructBlock):
    link_name = blocks.TextBlock(required=True, help_text="add your callout")
    link_page = blocks.PageChooserBlock(required=True, help_text="choose internal page")
    link_tab_chooser = LinkTabChooserBlock(required=True, help_text="choose either open image on new or current tab")

    class Meta:
        icon = "link"


class SiteLinks(PolicyLinks):
    link_page = LinkChooserBlock(required=True, help_text="choose one type of url you want to use")


class GlobalSitesLinks(PolicyLinks):
    link_page = blocks.URLBlock(required=True, help_text="add url")
