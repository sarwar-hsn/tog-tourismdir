import datetime
from django.conf import settings
from .models import Post,Tag,Category
from django.core.paginator import Paginator
from mainapp.models import SocialMedia


RCTPST = 'recent_blogs'

def build_pagination(request,itemlist,iter_per_page):
    paginator = Paginator(itemlist, 6)
    page_num = request.GET.get('page',1)

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
    return page_obj

#need to improve the algorithm here
def popular_blogs():
    blogs = Post.objects.order_by('-view_count')[:6]
    return blogs

#blog recommendation
def blog_recommend(last_reads):
    pass


def build_blog_details(request,blog_slug):
    ctg = None
    tags = None
    post = None
    try:
        post = Post.objects.get(slug=blog_slug)
    except:
        post = None
    try:
        ctg = Category.objects.all()
        tags = Tag.objects.all()
    except:
        ctg = None
        tags = None
    context ={
        'blog':post,
        'tags':tags,
        'categories':ctg,
    }
    return context


