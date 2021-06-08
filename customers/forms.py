from django import forms


class CustomerForm(forms.Form):
    name = forms.CharField(label="Name", max_length=25)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    email = forms.EmailField(label="Email")
