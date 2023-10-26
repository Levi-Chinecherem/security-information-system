from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import SecurityIncident, SecurityGroup

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class SecurityIncidentForm(forms.ModelForm):
    class Meta:
        model = SecurityIncident
        fields = ['title', 'description', 'location', 'involved_parties']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Incident Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Incident Description'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Incident Location'}),
            'involved_parties': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

class SecurityGroupForm(forms.ModelForm):
    class Meta:
        model = SecurityGroup
        fields = ['name', 'description', 'members']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Group Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Group Description'}),
            'members': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
