# Generated by Django 4.1.1 on 2023-05-18 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_categorybangla_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banglablog',
            old_name='eng_blog_url',
            new_name='ref_blog_url',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='ban_blog_url',
            new_name='ref_blog_url',
        ),
    ]