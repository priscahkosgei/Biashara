from django import forms
from BiasharaApp.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields =['name','price','description']