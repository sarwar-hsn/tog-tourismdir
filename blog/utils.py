import datetime
from django.conf import settings
from .models import Post,Tag,Category,CategoryBangla,BanglaBlog
from django.core.paginator import Paginator
from mainapp.models import SocialMedia


RCTPST = 'recent_blogs_en'
RCTBNPST = 'recent_blogs_bn'
BLANG = 'blog_lang'

#lang can be either english or bangla
def set_blog_lang(request,lang):
    request.session[BLANG] = lang
    request.session.modified = True

def retrieve_blog_lang(request):
    if BLANG in request.session:
        return request.session[BLANG];
    return 'en'
        

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
def popular_blogs(request):
    lang = retrieve_blog_lang(request)
    if lang == 'bn':
        blogs = BanglaBlog.objects.filter(status=BanglaBlog.PUBLISHED).order_by('-view_count')[:6]
        return blogs
    else:
        return Post.objects.filter(status=Post.PUBLISHED).order_by('-view_count')[:6]

#blog recommendation
def blog_recommend(last_reads):
    pass



def determine_language_from_post(request,blog_slug):
    post = BanglaBlog.objects.filter(slug=blog_slug)
    if post:
        return {'post':post[0],'lang':'bn'}
    else:
        post = Post.objects.filter(slug=blog_slug)
        if post:
            return {'post':post[0],'lang':'en'}
    return None

def build_blog_details(request,blog_slug):
    ctg = None
    tags = None
    determined_post = determine_language_from_post(request, blog_slug)
    if determined_post is None:
        context = {
        'blog':None,
        'tags':None,
        'categories':None,
        'meta':None,
        }
        return context
    else:
        post = determined_post['post']
        lang = determined_post['lang']
        if lang == 'en':
            swlang ='Bangla Blogs'
            swlang_ = 'Bangla'
        else:
            swlang = 'English Blogs'
            swlang_ = "English"
        set_blog_lang(request, lang)
        if lang == 'en':
            ctg = Category.objects.all()
            tags = Tag.objects.all()
        else:
            ctg = CategoryBangla.objects.all()
        context ={
            'blog':post,
            'tags':tags,
            'categories':ctg,
            'meta':post.as_meta(),
            'swlang':swlang,
            'lang':lang,
            'swlang_':swlang_
        }
        return context

def get_switch_lang(request):
    lang = retrieve_blog_lang(request)
    if lang == 'en':
        return "Bangla Blogs"
    else:
        return "English Blogs"


def set_last_read_english(request,blog):
    if RCTPST not in request.session:
        request.session[RCTPST] = [blog.id]
    else:
        #retriving the last read list
        if blog.id in request.session: 
            request.session[RCTPST].remove(blog.id)              
        recent_blogs  =  Post.objects.filter(pk__in=request.session[RCTPST])
        #adding the current blog to the read list
        request.session[RCTPST].insert(0,blog.id)
        request.session.modified = True
        #allowing only 6 items
        if len(request.session[RCTPST]) > 6:
            request.session[RCTPST].pop()
        return recent_blogs

def set_last_read_bangla(request,blog):
    if RCTBNPST not in request.session:
        request.session[RCTBNPST] = [blog.id]
    else:
        #retriving the last read list
        if blog.id in request.session: 
            request.session[RCTBNPST].remove(blog.id)              
        recent_blogs  =  BanglaBlog.objects.filter(pk__in=request.session[RCTBNPST])
        #adding the current blog to the read list
        request.session[RCTBNPST].insert(0,blog.id)
        request.session.modified = True
        #allowing only 6 items
        if len(request.session[RCTBNPST]) > 6:
            request.session[RCTBNPST].pop()
        return recent_blogs
