from django.forms import ModelForm
from django import forms
from .models import Booking
from .models import BookingExtended,Destination

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','phone_number','contact_pref','message']

class BookingFormExtended(ModelForm):

    class Meta:
        model = BookingExtended
        fields =['name','email','phone_number','arrival','depart','no_of_persons','transportation','destinations','contact_pref','message',]
        widgets = {
            'arrival': forms.DateInput(attrs={
                'class': 'input-field check-in',
                'placeholder':'dd-mm-yy',
            }),
            'depart': forms.DateInput(attrs={
                'class': 'input-field check-in',
                'placeholder':'dd-mm-yy',
            }),
            'group_size':forms.TextInput(
                attrs={
                    'placeholder':'no. of persons'
                }
            ),
            'message': forms.Textarea(attrs={'rows':3}),
        }

    destinations = forms.ModelMultipleChoiceField(
            queryset=Destination.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True)

    
   
    
    
