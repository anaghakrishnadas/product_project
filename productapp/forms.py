from django import forms
from .models import Product
# create forms-
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name', 'desc','price','img']