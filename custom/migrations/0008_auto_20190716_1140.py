# Generated by Django 2.2.3 on 2019-07-16 11:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0007_auto_20190708_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='menusnippet',
            name='social_channel_links_mobile_menu',
            field=wagtail.core.fields.StreamField([('social_channel_links', wagtail.core.blocks.StructBlock([('social_channel_logo', wagtail.core.blocks.ChoiceBlock(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('instagram', 'instagram'), ('rss', 'rss')], help_text='choose social channel logo')), ('social_channel_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='footersnippet',
            name='social_channel_links',
            field=wagtail.core.fields.StreamField([('social_channel_links', wagtail.core.blocks.StructBlock([('social_channel_logo', wagtail.core.blocks.ChoiceBlock(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('instagram', 'instagram'), ('rss', 'rss')], help_text='choose social channel logo')), ('social_channel_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menusnippet',
            name='menu_links',
            field=wagtail.core.fields.StreamField([('social_channel_links', wagtail.core.blocks.StructBlock([('menu_navigation_level_1', wagtail.core.blocks.StreamBlock([('menu_external_url', wagtail.core.blocks.StructBlock([('displayed_name', wagtail.core.blocks.CharBlock(max_length=16, required=True)), ('url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], help_text='choose url', required=True)), ('menu_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True)), ('menu_anchor_page', wagtail.core.blocks.StructBlock([('displayed_name', wagtail.core.blocks.CharBlock(max_length=16, required=True)), ('navigation_html_id', wagtail.core.blocks.CharBlock(max_length=16, required=True))], help_text='choose anchor page', required=True))], help_text='choose page', required=True)), ('menu_navigation_level_2', wagtail.core.blocks.StreamBlock([('menu_external_url', wagtail.core.blocks.StructBlock([('displayed_name', wagtail.core.blocks.CharBlock(max_length=16, required=True)), ('url', wagtail.core.blocks.URLBlock(help_text='add url', required=True))], help_text='choose url', required=True)), ('menu_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True))], help_text='add nested pages', required=False))]))], blank=True, null=True),
        ),
    ]