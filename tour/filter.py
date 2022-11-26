import django_filters
from django import forms
from .models import Tour,Destination


class TourFilter(django_filters.FilterSet):
    
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='price >=')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='price <=')

    destinations = django_filters.ModelMultipleChoiceFilter(
            queryset=Destination.objects.all(),
            widget=forms.CheckboxSelectMultiple,)

    class Meta:
        model = Tour
        fields = ['price__lt','price__gt','destinations']