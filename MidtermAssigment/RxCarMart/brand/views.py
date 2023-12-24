from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from brand.models import BrandModel
from brand.forms import BrandForm
from django.views.generic import CreateView
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class AddBrandView(CreateView):
    model = BrandModel
    form_class = BrandForm
    template_name = 'add_brand.html' 
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Brand successfully added')
        return super().form_valid(form)
