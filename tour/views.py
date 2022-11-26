from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Tour
from .filter import TourFilter

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
    }
    return render(request, 'tour/views/tour_detail.html',context=context)
