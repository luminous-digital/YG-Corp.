from django.utils.html import format_html
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmedia.blocks import AbstractMediaChooserBlock

from .link_tab_chooser import LinkTabChooserBlock
from .link_choosers import ChooserBlock, LinkAndDocChooserBlock
from .title_color_chooser import TitleColorChooserBlock


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


class VideoMediaChooserBlock(ChooserBlock):
    video_url = EmbedBlock()
    video_file = AbstractMediaChooserBlock(icon="media")


class VideoBlock(blocks.StructBlock):
    """ Video block"""

    header = blocks.TextBlock(required=False)
    sub_copy = blocks.TextBlock(required=False)
    text_colour = TitleColorChooserBlock(required=True)
    play_text_1 = blocks.CharBlock(required=False, max_length=255, default="Watch the video")
    play_text_2 = blocks.CharBlock(required=False, max_length=255, default="Transparency with data")
    video_thumbnail = ImageChooserBlock(required=False)
    media_chooser = VideoMediaChooserBlock(max_num=1, required=False)
    link = LinkAndDocChooserBlock(required=False)
    link_text = blocks.CharBlock(required=False, max_length=255)
    link_tab_chooser = LinkTabChooserBlock(required=False, help_text="choose either open image on new or current tab")

    class Meta:
        template = "streams/video_block.html"
        icon = "media"
        label = "Video"
