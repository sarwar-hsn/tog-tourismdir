from django.shortcuts import render
from django.http import HttpResponse
from tour.models import Tour,Destination
from newsletterapp.forms import NewsletterForm
from blog.models import Post
from .models import HomeBanner,PopularDest,Seo,SocialMedia
from tour.forms import BookingForm
from . import utils


#views
def index(request,*args, **kwargs):
    return HttpResponse("<h2>fuck this life</h2>")
    # destinations = PopularDest.objects.all()
    # popular_dest = {}
    # for dest in destinations:
    #     city = str(dest.destination)
    #     tours = Tour.objects.filter(destinations__city=city)
    #     popular_dest[dest.destination]=tours
    # banners =  HomeBanner.objects.all()
    # fb = utils.featured_blogs()
    # context = {
    #     "banners":banners,
    #     "bestpackages": utils.bestpackages(),
    #     "populardestinations":popular_dest,
    #     "form":NewsletterForm,
    #     "blogs":fb,
    #     "seo":utils.get_seo('home'),
    #     "contact":utils.retrive_contacts()
    # }
    # return render(request, 'mainapp/views/mainapp_home.html',context=context)

def about(request):
    context ={
        'seo':utils.get_seo('about'),
        "contact":utils.retrive_contacts(),
    }
    return render(request, 'mainapp/views/mainapp_about.html', context=context)

def contact(request):
    context ={
        'seo':utils.get_seo('contact'),
        "contact":utils.retrive_contacts(),
        "form":BookingForm()
    }
    return render(request, "mainapp/views/mainapp_contact.html",context=context)


def error_404_view(request, exception):
    return render(request, 'error_404.html')