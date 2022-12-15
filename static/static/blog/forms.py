from django import forms


class BlogSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'search blog'
