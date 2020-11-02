from django import forms


class UrlForm(forms.Form):
    url = forms.URLField()

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    email = forms.EmailField()