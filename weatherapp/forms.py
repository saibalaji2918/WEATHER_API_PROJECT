from django import forms

from weatherapp.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}