import uuid
from django.urls import path
from . import views


urlpatterns = [
    path('sub/',views.subscribe,name='newsletter-subscribe'),
    path('unsub/',views.unsubsribe,name='newsletter-unsubscribe')
]
