from django.db import models
from tour.models import Tour,Destination
import os


def bannerdirectory(instance,filename,*args, **kwargs):
    base,ext = os.path.splitext(filename)
    ext = ext.lower()
    return f"homebanners/{base}{ext}"

class HomeBanner(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE,null=True,blank=True)
    banner = models.ImageField(upload_to=bannerdirectory)
    alttag = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk}-{self.alttag}";
    
    

class PopularDest(models.Model):
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.destination.country}/{self.destination.city}"



class Seo(models.Model):
    DEFAULT_KEYWORDS = "Ottoman travels, Tourism in Turkey, Private Tourism in Turkiye, Best Tourism in Turkey, Tours and Travels, Tour Guide in Istanbul, Trip to Istanbul, Visit in Turkey, Tourist Attractions in Istanbul, Medical Tourism, Tourist Places in Turkey, Travel and Tourism, Tourist Spot, Adventure Tourism, Tourist Destination, Private Tour Package in Istanbul, Best Tourist places in the world, Cheap Tour Package in Turkey"
    pages = [
        ('home','home'),
        ('about','about'),
        ('contact','contact'),
        ('packages_home','packages_home'),
        ('blog_home','blog_home'),
        ('blog_category','blog_category'),
        ('blog_hashtag','blog_hashtag'),
        ('book_custom_tour','book_custom_tour'),
    ] 
    page = models.CharField(max_length=40,choices=pages,unique=True)
    seo_title = models.CharField(max_length=100,)
    description = models.TextField(blank=True,null=True)
    keywords = models.TextField(blank=True,null=True,default=DEFAULT_KEYWORDS)
    page_url = models.URLField(max_length=200,blank=True,null=True)
    image_url = models.URLField(blank=True,null=True)
    locale = models.CharField(max_length=10,default='en_US')
    use_og = models.BooleanField(default=False)
    use_twitter = models.BooleanField(default=False)
    use_facebook = models.BooleanField(default=False)
    use_schemaorg = models.BooleanField(default=False)

    def string_to_array(self):
        return self.keywords.split(sep=",")

    def __str__(self):
        return self.page
    
    
class SocialMedia(models.Model):
    facebook = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    whatsapp = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=25,blank=True,null=True)
    youtube = models.URLField(blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    google_map = models.URLField(blank=True,null=True)

    def __str__(self):
        return f"contactinfo"
    
    
