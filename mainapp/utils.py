from .models import Seo,Tour,SocialMedia
from blog.models import Post

def get_seo(page_name):
    seo = Seo.objects.filter(page=page_name)
    if len(seo) == 0:
        return None
    else:
        return seo[0]


def bestpackages():
    packages = Tour.objects.order_by('view_count','-created_at')[:6]
    return packages

def feautured_packages():
    return Tour.objects.filter(featured=True)[:3]

def featured_blogs():
    return Post.objects.filter(featured=True)[:3]

def retrive_contacts():
    contact = SocialMedia.objects.all()
    if len(contact) == 0:
        return None
    else:
        return contact[0]