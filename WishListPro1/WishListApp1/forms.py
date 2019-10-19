#WishListFrom
from  django import forms
class WishListFrom(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name here'
            }
        )
    )
    year = range(2019, 2025)

    wishDatetobuy= forms.DateField(
        widget=forms.SelectDateWidget(years=year))

    wishobj = forms.CharField(
        label="Enter your WishList",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your WishList here'
            }
        )
    )
class WishListDelForm(forms.Form):
    name=forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Wisher Name'
            }
        )
    )