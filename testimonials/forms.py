from django import forms
from .models import Testimonial
from products.widgets import CustomClearableFileInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = [
            'rating',
            'body',
            'service',
        ]
        widgets = {
            'rating': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('rating', css_class='star-rating'),
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-gold'
