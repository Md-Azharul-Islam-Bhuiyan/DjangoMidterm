from django.shortcuts import render, redirect
from car.models import CarModel,Purcehase_history
from django.contrib.auth.models import User
from auth_user.forms import RegisterForm, ChangeUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView, View
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class RegestrationView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        messages.success(self.request, 'Account Successfully Created')
        return super().form_valid(form)

# @method_decorator(login_required, name='dispatch')    
class UserLoginView(LoginView):
    template_name='login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

@login_required
def profile(request):
    buyers = Purcehase_history.objects.filter(user = request.user)
    data = CarModel.objects.filter(auth_user = request.user)
    return render(request, 'profile.html', {'data': data,'buyers': buyers})
    

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    form_class = ChangeUserForm
    pk_url_kwarg = 'id'
    template_name = 'updateProfile.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'Logged Out Successfully')
        return redirect('login')     