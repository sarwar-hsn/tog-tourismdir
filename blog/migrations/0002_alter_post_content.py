# Generated by Django 4.1.1 on 2023-04-30 23:13

from django.db import migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
