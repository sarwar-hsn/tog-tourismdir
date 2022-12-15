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
    




    
