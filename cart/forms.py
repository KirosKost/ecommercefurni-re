from django import forms
from mebel.models import Products

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.CharField(required=False, initial=1, widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    colors = forms.CharField(required=False, initial=False, widget=forms.RadioSelect)
    sizes = forms.CharField(required=False, initial=False, widget=forms.RadioSelect)


class OrderSendForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    mail = forms.CharField(required=False)
