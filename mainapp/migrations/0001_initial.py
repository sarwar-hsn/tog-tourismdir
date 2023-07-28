# Generated by Django 4.1.1 on 2023-03-25 08:56

from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('home', 'home'), ('about', 'about'), ('contact', 'contact'), ('packages_home', 'packages_home'), ('blog_home', 'blog_home'), ('blog_category', 'blog_category'), ('blog_hashtag', 'blog_hashtag'), ('book_custom_tour', 'book_custom_tour')], max_length=40, unique=True)),
                ('seo_title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('keywords', models.TextField(blank=True, default='The Ottoman Group, tog,Turkiye, Real Estate, Turkish Citizenship study in turkey, Turkey,Tourism,turkish tourism,health tourism', null=True)),
                ('page_url', models.URLField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('locale', models.CharField(default='en_US', max_length=10)),
                ('use_og', models.BooleanField(default=False)),
                ('use_twitter', models.BooleanField(default=False)),
                ('use_facebook', models.BooleanField(default=False)),
                ('use_schemaorg', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('whatsapp', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('google_map', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PopularDest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.destination')),
            ],
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to=mainapp.models.bannerdirectory)),
                ('alttag', models.CharField(max_length=100)),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
            ],
        ),
    ]
