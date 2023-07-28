from .models import Seo,Tour,SocialMedia
from blog.models import Post
from meta.views import Meta

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


#seo of different pages
def meta_home():
    seo_obj = Seo.objects.filter(page='home')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_about():
    seo_obj = Seo.objects.filter(page='about')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_contact():
    seo_obj = Seo.objects.filter(page='contact')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_packages_home():
    seo_obj = Seo.objects.filter(page='packages_home')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_blog_home():
    seo_obj = Seo.objects.filter(page='blog_home')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_blog_category():
    seo_obj = Seo.objects.filter(page='blog_category')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_blog_hashtag():
    seo_obj = Seo.objects.filter(page='blog_hashtag')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta

def meta_book_custom_tour():
    seo_obj = Seo.objects.filter(page='book_custom_tour')
    if len(seo_obj) < 1:
        return None
    else:
        seo_obj = seo_obj[0]
        meta = Meta(
            use_og = seo_obj.use_og,
            use_twitter = seo_obj.use_twitter,
            use_facebook = seo_obj.use_facebook,
            use_schemaorg = seo_obj.use_schemaorg,
            title=seo_obj.seo_title,
            description=seo_obj.description,
            keywords=seo_obj.string_to_array(),
            url=seo_obj.page_url,
            image=seo_obj.image_url,
            locale=seo_obj.locale,
        )
        return meta