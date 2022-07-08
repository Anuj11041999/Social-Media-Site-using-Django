from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='basic_app'

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name = 'basic_app/login.html'), 
        name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.Signup.as_view(), name="signup"),
]