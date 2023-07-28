from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='tour-home'),
    path('booking/',views.booking,name='tour-booking'),
    path('custom-booking/',views.bookingExt,name='tour-booking-ext'),
    path('<slug:tour_slug>/',views.detail,name='tour-detail'),
    
]
