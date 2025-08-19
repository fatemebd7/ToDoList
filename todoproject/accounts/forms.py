from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500",
            "placeholder": "********"
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500",
            "placeholder": "********"
        }),
        label="Repeat password"
    )

    class Meta:
        model = User
        fields = ["username", "password", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500",
                "placeholder": "Username"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password2"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-3 py-2 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500",
            "placeholder": "Username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500",
            "placeholder": "********"
        })
    )
