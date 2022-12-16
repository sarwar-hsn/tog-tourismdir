from .models import Seo,Tour,SocialMedia
from blog.models import Post

def get_seo(page_name):
    seo = Seo.objects.filter(page=page_name)
    if seo is not None:
        seo = seo[0]
    else:
        seo = None
    return seo


def bestpackages():
    packages = Tour.objects.order_by('view_count','-created_at')[:6]
    return packages

def feautured_packages():
    return Tour.objects.filter(featured=True)[:3]

def featured_blogs():
    return Post.objects.filter(featured=True)[:3]

def retrive_contacts():
    contact = SocialMedia.objects.all()
    if contact is not None:
        contact = contact[0]
    else:
        contact = None
    return contact