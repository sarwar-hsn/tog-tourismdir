import os
from django.db import models
from django.db.models.signals import post_delete,pre_save,post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from datetime import datetime
from django.urls import reverse
    

#destination class start
def destination_thumb_path(instance,filename,*args, **kwargs):
    base,ext = os.path.splitext(filename)
    ext = ext.lower()
    t = datetime.today()
    return f"dest_thumbnails/{instance.country}/{instance.city}/{base}{ext}"


class Destination(models.Model):
    country_options = [
        ('turkey','turkey'),
    ]
    cities = [
        ("istanbul","Istanbul"),
        ("antalya","Antalya"),
        ("muğla","Muğla"),
        ("aydın","Aydın"),
        ("izmir","İzmir"),
        ("nevşehir","Nevşehir"),
        ("edirne","Edirne"),
        ("bursa","Bursa"),
        ("konya","Konya"),
        ("sanlıurfa","Şanlıurfa"),
        ("ankara","Ankara")
    ]
    country = models.CharField(max_length=20,choices=country_options)
    city = models.CharField(choices=cities, max_length=35,unique=True)
    view_count = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(upload_to=destination_thumb_path)
    alttag = models.CharField(max_length=100)

    def __str__(self):
        return str(self.city)

    

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
    min_size = models.IntegerField(default=1)
    max_size = models.IntegerField(default=1)
    destinations = models.ManyToManyField(Destination)
    accommodation = models.TextField()
    transportation = models.TextField()
    overview = models.CharField( max_length=250,null=True,blank=True)
    description = models.TextField()
    meta=models.CharField(max_length=300,blank=True,null=True)
    imagelink = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)



    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse("tour-detail", kwargs={"tour_slug": self.slug})

    
    def getthumbnail(self):
        thumbnail = self.tourimage_set.all().first()
        return thumbnail

    def getgallary(self):
        images = self.tourimage_set.all()
        if len(images) >= 2:
            galleryphotos = images[1:]
            return galleryphotos
        else:
            return None

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
    alttag = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.pk}"


class Booking(models.Model):
    contact_choice = [
        ('whatsapp','whatsapp'),
        ('email','email'),
        ('phone','phone')
    ]
    packageId = models.BigIntegerField(null=True,blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    phone_number = models.CharField(max_length=15)
    contact_pref = models.CharField(max_length=20,choices=contact_choice)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    
    def __str__(self):
        return f"{self.email}-{self.name}"

class BookingExtended(models.Model):
    contact_choice = [
        ('whatsapp','whatsapp'),
        ('email','email'),
        ('phone','phone')
    ]

    acc_choice = [
        ('5-star','5-Star'),
        ('4-star','4-Star'),
        ('3-star','3-Star'),
        ('airbnb','Airbnb')
    ]

    trans_choice = [
        ('taxi','Taxi'),
        ('private_car','Private Car'),
        ('vip_tour','VIP Tour')
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    phone_number = models.CharField(max_length=15)
    contact_pref = models.CharField(max_length=20,choices=contact_choice) 
    arrival = models.CharField(max_length=100)
    depart = models.CharField(max_length=100)
    adult = models.IntegerField(default=1)
    child = models.IntegerField(blank=True,null=True)
    transportation = models.CharField(choices=trans_choice,max_length=50)
    accommodation = models.CharField(choices=acc_choice,max_length=20)
    destinations = models.ManyToManyField(Destination)
    message = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)   
    
    def get_property_values(self):
        values = ""
        values+="created_at\t: "+str(self.created_at)+"\n"
        values+="name\t: "+str(self.name)+"\n"
        values+="email\t: "+str(self.email)+"\n"
        values+="phone_number\t: "+str(self.phone_number)+"\n"
        values+="contact_pref\t: "+str(self.contact_pref)+"\n"
        values+="arrival\t: "+str(self.arrival)+"\n"
        values+="depart\t: "+str(self.depart)+"\n"
        values+="adult\t: "+str(self.adult)+"\n"
        values+="child\t: "+str(self.child)+"\n"
        values+="transportation\t: "+str(self.transportation)+"\n"
        values+="accommodation\t: "+str(self.accommodation)+"\n"
        values+="message\t: "+str(self.message)+"\n"
        values+="places want to visit:\n"
        for dest in self.destinations.all():
            values+=dest.city+" "
        return values
    
    def __str__(self):
        return f"{self.email}-{self.name}"
