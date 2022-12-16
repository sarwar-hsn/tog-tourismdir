from django.shortcuts import render
from django.http import HttpResponse
from tour.models import Tour,Destination
from newsletterapp.forms import NewsletterForm
from blog.models import Post
from .models import HomeBanner,PopularDest,Seo,SocialMedia
from tour.forms import BookingForm


#views
def index(request,*args, **kwargs):
    destinations = PopularDest.objects.all()
    popular_dest = {}
    for dest in destinations:
        city = str(dest.destination)
        tours = Tour.objects.filter(destinations__city=city)
        popular_dest[dest.destination]=tours
    banners =  HomeBanner.objects.all()
    fb = featured_blogs()
    seo = Seo.objects.filter(page="home")
    if seo is not None:
        seo = seo[0]

    context = {
        "banners":banners,
        "bestpackages": bestpackages(),
        "populardestinations":popular_dest,
        "form":NewsletterForm,
        "blogs":fb,
        "seo":seo,
        "contact":retrive_contacts()
    }
    return render(request, 'mainapp/views/mainapp_home.html',context=context)

def about(request):
    seo = Seo.objects.filter(page='about')
    if seo is not None:
        seo = seo[0]
    context ={
        'seo':seo,
        "contact":retrive_contacts(),
    }
    return render(request, 'mainapp/views/mainapp_about.html', context=context)

def contact(request):
    seo = Seo.objects.filter(page='contact')
    if seo is not None:
        seo = seo[0]
    context ={
        'seo':seo,
        "contact":retrive_contacts(),
        "form":BookingForm()
    }
    return render(request, "mainapp/views/mainapp_contact.html",context=context)


#utilities
def bestpackages():
    packages = Tour.objects.order_by('view_count','-created_at')[:6]
    return packages

def feautured_packages():
    return Tour.objects.filter(featured=True)[:3]

def featured_blogs():
    return Post.objects.filter(featured=True)[:3]

def retrive_contacts():
    contact = SocialMedia.objects.all()
    if contact is not None:
        contact = contact[0]
    else:
        contact = None
    return contact