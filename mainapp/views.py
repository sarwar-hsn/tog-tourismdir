from django.shortcuts import render
from django.http import HttpResponse
from tour.models import Tour

# Create your views here.
def index(request):
    banners = Tour.objects.all()
    populardestinations = popular_destinations("istanbul", "gebze", "antalya")
    featured= feautured_packages()
    context = {
        "banners":banners,
        "bestpackages": bestpackages(),
        "populardestinations":populardestinations,
        "featured": featured,
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

def popular_destinations(city1, city2 , city3):
    dest_set_one = Tour.objects.filter(destinations__city=city1)
    dest_set_two = Tour.objects.filter(destinations__city=city2)
    dest_set_three = Tour.objects.filter(destinations__city=city3)
    return {city1:dest_set_one,city2:dest_set_two,city3:dest_set_three}
    
def feautured_packages():
    return Tour.objects.filter(featured=True)
    