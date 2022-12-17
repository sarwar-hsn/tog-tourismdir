from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from tour.models import Tour,TourImage
from blog.models import Post,Category,Tag


class TourSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    def items(self):
        return Tour.objects.filter()
    def lastmod(self, obj):
        return obj.last_modified


class BlogSiteMap(Sitemap):
    changefreq = "monthly"
    priority = .9

    def items(self):
        return Post.objects.all()

    def lastmod(self,obj):
        return obj.last_modified
        

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    def items(self):
        return ['mainapp:mainapp-home', 'mainapp:mainapp-about', 'mainapp:mainapp-contact',
                'tour-home','blog-home']
    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = .6
    def items(self):
        return Category.objects.all()

class TagSitemap(Sitemap):
    changefreq = "daily"
    priority = .6
    def items(self):
        return Tag.objects.all()
