from django import forms


class NewDogForm(forms.Form):

    name = forms.CharField(max_length=50)
    owner = forms.CharField(max_length=100, )
    description = forms.CharField(max_length=500, widget=forms.Textarea)
    picture = forms.ImageField()
