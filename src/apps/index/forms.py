from os import urandom

from django import forms


class UpForm(forms.Form):
    city = forms.CharField(max_length=200, min_length=1, required=True)
    date = forms.DateTimeField(input_formats=["%d-%m-%Y %H"])
