from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from car.models import CarModel, Comment, Purcehase_history
from car.forms import CarForm, CommentForm
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AddCarView(CreateView):
    model = CarModel
    form_class = CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car')

    def form_valid(self, form):
        form.instance.auth_user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Car'
        return context

@method_decorator(login_required, name='dispatch')
class EditCarView(UpdateView):
    model = CarModel
    form_class = CarForm
    pk_url_kwarg = 'id'
    template_name = 'add_car.html'
    success_url = reverse_lazy('add_car')
    
    def form_valid(self, form):
        messages.success(self.request, 'Car Post Successfully Updated')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit Car'
        return context
    
@method_decorator(login_required, name='dispatch')
class DeleteCarView(DeleteView):
    model = CarModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


class DetailCarview(DetailView):
    model = CarModel
    pk_url_kwarg= 'id'
    template_name = 'details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object # post model er object ekhane store korlam
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def buyNow(request, id):
    # car = get_object_or_404(CarModel, id=id)
    car = CarModel.objects.get(id=id)
    # print(car.quantity)
    if car.quantity> 0:
        car.quantity-=1
        car.save()
        Purcehase_history.objects.create(user=request.user, car=car)
    return redirect('profile')
        

