from django import forms

class AddProductForm(forms.Form):
    # quantity = forms.IntegerField(min_value=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)