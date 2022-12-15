from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Newsletter
from .forms import NewsletterForm




# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            letter_obj = form.save(commit=False)
            letter_obj.isSubscribed = True
            letter_obj.save()
            messages.success(request, "you are subscribed to our mailing list")
            form = NewsletterForm()
        else:
            messages.warning(request, "failed to add to our mailing list !!!")
    else:
        form = NewsletterForm(request.POST)
        messages.warning(request, "failed to add to our mailing list !!!")
    return  redirect('mainapp:mainapp-home')


#post method , email & trackingid
def unsubsribe(request):
    if 'email' in request.GET and 'tracking_id' in request.GET:
        email = request.GET.get('email');
        tracking_id = request.GET.get('tracking_id')
        letter_obj = Newsletter.objects.filter(email=email,tracking_id=tracking_id)
        if letter_obj is not None:
            letter_obj = letter_obj[0]
            letter_obj.isSubscribed = False
            letter_obj.save()
            messages.success(request, "you opt out from our mailing list")
        else:
            messages.info(request, "something went wrong")
    return redirect('mainapp:mainapp-home')

    
    
    

