from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
# class RegisterUserForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#     first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
#     last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name','email', 'password1','password2']

#     def __init__(self, *args, **kwargs) :
#         super(RegisterUserForm,self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['class'] = 'forform-control'
#         self.fields['password1'].widget.attrs['class'] = 'forform-control'
#         self.fields['password2'].widget.attrs['class'] = 'forform-control'




class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
