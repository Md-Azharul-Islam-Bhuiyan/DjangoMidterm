from django import forms
from brand.models import BrandModel


class BrandForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = '__all__'
