from django.db import models
from django.db.models.signals import post_delete,pre_save,post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from datetime import datetime
import os
from django.urls import reverse

# Create your models here.


class Destination(models.Model):
    city = models.CharField(max_length=20,null=True,blank=True)
    country = models.CharField(max_length=20,null=True,blank=True)

    
    def __str__(self):
        return self.city
    

class Tour(models.Model):
    TAKA = "BDT"
    USDOLLAR = "USD"
    TURKISHLIRA = "TL"
    EURO = "EUR"
    currency_choice =(
        (TAKA,TAKA),
        (USDOLLAR,USDOLLAR),
        (TURKISHLIRA,TURKISHLIRA),
        (EURO,EURO)
    )
    
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=20,choices=currency_choice,default=TAKA)
    discount = models.PositiveIntegerField()
    durations = models.CharField(max_length=50)
    size = models.IntegerField(default=1)
    destinations = models.ManyToManyField(Destination)
    accommodation = models.TextField()
    transportation = models.TextField()
    overview = models.CharField( max_length=250,null=True,blank=True)
    description = models.TextField()
    meta=models.CharField(max_length=300,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("tour-detail", kwargs={"tour_slug": self.slug})

    
    def getthumbnail(self):
        thumbnail = None
        images = self.tourimage_set.all()
        if images is not None:
            thumbnail = images[0]
        return thumbnail

    def getgalleryimages(self):
        galleryphotos = None
        images = self.tourimage_set.all()
        if len(images) >= 2:
            galleryphotos = images[1:]
        return galleryphotos


    def __str__(self):
        return f"{self.pk}_{self.title}"



def _tour_slug(sender,instance,created, **kwargs):
    if created:
        slug = f"{slugify(instance.title)}-{instance.pk}"
        instance.slug = slug
        instance.save()

post_save.connect(_tour_slug, sender=Tour)
    




def tourimagedirectorypath(instance,filename,*args, **kwargs):
    base,ext = os.path.splitext(filename)
    ext = ext.lower()
    t = datetime.today()
    return f"tourimage/{t.year}/{t.month}/{instance.tour.slug}/{base}{ext}"

class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=tourimagedirectorypath,default=None)
    altText = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.pk}"

@receiver(models.signals.post_delete, sender=TourImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """

    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=TourImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = TourImage.objects.get(pk=instance.pk).image
    except TourImage.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


