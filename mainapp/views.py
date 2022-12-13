from django.shortcuts import render
from django.http import HttpResponse
from tour.models import Tour,Destination
from newsletterapp.forms import NewsletterForm
from blog.models import Post


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
    CITY1='istanbul'
    CITY2='antalya'
    CITY3='edirne'
    populardestinations = popular_destinations(CITY1,CITY2,CITY3)
    fp= feautured_packages()
    fb= featured_blogs()

    context = {
        "banners":fp,
        "bestpackages": bestpackages(),
        "populardestinations":populardestinations,
        "form":NewsletterForm,
        "blogs":fb
    }
    return render(request, 'mainapp/views/mainapp_home.html',context=context)

def about(request):
    context ={}
    return render(request, 'mainapp/views/mainapp_about.html', context=context)

def bestpackages():
    packages = Tour.objects.order_by('view_count','-created_at')[:6]
    return packages


def feautured_packages():
    return Tour.objects.filter(featured=True)[:3]

def featured_blogs():
    return Post.objects.filter(featured=True)[:3]