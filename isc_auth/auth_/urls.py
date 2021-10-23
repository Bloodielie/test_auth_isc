from django.contrib.auth import views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]
