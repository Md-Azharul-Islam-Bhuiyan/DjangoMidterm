from django.shortcuts import render, redirect
from car.models import CarModel
from brand.models import BrandModel

def home(request, brand_slug=None):
    data  = CarModel.objects.all()
    brands = BrandModel.objects.all()
    
    if brand_slug is not None:
        brand = BrandModel.objects.get(slug = brand_slug)
        data = CarModel.objects.filter(brand = brand)
    
    return render(request, 'home.html', {'data': data, 'brands': brands})