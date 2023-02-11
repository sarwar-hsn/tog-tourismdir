from django.forms import ModelForm
from django import forms
from .models import Booking,BookingExtended

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','phone_number','contact_pref','message']

class BookingFormExtended(BookingForm):
    class Meta:
        model = BookingExtended
        fields =['name','email','phone_number','contact_pref','message','arrival','group_size']
        widgets = {
            'arrival': forms.DateInput(attrs={
                'class': 'input-field check-in',
                'placeholder':'dd-mm-yy',
            }),
        }
    
   
    
    
