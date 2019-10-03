# Generated by Django 2.2.3 on 2019-07-02 14:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0004_footersnippet_policy_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='footersnippet',
            name='global_links',
            field=wagtail.core.fields.StreamField([('site_link', wagtail.core.blocks.StructBlock([('link_name', wagtail.core.blocks.TextBlock(help_text='add your callout', required=True)), ('link_page', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab'))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footersnippet',
            name='site_links',
            field=wagtail.core.fields.StreamField([('site_link', wagtail.core.blocks.StructBlock([('link_name', wagtail.core.blocks.TextBlock(help_text='add your callout', required=True)), ('link_page', wagtail.core.blocks.StreamBlock([('link_external_url', wagtail.core.blocks.URLBlock(help_text='add url', required=True)), ('link_internal_page', wagtail.core.blocks.PageChooserBlock(help_text='choose page', required=True))], help_text='choose one type of url you want to use', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab'))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='footersnippet',
            name='policy_links',
            field=wagtail.core.fields.StreamField([('policy_link', wagtail.core.blocks.StructBlock([('link_name', wagtail.core.blocks.TextBlock(help_text='add your callout', required=True)), ('link_page', wagtail.core.blocks.PageChooserBlock(help_text='choose internal page', required=True)), ('link_tab_chooser', wagtail.core.blocks.ChoiceBlock(choices=[('_self', 'Current Tab'), ('_blank', 'New Tab')], help_text='choose either open image on new or current tab'))]))], blank=True, null=True),
        ),
    ]
