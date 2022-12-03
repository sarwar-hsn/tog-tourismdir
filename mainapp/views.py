from django.shortcuts import render
from django.http import HttpResponse
from tour.models import Tour,Destination
from newsletterapp.forms import NewsletterForm


# Create your views here.
def popular_destinations(city1, city2 , city3):
    dest_one = Destination.objects.filter(city=city1)[0]
    dest_set_one = Tour.objects.filter(destinations__city=city1)
    dest_two = Destination.objects.filter(city=city2)[0]
    dest_set_two = Tour.objects.filter(destinations__city=city2)
    dest_three = Destination.objects.filter(city=city3)[0]
    dest_set_three = Tour.objects.filter(destinations__city=city3)
    return {dest_one:dest_set_one,dest_two:dest_set_two,dest_three:dest_set_three}
    
def index(request,*args, **kwargs):
    banners = Tour.objects.all()
    CITY1='istanbul'
    CITY2='antalya'
    CITY3='edirne'
    populardestinations = popular_destinations(CITY1,CITY2,CITY3)
    featured= feautured_packages()
    context = {
        "banners":banners,
        "bestpackages": bestpackages(),
        "populardestinations":populardestinations,
        "featured": featured,
        "form":NewsletterForm,
    }
    return render(request, 'mainapp/views/mainapp_home.html',context=context)

def about(request):
    context ={}
    return render(request, 'mainapp/views/mainapp_about.html', context=context)

def bestpackages():
    packages = Tour.objects.all()
    if(len(packages) > 6):
        packages = packages[0:6]
    return packages


def feautured_packages():
    return Tour.objects.filter(featured=True)
    