"""togtourismsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog import urls as blogurls
from django.contrib.auth import urls as authurls
from mainapp import urls as mailappappurls
from django.conf import settings
from django.conf.urls.static import static
from tour import urls as toururls
from newsletterapp import urls as newsletterurls
from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps
from django.contrib.sitemaps import views
from django.views.generic.base import TemplateView


admin.site.site_header = "Ottoman Tours & Travels"
admin.site.site_title = "TOG Tourism Admin Portal"
admin.site.index_title = "Welcome to TOG"

sitemaps = {
    'static':sitemaps.StaticViewSitemap,
    'blog':sitemaps.BlogSiteMap,
    'tour':sitemaps.TourSiteMap,
    'blogcategories':sitemaps.CategorySitemap,
    'blogtags':sitemaps.TagSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/',include(blogurls)),
    path('tours/',include(toururls)),
    path('auth/',include('django.contrib.auth.urls')),
    path('newsletter/',include(newsletterurls)),
    path('',include(mailappappurls)),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.index'),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]


handler404 = 'mainapp.views.error_404_view'

if settings.DEBUG is True:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
