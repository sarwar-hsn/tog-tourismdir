from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='blog-home'),
    path('tags/<str:hashtag>/',views.blog_tags,name='blog-tags'),
    path('search/',views.blog_search,name='blog-search'),
    path('switch-lang/',views.switch_lang,name='blog-switchlang'),
    path('<slug:category_slug>/',views.categorydetails,name='blog-categorydetails'),
    path('<slug:category_slug>/<slug:blog_slug>/',views.blogdetails,name='blog-detail')
]
