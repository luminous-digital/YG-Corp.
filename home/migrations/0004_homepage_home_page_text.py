# Generated by Django 2.2.2 on 2019-06-07 12:33

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_page_text',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
