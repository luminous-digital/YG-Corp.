# Generated by Django 2.2.4 on 2019-08-13 10:03

from django.db import migrations
import streams.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmedia.blocks
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20190809_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add addition text', required=True))])), ('quotation_block', wagtail.core.blocks.StructBlock([('quote_author', wagtail.core.blocks.TextBlock(required=True)), ('author_title', wagtail.core.blocks.TextBlock(required=True)), ('quote_text', wagtail.core.blocks.TextBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab')), ('optional_padding_above', wagtail.core.blocks.BooleanBlock(help_text='add padding above field', required=False))])), ('full_rich_text', streams.blocks.RichTextBlock()), ('video_block', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.TextBlock(help_text='add your header', required=True)), ('sub_copy', wagtail.core.blocks.TextBlock(help_text='add your sub_copy', required=True)), ('video_thumbnail', wagtail.images.blocks.ImageChooserBlock(help_text='choose video thumbnail image', required=True)), ('media_chooser', wagtail.core.blocks.StreamBlock([('video_url', wagtail.embeds.blocks.EmbedBlock()), ('video_file', wagtailmedia.blocks.AbstractMediaChooserBlock(icon='media'))], max_num=1))])), ('image_person_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('name', wagtail.core.blocks.CharBlock(help_text='add name and surname', max_length=255, required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('biography', wagtail.core.blocks.TextBlock(help_text='biography about', required=True))])), ('image_people_block', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('name', wagtail.core.blocks.CharBlock(help_text='add name and surname', max_length=255, required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('biography', wagtail.core.blocks.TextBlock(help_text='biography about', required=True))])))])), ('image_content_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('caption', wagtail.core.blocks.TextBlock(help_text='add caption', required=True))])), ('callout_module_block', wagtail.core.blocks.StructBlock([('callouts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('callout', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('subcopy', wagtail.core.blocks.CharBlock(max_length=255, required=True))])))])), ('download_block', wagtail.core.blocks.StructBlock([('news', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.DateBlock(required=True)), ('file_name', wagtail.core.blocks.CharBlock(help_text='file name', max_length=255, required=True)), ('source_type', wagtail.core.blocks.StreamBlock([('audio_video', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=255, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('audio_video', wagtailmedia.blocks.AbstractMediaChooserBlock(help_text='choose audio or video file', required=True))], required=True)), ('hyperlink', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=255, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('hyper_link_url', wagtail.core.blocks.URLBlock(help_text='choose url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab'))], required=True)), ('document', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=255, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], required=True))], required=False))])))])), ('contact_block', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='add sub title', max_length=255, required=True)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('email', wagtail.core.blocks.CharBlock(help_text='add email', max_length=255, required=True))], required=True)))], required=True)), ('right_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('city', wagtail.core.blocks.CharBlock(help_text='add city', max_length=255, required=True)), ('address_line_1', wagtail.core.blocks.CharBlock(help_text='add address', max_length=255, required=True)), ('address_line_2', wagtail.core.blocks.CharBlock(help_text='add address', max_length=255, required=True)), ('address_line_3', wagtail.core.blocks.CharBlock(help_text='add address', max_length=255, required=True)), ('country', wagtail.core.blocks.CharBlock(help_text='add country', max_length=255, required=True)), ('right_column_text_editor', streams.blocks.RichTextBlock(label='Right column text', required=False)), ('telephone', wagtail.core.blocks.CharBlock(help_text='add telephone', max_length=255, required=False)), ('email_address', wagtail.core.blocks.CharBlock(help_text='add email', max_length=255, required=False)), ('website', wagtail.core.blocks.URLBlock(help_text='add website address', required=False))], required=True)))], required=True)), ('contact_text_editor', streams.blocks.RichTextBlock(label='Contact text editor', required=False))])), ('advisor_analyst_block', wagtail.core.blocks.StructBlock([('advisors', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add job title', max_length=255, required=True)), ('company_name', wagtail.core.blocks.CharBlock(help_text='add company name', max_length=255, required=True)), ('address_field_1', wagtail.core.blocks.CharBlock(help_text='', max_length=255, required=True)), ('address_field_2', wagtail.core.blocks.CharBlock(help_text='', max_length=255, required=True)), ('address_field_3', wagtail.core.blocks.CharBlock(help_text='', max_length=255, required=True)), ('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], required=True)))])), ('iframe_block', wagtail.core.blocks.StructBlock([('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=True))])), ('hero_banner_block', wagtail.core.blocks.StructBlock([('banner_text', streams.blocks.RichTextBlock(label='Hero banner text', required=False)), ('hyperlink', wagtail.core.blocks.StreamBlock([('link_external_page', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('link_document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='add link', required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab'))])), ('accordion_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='add subtitle', max_length=255, required=False)), ('content', streams.blocks.RichTextBlock(label='Content', required=True)), ('expand', wagtail.core.blocks.ChoiceBlock(choices=[('expand', 'Expand'), ('collapse', 'Collapse')], help_text='expand/collapse region'))])), ('accordion_list_block', wagtail.core.blocks.StructBlock([('accordions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='add subtitle', max_length=255, required=False)), ('content', streams.blocks.RichTextBlock(label='Content', required=True)), ('expand', wagtail.core.blocks.ChoiceBlock(choices=[('expand', 'Expand'), ('collapse', 'Collapse')], help_text='expand/collapse region'))])))])), ('table_block', wagtail.core.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock())])), ('widget_block', wagtail.core.blocks.StreamBlock([('link_container', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False)), ('two_columns', wagtail.core.blocks.StructBlock([('left', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False)), ('right', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False))], required=False)), ('iframe', wagtail.core.blocks.StructBlock([('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], required=False))])), ('two_columns_block', wagtail.core.blocks.StructBlock([('social_links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('social_channel_logo', wagtail.core.blocks.ChoiceBlock(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('instagram', 'instagram'), ('rss', 'rss'), ('linkedin', 'linkedin')], help_text='choose social channel logo')), ('social_channel_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))]))), ('left_widget', wagtail.core.blocks.StreamBlock([('link_container', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False)), ('two_columns', wagtail.core.blocks.StructBlock([('left', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False)), ('right', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False))], required=False)), ('iframe', wagtail.core.blocks.StructBlock([('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], required=False))], label='Left widget', required=False)), ('right_widget', wagtail.core.blocks.StreamBlock([('link_container', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False)), ('two_columns', wagtail.core.blocks.StructBlock([('left', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False)), ('right', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark')], help_text='background color')), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('content', wagtail.core.blocks.CharBlock(help_text='add content', max_length=255, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))], required=False))], required=False)), ('iframe', wagtail.core.blocks.StructBlock([('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], required=False))], label='Right widget', required=False))])), ('form_module_block', wagtail.core.blocks.StructBlock([('form', wagtailstreamforms.blocks.FormChooserBlock()), ('form_action', wagtail.core.blocks.CharBlock(help_text='The form post action. "" or "." for the current page or a url', required=False)), ('form_reference', wagtailstreamforms.blocks.InfoBlock(help_text='This form will be given a unique reference once saved', required=False)), ('link_data', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(help_text='add text', max_length=256, required=True)), ('link', wagtail.core.blocks.StreamBlock([('internal_page', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))])), ('doc', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))]))], help_text='choose page or document', required=True)), ('error_message', wagtail.core.blocks.CharBlock(help_text='add message', max_length=256, required=True)), ('success_message', wagtail.core.blocks.CharBlock(help_text='add message', max_length=256, required=True)), ('sub_copy', wagtail.core.blocks.CharBlock(help_text='add sub copy', max_length=256, required=True))], required=True))])), ('event_module_block', wagtail.core.blocks.StructBlock([('events', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='event name', max_length=264, required=True)), ('date', wagtail.core.blocks.DateBlock(required=True)), ('to_be_confirmed', wagtail.core.blocks.ChoiceBlock(choices=[(1, 'Yes'), (0, 'No')]))])))])), ('newsfeed_block', wagtail.core.blocks.StructBlock([('number_of_news', wagtail.core.blocks.IntegerBlock(required=True))]))], blank=True, null=True),
        ),
    ]
