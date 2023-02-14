# Generated by Django 4.1.1 on 2023-02-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_rename_pacakgeid_booking_packageid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingExtended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('contact_pref', models.CharField(choices=[('whatsapp', 'whatsapp'), ('email', 'email'), ('phone', 'phone')], max_length=20)),
                ('arrival', models.CharField(max_length=100)),
                ('depart', models.CharField(max_length=100)),
                ('group_size', models.IntegerField(default=1)),
                ('transportation', models.CharField(choices=[('taxi', 'Taxi'), ('private_car', 'Private Car'), ('vip_tour', 'VIP Tour')], max_length=50)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('destinations', models.ManyToManyField(to='tour.destination')),
            ],
        ),
    ]