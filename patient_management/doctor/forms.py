from django import forms
from .models import doctor

class ContactForm(forms.Form):
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = doctor
        fields = ['full_name', 'email']


class areaForm(forms.Form):
    message = forms.CharField()


