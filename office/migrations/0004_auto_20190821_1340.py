# Generated by Django 2.2.4 on 2019-08-21 13:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20190821_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeHQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('country_name', models.CharField(blank=True, max_length=255, null=True)),
                ('office_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_3', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('did_you_know', models.TextField(blank=True, null=True)),
                ('office_component', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_offices_hq', to='office.OfficeComponent')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Office',
        ),
    ]
