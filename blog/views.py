from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category,Tag
from .forms import BlogSearchForm
from django.db.models import Q
from analyticsapp.signals import object_view_signal
from . import utils
from mainapp.models import Seo
from mainapp.utils import get_seo,retrive_contacts


# Create your views here.
def index(request):
    ctg = Category.objects.all()
    posts = Post.objects.filter(status=Post.PUBLISHED).order_by('created_at')
    featured = Post.objects.filter(featured=True,status=Post.PUBLISHED)
    tags = Tag.objects.all()

    page_obj = utils.build_pagination(request,posts, 6)
    pb = utils.popular_blogs()
    context = {
        'categories':ctg,
        'page_obj' : page_obj,
        'popular_blogs' : pb,
        'tags':tags,
        'seo':get_seo('blog'),
        'contact':retrive_contacts()
    }
    return render(request, 'blog/views/blog_home.html',context=context)


def categorydetails(request,category_slug):
    posts = Post.objects.filter(category__slug=category_slug)
    page_obj = utils.build_pagination(request, posts, 6)
    
    #if the category is available , then send a signal that it was viewed
    try:
        catg = Category.objects.get(slug=category_slug);
    except:
        catg = None
    if catg is not None:
        object_view_signal.send(sender=catg.__class__ , instance = catg, request = request);
    context ={
        'page_obj':page_obj,
        'categories':Category.objects.all(),
        'tags':Tag.objects.all(),
        'category':catg,
        'contact':retrive_contacts(),
    }
    return render(request,'blog/views/category_details.html',context=context)


def blogdetails(request,category_slug,blog_slug):
    context = utils.build_blog_details(request,blog_slug)
    blog = context.get('blog',None)
    
    if blog is not None:
        object_view_signal.send(sender=blog.__class__ , instance = blog, request = request);
        #setting recent post for the session
        if utils.RCTPST not in request.session:
            request.session[utils.RCTPST] = [blog.id]
        else:
            #retriving the last read list
            if blog.id in request.session: 
                request.session[utils.RCTPST].remove(blog.id)                
            recent_blogs  =  Post.objects.filter(pk__in=request.session[utils.RCTPST])
            #adding the current blog to the read list
            request.session[utils.RCTPST].insert(0,blog.id)
            request.session.modified = True
            #allowing only 6 items
            if len(request.session[utils.RCTPST]) > 6:
                request.session[utils.RCTPST].pop()
            context['recent_blogs']=recent_blogs
            context['contact']=retrive_contacts()
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

    page_obj = utils.build_pagination(request,results, 6)

    context = {
        'form':form,
        'results':results,
        'categories':ctg,
        'tags':tags,
        'page_obj':page_obj,
        'contact':retrive_contacts(),
    }
    return render(request, 'blog/views/search_result.html',context=context)


def blog_tags(request,hashtag):
    try:
        tag = Tag.objects.get(name=hashtag)
    except:
        tag = None

    if tag is not None:
        posts = tag.post_set.all()
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
        'popular_blogs':utils.popular_blogs(),
        'contact':retrive_contacts(),
        
    }
    return render(request, 'blog/views/blog_tags.html',context=context)

