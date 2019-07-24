# Generated by Django 2.2.3 on 2019-07-24 09:42

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190723_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add addition text', required=True))])), ('quotation_block', wagtail.core.blocks.StructBlock([('quotation', wagtail.core.blocks.TextBlock(help_text='Add your quote', required=True)), ('citation', wagtail.core.blocks.TextBlock(help_text='add citation', required=True)), ('background', wagtail.core.blocks.ChoiceBlock(choices=[('#F5F6F7', 'Grey'), ('#FFFFFF', 'White')], help_text='choose color'))])), ('full_rich_text', streams.blocks.RichTextBlock()), ('video_block', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.TextBlock(help_text='add your header', required=True)), ('sub_copy', wagtail.core.blocks.TextBlock(help_text='add your sub_copy', required=True)), ('video_thumbnail', wagtail.images.blocks.ImageChooserBlock(help_text='choose video thumbnail image', required=True)), ('media_chooser', wagtail.core.blocks.StreamBlock([('video_url', wagtail.embeds.blocks.EmbedBlock()), ('video_file', streams.blocks.TestMediaBlock(icon='media'))], max_num=1))])), ('image_block', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.TextBlock(help_text='add your header', required=True)), ('header_color', wagtail.core.blocks.ChoiceBlock(choices=[('#FFFFFF', 'White'), ('#000000', 'Black')], help_text='choose header color')), ('sub_copy', wagtail.core.blocks.TextBlock(help_text='add your sub_copy', required=True)), ('sub_copy_color', wagtail.core.blocks.ChoiceBlock(choices=[('#FFFFFF', 'White'), ('#000000', 'Black')], help_text='choose sub copy color')), ('link_text', wagtail.core.blocks.CharBlock(max_length=128, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab')), ('link_media_content', wagtail.core.blocks.TextBlock(help_text='for now idk for what')), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True))])), ('image_person_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('name', wagtail.core.blocks.CharBlock(help_text='add name and surname', max_length=32, required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=32, required=True)), ('biography', wagtail.core.blocks.TextBlock(help_text='biography about', required=True))])), ('image_people_block', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('name', wagtail.core.blocks.CharBlock(help_text='add name and surname', max_length=32, required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=32, required=True)), ('biography', wagtail.core.blocks.TextBlock(help_text='biography about', required=True))])))])), ('image_content_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('caption', wagtail.core.blocks.TextBlock(help_text='add caption', required=True))])), ('callout_stream_block', wagtail.core.blocks.StreamBlock([('content', wagtail.core.blocks.StructBlock([('callout', wagtail.core.blocks.TextBlock(help_text='add your callout', required=True)), ('header', wagtail.core.blocks.TextBlock(help_text='add your header', required=True)), ('sub_copy', wagtail.core.blocks.TextBlock(help_text='add your sub_copy', required=True)), ('background', wagtail.core.blocks.ChoiceBlock(choices=[('#F5F6F7', 'Grey'), ('#FFFFFF', 'White')], help_text='choose color'))], help_text='You can add max 3 callouts', required=True))])), ('download_block', wagtail.core.blocks.StructBlock([('news', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.DateBlock(required=True)), ('file_name', wagtail.core.blocks.CharBlock(help_text='file name', max_length=128, required=True)), ('source_type', wagtail.core.blocks.StreamBlock([('audio_video', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=128, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('audio_video', wagtailmedia.blocks.AbstractMediaChooserBlock(help_text='choose audio or video file', required=True))], required=True)), ('hyperlink', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=128, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('hyper_link_url', wagtail.core.blocks.URLBlock(help_text='choose url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab'))], required=True)), ('document', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=128, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], required=True))], required=False))])))])), ('contact_block', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=64, required=True)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='add sub title', max_length=128, required=True)), ('item', wagtail.core.blocks.StreamBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=64, required=True)), ('email', wagtail.core.blocks.CharBlock(help_text='add email', max_length=32, required=True))], required=True))], required=True)), ('right_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=64, required=True)), ('item', wagtail.core.blocks.StreamBlock([('city', wagtail.core.blocks.CharBlock(help_text='add city', max_length=32, required=True)), ('address_line_1', wagtail.core.blocks.CharBlock(help_text='add address', max_length=32, required=True)), ('address_line_2', wagtail.core.blocks.CharBlock(help_text='add address', max_length=32, required=True)), ('address_line_3', wagtail.core.blocks.CharBlock(help_text='add address', max_length=32, required=True)), ('country', wagtail.core.blocks.CharBlock(help_text='add country', max_length=32, required=True)), ('right_column_text_editor', streams.blocks.RichTextBlock()), ('telephone', wagtail.core.blocks.CharBlock(help_text='add telephone', max_length=32, required=True)), ('email_address', wagtail.core.blocks.CharBlock(help_text='add email', max_length=64, required=True)), ('website', wagtail.core.blocks.URLBlock(help_text='add website address', required=True))], required=False))], required=True)), ('contact_text_editor', streams.blocks.RichTextBlock(required=False))]))], blank=True, null=True),
        ),
    ]
