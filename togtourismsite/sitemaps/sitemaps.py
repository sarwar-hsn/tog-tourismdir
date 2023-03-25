from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from tour.models import Tour,TourImage
from blog.models import Post,Category,Tag



class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'
    protocol = 'https'
    def items(self):
        return ['mainapp:mainapp-home', 'mainapp:mainapp-about', 'mainapp:mainapp-contact',
                'tour-home','blog-home']
    def location(self, item):
        return reverse(item)


class TourSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = 'https'
    def items(self):
        return Tour.objects.all().order_by('-created_at').distinct()
    def lastmod(self, obj):
        return obj.last_modified


class BlogSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = 'https'
    def items(self):
        return Post.objects.filter(status='published').order_by('-created_at').distinct()

    def lastmod(self,obj):
        return obj.last_modified
        


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = .7
    protocol = 'https'
    def items(self):
        return Category.objects.all().distinct()

class TagSitemap(Sitemap):
    changefreq = "daily"
    priority = .7
    protocol = 'https'
    def items(self):
        return Tag.objects.all().distinct()
