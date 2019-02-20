from django import forms
from products.models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'image', 'category',
            'description', 'cost'
            ]
        widgets = {
            'name': forms.widgets.TextInput(
                attrs={
                    'class': 'model-form'
                }
            ),

            'description': forms.widgets.Textarea(
                attrs={
                    'class': 'model-form'
                }
            )
        }