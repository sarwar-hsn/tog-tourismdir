from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post,Category,Tag
from .forms import BlogSearchForm
from django.db.models import Q
from analyticsapp.signals import object_view_signal



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


# Create your views here.
def index(request):
    ctg = Category.objects.all()
    # posts = Post.objects.filter(status=Post.PUBLISHED).exclude(featured=True)
    posts = Post.objects.filter(status=Post.PUBLISHED)
    featured = Post.objects.filter(featured=True,status=Post.PUBLISHED)
    tags = Tag.objects.all()

    page_obj = build_pagination(request,posts, 6)

    context = {
        'categories':ctg,
        'page_obj' : page_obj,
        'featured' : featured,
        'tags':tags,
    }
    return render(request, 'blog/views/blog_home.html',context=context)


def categorydetails(request,category_slug):
    posts = Post.objects.filter(category__slug=category_slug)
    page_obj = build_pagination(request, posts, 6)
    context ={
        'page_obj':page_obj,
        'categories':Category.objects.all(),
        'tags':Tag.objects.all(),
        'category_slug':category_slug,
    }
    #if the category is available , then send a signal that it was viewed
    try:
        catg = Category.objects.get(slug=category_slug);
    except:
        catg = None
    if catg is not None:
        object_view_signal.send(sender=catg.__class__ , instance = catg, request = request);
    return render(request,'blog/views/category_details.html',context=context)


def blogdetails(request,category_slug,blog_slug):
    try:
        post = Post.objects.get(slug=blog_slug)
        try:
            tags = post.tags.all()
            ctg = Category.objects.all()
        except:
            tags = None
    except:
        post = None

    context ={
        'blog':post,
        'tags':tags,
        'categories':ctg,
    }
    if post is not None:
        object_view_signal.send(sender=post.__class__ , instance = post, request = request);
    return render(request, 'blog/views/blog_detail.html',context=context)


def blog_search(request):
    form = BlogSearchForm()
    results = []
    if 'q' in request.GET:
        form = BlogSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            results = Post.objects.filter(
                Q(title__contains=query) | Q(content__contains=query) | Q(tags__name__contains = query)
            ).distinct()
    ctg = Category.objects.all()
    tags = Tag.objects.all()

    page_obj = build_pagination(request,results, 6)

    context = {
        'form':form,
        'results':results,
        'categories':ctg,
        'tags':tags,
        'page_obj':page_obj,
    }
    return render(request, 'blog/views/search_result.html',context=context)


def blog_tags(request,hashtag):
    
    try:
        tag = Tag.objects.get(name=hashtag)
    except:
        tag = None

    if tag is not None:
        posts = tag.post_set.all()
        #send a signal
        object_view_signal.send(sender=tag.__class__ , instance=tag, request=request);
    else:
        posts = []

    page_obj = build_pagination(request, posts, 6)
    context = {
        'page_obj' : page_obj,
        'tag':hashtag,
    }
    return render(request, 'blog/views/blog_tags.html',context=context)