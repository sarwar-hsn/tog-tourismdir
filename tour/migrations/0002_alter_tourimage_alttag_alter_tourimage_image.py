# Generated by Django 4.1.1 on 2023-03-25 13:39

from django.db import migrations, models
import tour.models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourimage',
            name='alttag',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tourimage',
            name='image',
            field=models.ImageField(upload_to=tour.models.tourimagedirectorypath, validators=[tour.models.validate_image_size]),
        ),
    ]
