from django import forms
from .models import Student

class Studentregistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets={
            'password' : forms.PasswordInput(),
        }
