from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, signup
from ProyectoFinalValenti.views import home, about
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
