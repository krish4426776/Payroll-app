from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser , Bill 


class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES)
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'user_type')

        

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        exclude = ['seller']

class EditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password')