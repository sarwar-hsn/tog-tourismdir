from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Category,Tag,CategoryBangla,BanglaBlog
from .forms import BlogSearchForm
from django.db.models import Q
from analyticsapp.signals import object_view_signal
from . import utils
from mainapp.models import Seo
from mainapp.utils import get_seo,retrive_contacts
from mainapp import utils as seo_utils

#blog homepage
def index(request):
    lang = utils.retrieve_blog_lang(request)
    posts = tags = ctg = None
    featured = None
    posts = None
    if(lang == 'bn'):
        ctg = CategoryBangla.objects.all()
        posts = BanglaBlog.objects.filter(status=BanglaBlog.PUBLISHED).order_by('created_at')
        #featured = BanglaBlog.objects.filter(featured=True,status=BanglaBlog.PUBLISHED)
    else:
        ctg = Category.objects.all()
        posts = Post.objects.filter(status=Post.PUBLISHED).order_by('created_at')
        featured = Post.objects.filter(featured=True,status=Post.PUBLISHED)
        tags = Tag.objects.all()
    
    page_obj = utils.build_pagination(request,posts, 6)
    pb = utils.popular_blogs(request)
    context = {
        'categories':ctg,
        'page_obj' : page_obj,
        'popular_blogs' : pb,
        'tags':tags,
        'meta':seo_utils.meta_blog_home(),
        'contact':retrive_contacts(),
        'swlang':utils.get_switch_lang(request),
    }
    return render(request, 'blog/views/blog_home.html',context=context)

#blog category page
def categorydetails(request,category_slug):
    lang = utils.retrieve_blog_lang(request)
    tags = None
    if lang == 'en':
        posts = Post.objects.filter(category__slug=category_slug,status=Post.PUBLISHED)
        catg = Category.objects.filter(slug=category_slug)
        tags = Tag.objects.all()
        categories = Category.objects.all()
    else:
        posts = BanglaBlog.objects.filter(category__slug=category_slug,status=BanglaBlog.PUBLISHED)
        catg = CategoryBangla.objects.filter(slug=category_slug)
        categories = CategoryBangla.objects.all()

    page_obj = utils.build_pagination(request, posts, 6)
    pb = utils.popular_blogs(request)
    if catg:
        catg=catg[0]
        object_view_signal.send(sender=catg.__class__ , instance = catg, request = request);
    
    context ={
        'page_obj':page_obj,
        'popular_blogs' : pb,
        'categories':categories,
        'tags':tags,
        'category':catg,
        'contact':retrive_contacts(),
        'meta':seo_utils.meta_blog_category(),
        'swlang':utils.get_switch_lang(request)
    }
    return render(request,'blog/views/category_details.html',context=context)

#blog details page
def blogdetails(request,category_slug,blog_slug):
    context = utils.build_blog_details(request,blog_slug)
    context['contact']=retrive_contacts()
    try:
        blog = context.get('blog',None)
        if blog:
            lang = context.get('lang')
            if lang == 'bn':
                if blog.ref_blog:
                    context['ref_blog']=blog.ref_blog
            else:
                banglablogref = BanglaBlog.objects.filter(ref_blog=blog)
                if banglablogref:
                    context['ref_blog']=banglablogref.first()
            object_view_signal.send(sender=blog.__class__ , instance = blog, request = request);
            #setting recent post for the session
            if lang == 'bn':
                context['recent_blogs']=utils.set_last_read_bangla(request,blog)
                print(f"lang:{lang}, lastread:{utils.set_last_read_bangla(request, blog)}")
            else:
                context['recent_blogs']=utils.set_last_read_english(request,blog)
    except:
        pass
    return render(request, 'blog/views/blog_detail.html',context=context)

       
def blog_search(request):
    lang = utils.retrieve_blog_lang(request)
    form = BlogSearchForm()
    results = []
    ctg =tags= None
    if 'q' in request.GET:
        form = BlogSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            if lang == 'bn':
                results = BanglaBlog.objects.filter(
                    Q(title__contains=query) | Q(content__contains=query)).distinct().filter(status=BanglaBlog.PUBLISHED)
                ctg = CategoryBangla.objects.all()
                tags = None
            else:
                results = Post.objects.filter(
                    Q(title__contains=query) | Q(content__contains=query) | Q(tags__name__contains = query)
                ).distinct().filter(status=Post.PUBLISHED)
                ctg = Category.objects.all()
                tags = Tag.objects.all()
        else:
            if lang == 'bn':
                ctg = CategoryBangla.objects.all()
                tags = None
            else:
                ctg = Category.objects.all()
                tags = Tag.objects.all()

    page_obj = utils.build_pagination(request,results, 6)
    context = {
        'form':form,
        'results':results,
        'categories':ctg,
        'tags':tags,
        'page_obj':page_obj,
        'contact':retrive_contacts(),
        'swlang':utils.get_switch_lang(request),
    }
    return render(request, 'blog/views/search_result.html',context=context)

#blog hashtag page
def blog_tags(request,hashtag):
    try:
        tag = Tag.objects.get(name=hashtag)
    except:
        tag = None

    if tag is not None:
        posts = tag.post_set.all().filter(status=Post.PUBLISHED)
        page_obj = utils.build_pagination(request, posts, 6)
        #send a signal
        object_view_signal.send(sender=tag.__class__ , instance=tag, request=request);
    else:
        posts = []

    context = {
        'page_obj' : page_obj,
        'tag':tag,
        'tags':Tag.objects.all(),
        'categories':Category.objects.all(),
        'popular_blogs':utils.popular_blogs(request),
        'contact':retrive_contacts(),
        'meta':seo_utils.meta_blog_hashtag(),
        'swlang':utils.get_switch_lang(request)
        
    }
    return render(request, 'blog/views/blog_tags.html',context=context)

def switch_lang(request):
    lang = utils.retrieve_blog_lang(request)
    print(f"currentlang from switch blog:{lang}")
    if lang == 'en':
        print(f"currentlang from switch blog:{lang}")
        utils.set_blog_lang(request, 'bn')
    else:
        utils.set_blog_lang(request, 'en')
    return redirect('blog-home')