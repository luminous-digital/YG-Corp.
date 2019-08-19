# Generated by Django 2.2.4 on 2019-08-19 14:03

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
        ('home', '0023_auto_20190816_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('accordion_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='add subtitle', max_length=255, required=False)), ('content', streams.blocks.RichTextBlock(label='Content', required=True)), ('expand', wagtail.core.blocks.ChoiceBlock(choices=[('expand', 'Expand'), ('collapse', 'Collapse')], help_text='expand/collapse region'))])), ('accordion_list_block', wagtail.core.blocks.StructBlock([('accordions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('subtitle', wagtail.core.blocks.CharBlock(help_text='add subtitle', max_length=255, required=False)), ('content', streams.blocks.RichTextBlock(label='Content', required=True)), ('expand', wagtail.core.blocks.ChoiceBlock(choices=[('expand', 'Expand'), ('collapse', 'Collapse')], help_text='expand/collapse region'))])))])), ('advisor_analyst_block', wagtail.core.blocks.StructBlock([('advisors', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add job title', max_length=255, required=True)), ('company_name', wagtail.core.blocks.CharBlock(help_text='add company name', max_length=255, required=True)), ('address_field_1', wagtail.core.blocks.CharBlock(help_text='', max_length=255, required=True)), ('address_field_2', wagtail.core.blocks.CharBlock(help_text='', max_length=255, required=True)), ('address_field_3', wagtail.core.blocks.CharBlock(help_text='', max_length=255, required=True)), ('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], required=True)))])), ('callout_module_block', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('callouts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('callout', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('subcopy', wagtail.core.blocks.CharBlock(max_length=255, required=True))])))])), ('contact_block', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('sub_title', wagtail.core.blocks.CharBlock(help_text='add sub title', max_length=255, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('email', wagtail.core.blocks.CharBlock(help_text='add email', max_length=255, required=False))], required=False)))], required=False)), ('right_column', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('city', wagtail.core.blocks.CharBlock(help_text='add city', max_length=255, required=False)), ('address_line_1', wagtail.core.blocks.CharBlock(help_text='add address', max_length=255, required=False)), ('address_line_2', wagtail.core.blocks.CharBlock(help_text='add address', max_length=255, required=False)), ('address_line_3', wagtail.core.blocks.CharBlock(help_text='add address', max_length=255, required=False)), ('country', wagtail.core.blocks.CharBlock(help_text='add country', max_length=255, required=False)), ('right_column_text_editor', streams.blocks.RichTextBlock(label='Right column text', required=False)), ('telephone', wagtail.core.blocks.CharBlock(help_text='add telephone', max_length=255, required=False)), ('email_address', wagtail.core.blocks.CharBlock(help_text='add email', max_length=255, required=False)), ('website', wagtail.core.blocks.URLBlock(help_text='add website address', required=False))], required=False)))], required=False)), ('contact_text_editor', streams.blocks.RichTextBlock(label='Contact text editor', required=False))])), ('download_block', wagtail.core.blocks.StructBlock([('news', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.DateBlock(required=True)), ('file_name', wagtail.core.blocks.CharBlock(help_text='file name', max_length=255, required=True)), ('source_type', wagtail.core.blocks.StreamBlock([('audio_video', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=255, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('audio_video', wagtailmedia.blocks.AbstractMediaChooserBlock(help_text='choose audio or video file', required=True))], required=True)), ('hyperlink', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=255, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('hyper_link_url', wagtail.core.blocks.URLBlock(help_text='choose url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab'))], required=True)), ('page_link', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=255, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('page_link', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab'))], required=True)), ('document', wagtail.core.blocks.StructBlock([('source_name', wagtail.core.blocks.CharBlock(help_text='choose source name', max_length=255, required=True)), ('item_relevant_tag', wagtail.core.blocks.ChoiceBlock(choices=[('press_release', 'Press release'), ('webcast', 'Webcast'), ('presentation', 'Presentation'), ('report', 'Report'), ('pdf', 'PDF')], help_text='choose relevant tag associated with download item')), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], required=True))], required=False))])))])), ('iframe_block', wagtail.core.blocks.StructBlock([('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('padding', wagtail.core.blocks.BooleanBlock(label='Add padding', required=False))])), ('image_content_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('image_person_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('name', wagtail.core.blocks.CharBlock(help_text='add name and surname', max_length=255, required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('biography', wagtail.core.blocks.TextBlock(help_text='biography about', required=True))])), ('image_people_block', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=True)), ('name', wagtail.core.blocks.CharBlock(help_text='add name and surname', max_length=255, required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=True)), ('biography', wagtail.core.blocks.TextBlock(help_text='biography about', required=True))])))])), ('newsfeed_block', wagtail.core.blocks.StructBlock([('number_of_news', wagtail.core.blocks.IntegerBlock(required=True))])), ('event_module_block', wagtail.core.blocks.StructBlock([('events', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(help_text='event name', max_length=264, required=True)), ('date', wagtail.core.blocks.DateBlock(required=True)), ('to_be_confirmed', wagtail.core.blocks.ChoiceBlock(choices=[(1, 'Yes'), (0, 'No')]))])))])), ('form_module_block', wagtail.core.blocks.StructBlock([('form', wagtailstreamforms.blocks.FormChooserBlock()), ('form_action', wagtail.core.blocks.CharBlock(help_text='The form post action. "" or "." for the current page or a url', required=False)), ('form_reference', wagtailstreamforms.blocks.InfoBlock(help_text='This form will be given a unique reference once saved', required=False)), ('link_data', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(help_text='add text', max_length=256, required=True)), ('link', wagtail.core.blocks.StreamBlock([('internal_page', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab'))])), ('doc', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))]))], help_text='choose page or document', required=True)), ('error_message', wagtail.core.blocks.CharBlock(help_text='add message', max_length=256, required=True)), ('success_message', wagtail.core.blocks.CharBlock(help_text='add message', max_length=256, required=True)), ('sub_copy', wagtail.core.blocks.CharBlock(help_text='add sub copy', max_length=256, required=True))], required=True))])), ('full_rte_editor', wagtail.core.blocks.StructBlock([('rich_text', streams.blocks.RichTextBlock(required=True)), ('text_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00B7B4', 'Cyan'), ('#00B7B5', 'Blue'), ('#9078D7', 'Violet'), ('#FF6352', 'Orange'), ('#605A70', 'Grey'), ('#241D36', 'Dark blue / Purple'), ('#000000', 'Black')])), ('full_size', wagtail.core.blocks.BooleanBlock(required=False))])), ('hero_banner_block', wagtail.core.blocks.StructBlock([('banner_text', streams.blocks.RichTextBlock(label='Hero banner text', required=True)), ('hyperlink', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='add link', required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab', required=False))])), ('padding_block', wagtail.core.blocks.StructBlock([('padding', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('bottom', 'Bottom')]))])), ('quotation_block', wagtail.core.blocks.StructBlock([('quote_author', wagtail.core.blocks.TextBlock(required=False)), ('author_title', wagtail.core.blocks.TextBlock(required=False)), ('quote_text', wagtail.core.blocks.TextBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab', required=False)), ('optional_padding_above', wagtail.core.blocks.BooleanBlock(help_text='add padding above field', required=False))])), ('table_block', wagtail.core.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock())])), ('timeline_block', wagtail.core.blocks.StructBlock([('timeline', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('year_field', wagtail.core.blocks.CharBlock(max_length=256, required=True)), ('text_editor', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('panel_field', wagtail.core.blocks.CharBlock(max_length=256, required=True)), ('employees_field', wagtail.core.blocks.CharBlock(max_length=256, required=True)), ('offices_field', wagtail.core.blocks.CharBlock(max_length=256, required=True))])))])), ('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('title_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00B7B4', 'Cyan'), ('#00B7B5', 'Blue'), ('#9078D7', 'Violet'), ('#FF6352', 'Orange'), ('#605A70', 'Grey'), ('#241D36', 'Dark blue / Purple'), ('#000000', 'Black')])), ('text', wagtail.core.blocks.TextBlock(help_text='Add addition text', required=False))])), ('two_columns_block', wagtail.core.blocks.StructBlock([('social_links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('social_channel_logo', wagtail.core.blocks.ChoiceBlock(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('instagram', 'instagram'), ('rss', 'rss'), ('linkedin', 'linkedin')], help_text='choose social channel logo')), ('social_channel_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], required=False))), ('left_widget', wagtail.core.blocks.StreamBlock([('link_container', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False)), ('two_columns', wagtail.core.blocks.StructBlock([('left', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False)), ('right', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False))], required=False)), ('iframe', wagtail.core.blocks.StructBlock([('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=False)), ('padding', wagtail.core.blocks.BooleanBlock(label='Add padding', required=False)), ('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color'))], required=False)), ('news_feed', wagtail.core.blocks.StructBlock([('number_of_news', wagtail.core.blocks.IntegerBlock(required=True))], required=False)), ('quick_links', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('title_color', wagtail.core.blocks.ChoiceBlock(choices=[('#00B7B4', 'Cyan'), ('#00B7B5', 'Blue'), ('#9078D7', 'Violet'), ('#FF6352', 'Orange'), ('#605A70', 'Grey'), ('#241D36', 'Dark blue / Purple'), ('#000000', 'Black')])), ('subtitle', wagtail.core.blocks.TextBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))])))], required=False)), ('quote', wagtail.core.blocks.StructBlock([('quote_author', wagtail.core.blocks.TextBlock(required=False)), ('author_title', wagtail.core.blocks.TextBlock(required=False)), ('quote_text', wagtail.core.blocks.TextBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab', required=False)), ('optional_padding_above', wagtail.core.blocks.BooleanBlock(help_text='add padding above field', required=False))], required=False)), ('callouts', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('callouts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('callout', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('subcopy', wagtail.core.blocks.CharBlock(max_length=255, required=True))])))], required=False)), ('board_of_directors', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False))], label='Left widget', required=False)), ('right_widget', wagtail.core.blocks.StreamBlock([('link_container', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False)), ('two_columns', wagtail.core.blocks.StructBlock([('left', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False)), ('right', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False))], required=False)), ('iframe', wagtail.core.blocks.StructBlock([('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=False)), ('padding', wagtail.core.blocks.BooleanBlock(label='Add padding', required=False)), ('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color'))], required=False)), ('news_feed', wagtail.core.blocks.StructBlock([('number_of_news', wagtail.core.blocks.IntegerBlock(required=True))], required=False)), ('quick_links', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('title_color', wagtail.core.blocks.ChoiceBlock(choices=[('#00B7B4', 'Cyan'), ('#00B7B5', 'Blue'), ('#9078D7', 'Violet'), ('#FF6352', 'Orange'), ('#605A70', 'Grey'), ('#241D36', 'Dark blue / Purple'), ('#000000', 'Black')])), ('subtitle', wagtail.core.blocks.TextBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))])))], required=False)), ('quote', wagtail.core.blocks.StructBlock([('quote_author', wagtail.core.blocks.TextBlock(required=False)), ('author_title', wagtail.core.blocks.TextBlock(required=False)), ('quote_text', wagtail.core.blocks.TextBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab', required=False)), ('optional_padding_above', wagtail.core.blocks.BooleanBlock(help_text='add padding above field', required=False))], required=False)), ('callouts', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('callouts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('callout', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('subcopy', wagtail.core.blocks.CharBlock(max_length=255, required=True))])))], required=False)), ('board_of_directors', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False))], label='Right widget', required=False))])), ('video_block', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.TextBlock(required=False)), ('sub_copy', wagtail.core.blocks.TextBlock(required=False)), ('video_thumbnail', wagtail.images.blocks.ImageChooserBlock(required=False)), ('media_chooser', wagtail.core.blocks.StreamBlock([('video_url', wagtail.embeds.blocks.EmbedBlock()), ('video_file', wagtailmedia.blocks.AbstractMediaChooserBlock(icon='media'))], max_num=1, required=False)), ('link', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab', required=False))])), ('widget_block', wagtail.core.blocks.StreamBlock([('link_container', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False)), ('two_columns', wagtail.core.blocks.StructBlock([('left', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False)), ('right', wagtail.core.blocks.StructBlock([('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color', required=False)), ('title', wagtail.core.blocks.CharBlock(help_text='add title', max_length=255, required=False)), ('content', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='choose image', required=False)), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))], required=False))], required=False)), ('iframe', wagtail.core.blocks.StructBlock([('hyperlink', wagtail.core.blocks.URLBlock(help_text='add url', required=False)), ('padding', wagtail.core.blocks.BooleanBlock(label='Add padding', required=False)), ('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('#00b7b5', 'Cyan'), ('#9078d7', 'Violet'), ('#605a70', 'Grey'), ('#241d36', 'Dark'), ('#DC4C81', 'Pink')], help_text='background color'))], required=False)), ('news_feed', wagtail.core.blocks.StructBlock([('number_of_news', wagtail.core.blocks.IntegerBlock(required=True))], required=False)), ('quick_links', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('title_color', wagtail.core.blocks.ChoiceBlock(choices=[('#00B7B4', 'Cyan'), ('#00B7B5', 'Blue'), ('#9078D7', 'Violet'), ('#FF6352', 'Orange'), ('#605A70', 'Grey'), ('#241D36', 'Dark blue / Purple'), ('#000000', 'Black')])), ('subtitle', wagtail.core.blocks.TextBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], help_text='choose page or doc', required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open page on new or current tab', required=False))])))], required=False)), ('quote', wagtail.core.blocks.StructBlock([('quote_author', wagtail.core.blocks.TextBlock(required=False)), ('author_title', wagtail.core.blocks.TextBlock(required=False)), ('quote_text', wagtail.core.blocks.TextBlock(required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_url', wagtail.core.blocks.URLBlock(required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab', required=False)), ('optional_padding_above', wagtail.core.blocks.BooleanBlock(help_text='add padding above field', required=False))], required=False)), ('callouts', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('callouts', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('callout', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('subcopy', wagtail.core.blocks.CharBlock(max_length=255, required=True))])))], required=False)), ('board_of_directors', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('link_text', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('link_or_doc', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('document', wagtail.documents.blocks.DocumentChooserBlock(help_text='choose file eg. PDF', required=True))], required=False)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False))])), ('full_rich_text', streams.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
