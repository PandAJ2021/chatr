from django import forms
from .models import User
import re
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError('Both password fields are required.')

        if password1 != password2:
            raise forms.ValidationError('Passwords must match.')
        
        validate_password(password2)

        return password2
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.fullmatch('09\d{9}', phone_number):
            raise forms.ValidationError('Number is not Valid.')
        return phone_number
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'is_active', 'is_admin']
    
    def clean_password(self):
        return self.initial.get('password')
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.fullmatch('09\d{9}', phone_number):
            raise forms.ValidationError('Number is not Valid.')
        return phone_number