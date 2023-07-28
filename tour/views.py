from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from .models import Tour
from .filter import TourFilter
from .forms import BookingForm
from .forms import BookingFormExtended
from django.core.mail import send_mail,BadHeaderError
from analyticsapp.signals import object_view_signal
from mainapp.models import Seo,SocialMedia
from mainapp.utils import get_seo,retrive_contacts
from django.conf import settings
from mainapp import utils as seo_utils

#tour/packages homepage
def home(request):
    tours = Tour.objects.all().order_by('-created_at')
    f = TourFilter(request.GET, queryset=tours)
    has_filter = any(field in request.GET for field in set(f.get_fields()))
    paginator = Paginator(f.qs, 6)
    page_num = request.GET.get('page', 1)
    try:
        if int(page_num) <= 0:
            page_num = 1
        elif int(page_num) > paginator.num_pages:
            page_num = paginator.num_pages
    except:
        page_num = 1;

    try:
        page_obj = paginator.get_page(page_num)
    except:
        page_obj = []

    context = {
        'filter':f,
        'page_obj':page_obj,
        'hasFilter':has_filter,
        'form':BookingForm,
        'meta':seo_utils.meta_packages_home(),
        'contact':retrive_contacts(),

    }
    return render(request, 'tour/views/tour_home.html',context=context)

def detail(request,tour_slug):
    try:
        tour = Tour.objects.get(slug=tour_slug)
        popular_tours = Tour.objects.order_by('view_count','-created_at')[:4]
    except:
        tour = None
        popular_tours = None
    if tour is not None:
        object_view_signal.send(sender=tour.__class__,instance=tour,request=request)
    context = {
        'tour':tour,
        'meta' : tour.as_meta(),
        'form':BookingForm,
        'popular_tours':popular_tours,
        'contact':retrive_contacts(),
    }
    return render(request, 'tour/views/tour_detail.html',context=context)


def booking(request):
    if request.POST:
        tourid = request.POST.get('packageid')
        form = BookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = str(obj.name)
            obj.email =str(obj.email)
            obj.phone_number = str(obj.phone_number)
            obj.message = str(obj.message)
            if tourid is not None:
                obj.packageId = tourid
            try:
                obj.save()
            except:
                pass
            
            mail_body =f"requested tour id: {tourid}\ntime:{str(obj.created_at)}\nemail:{obj.email}\nnumber:{obj.phone_number}\nname:{obj.name}\ncontact preference:{obj.contact_pref}\nmessage:{obj.message}\n"
            try:
                send_mail(
                    'booking query',
                    mail_body,
                    'it@ottomangrp.com',
                    ['info@ottomantravels.com'],
                )
                messages.success(request, "we received your request. we will contact soon")
            except:
                messages.error(request, "form submission failed")
        else:
            messages.error(request, "invalid form input")
    return redirect("tour-home")

def bookingExt(request):
    if request.POST:
        form = BookingFormExtended(request.POST)
        if form.is_valid():
            obj = form.save()
            mail_body = obj.get_property_values()
            try:
                send_mail(
                    'custom booking query',
                    mail_body,
                    'it@ottomangrp.com',
                    ['info@ottomantravels.com'],
                )
                messages.success(request, "we received your request. we will contact soon")
            except:
                messages.error(request, "form submission failed")
            return redirect("tour-home")
    else:
        form = BookingFormExtended()
    return render(request, 'tour/views/booking.html',context={'form':form})

