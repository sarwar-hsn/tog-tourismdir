from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.index,name='mainapp-home'),
    path('about/',views.about,name="mainapp-about"),
    path('contact/',views.contact,name="mainapp-contact")
]
