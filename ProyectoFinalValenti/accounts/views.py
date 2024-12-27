from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Implemento vistas de inicio de sesion y registro:

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

def signup(request):
    return render(request, 'accounts/signup.html')

