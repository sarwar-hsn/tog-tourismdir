from django.forms import ModelForm
from .models import Newsletter


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['name'] = 'email'


