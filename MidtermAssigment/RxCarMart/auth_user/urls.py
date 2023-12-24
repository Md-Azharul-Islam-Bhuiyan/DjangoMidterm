from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegestrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/<int:id>', views.EditProfileView.as_view(), name='edit_profile'),
    path('profile/edit/change_pass', views.pass_change, name='change_pass')
]
