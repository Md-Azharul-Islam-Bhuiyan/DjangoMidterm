from django import forms
from car.models import CarModel,Comment



class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        exclude = ['auth_user',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

