# Generated by Django 4.1.1 on 2023-04-30 23:19

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_alter_tour_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='accommodation',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='tour',
            name='transportation',
            field=tinymce.models.HTMLField(),
        ),
    ]