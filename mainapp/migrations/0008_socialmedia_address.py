# Generated by Django 4.1.1 on 2022-12-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_socialmedia_website_socialmedia_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
