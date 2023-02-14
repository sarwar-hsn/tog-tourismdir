from django.contrib import admin
from .models import Tour,TourImage,Destination,Booking,BookingExtended
from django import forms

# Register your models here.

admin.site.register(Destination)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    ordering=['-created_at']

@admin.register(BookingExtended)
class BookingExtAdmin(admin.ModelAdmin):
    ordering=['-created_at']

class TourImageAdmin(admin.StackedInline):
    model = TourImage

class TourAdmin(admin.ModelAdmin):
    inlines =[TourImageAdmin]
    def get_form(self, request, obj=None, **kwargs):
        form = super(TourAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['destinations'].widget = forms.CheckboxSelectMultiple()
        return form


admin.site.register(Tour,TourAdmin)
