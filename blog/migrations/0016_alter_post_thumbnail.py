# Generated by Django 4.1.1 on 2022-12-02 07:03

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to=blog.models.post_directory_path),
            preserve_default=False,
        ),
    ]
