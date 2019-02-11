from django import forms

from .models import Category, Product


class CategoryForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'model-form'
            }
        )
    )

    description = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'model-form'
            }
        )
    )


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
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


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'description', 'cost']
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
