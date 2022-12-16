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
        return self.tour.slug;
    
    

class PopularDest(models.Model):
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.destination.country}/{self.destination.city}"



class Seo(models.Model):
    
    pages = [
        ('home','home'),
        ('about','about'),
        ('contact','contact'),
        ('tour','tour'),
        ('blog','blog'),
    ]

    page = models.CharField(choices=pages,unique=True,max_length=25)
    title = models.CharField(max_length=50)
    description = models.TextField()
    keywords = models.TextField()    
    imagelink = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.page
    


class SocialMedia(models.Model):
    facebook = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    whatsapp = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    youtube = models.URLField(blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    google_map = models.URLField(blank=True,null=True)

    def __str__(self):
        return f"contactinfo"
    
    
