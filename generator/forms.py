from django import forms

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(
        min_value=8,
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    uppercase = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    numbers = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    symbols = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
