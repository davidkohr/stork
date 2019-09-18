from django import forms

class NameForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
