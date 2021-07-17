from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'your title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'placeholder': 'description', 'rows': 20, 'cols': 120}))
    price = forms.DecimalField(initial=199.99)
    summary = forms.CharField(label='', widget=forms.TextInput)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFf" in title:
            raise forms.ValidationError("uyumlu değil")
        else:
            return title


class RawProductForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.CharField()
