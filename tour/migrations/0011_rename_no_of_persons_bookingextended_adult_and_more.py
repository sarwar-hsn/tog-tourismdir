# Generated by Django 4.1.1 on 2023-02-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0010_rename_group_size_bookingextended_no_of_persons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingextended',
            old_name='no_of_persons',
            new_name='adult',
        ),
        migrations.AddField(
            model_name='bookingextended',
            name='accommodation',
            field=models.CharField(choices=[('5-star', '5-Star'), ('4-star', '4-Star'), ('3-star', '3-Star'), ('airbnb', 'Airbnb')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingextended',
            name='child',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]