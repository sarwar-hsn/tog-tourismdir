from django.urls import path
from . import views


urlpatterns = [
    path('tags/<str:hashtag>/',views.blog_tags,name='blog-tags'),
    path('',views.index,name='blog-home'),
    path('search/',views.blog_search,name='blog-search'),
    path('<slug:category_slug>/',views.categorydetails,name='blog-categorydetails'),
    path('<slug:category_slug>/<slug:blog_slug>/',views.blogdetails,name='blog-detail')
]
