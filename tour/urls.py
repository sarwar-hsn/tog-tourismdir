from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='tour-home'),
    path('<slug:tour_slug>/',views.detail,name='tour-detail')
]
