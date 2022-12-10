from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from .models import Tour
from .filter import TourFilter
from .forms import BookingForm
from django.core.mail import send_mail,BadHeaderError

# Create your views here.

def home(request):
    tours = Tour.objects.all()
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
    }
    return render(request, 'tour/views/tour_home.html',context=context)

def detail(request,tour_slug):
    try:
        tour = Tour.objects.get(slug=tour_slug)
    except:
        tour = None
    context = {
        'tour':tour,
        'form':BookingForm,
    }
    return render(request, 'tour/views/tour_detail.html',context=context)



def create_msgbody(booking_obj):
    #
    msg = "\n".join(booking_obj)

def booking(request):
    if request.POST:
        form = BookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = str(obj.name)
            obj.email =str(obj.email)
            obj.phone_number = str(obj.phone_number)
            obj.message = str(obj.message)
            obj.save()
            mail_body =f"time: {str(obj.created_at)}\nemail: {obj.email}\nnumber: {obj.phone_number}\nname: {obj.name}\ncontact preference: {obj.contact_pref}\nmessage: {obj.message}\n"
            try:
                send_mail(
                    'booking query',
                    mail_body,
                    'mail@ottomantravels.com',
                    ['john@example.com'],
                )
                messages.success(request, "we received your request. we will contact soon")
            except:
                messages.error(request, "form submission failed")
        else:
            messages.error(request, "invalid form input")
    return redirect("tour-home")
