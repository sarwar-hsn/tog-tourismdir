from django.forms import ModelForm
from django import forms
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','phone_number','contact_pref','message']
   
    
    
# class BookingForm(forms.Form):
#     contact_choice = [
#         ('whatsapp','whatsapp'),
#         ('email','email'),
#         ('phone','phone')
#     ]
#     name = forms.CharField(label='name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'name'}))
#     email = forms.EmailField(label="email", required=True, widget=forms.TextInput(attrs={'placeholder': 'email'}))
#     phone_number = forms.CharField(label="phone number", max_length=15, required=True,widget=forms.TextInput(attrs={'placeholder': 'phone number'}))
#     contact_pref = forms.ChoiceField(choices = contact_choice)
#     description = forms.CharField(widget=forms.Textarea(attrs={"rows":"7",'placeholder':'description'}))