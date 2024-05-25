from django import forms
from .models import Subscription

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs.update({'class': 'form-control w-50', 'placeholder': 'Enter your email',  
        'style':'background-color: #2b010170; border: 1px solid gold; color: #F0CA69; margin: 0 auto; '})
