from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from .models import Page

# Creo las vistas principales.

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

def pages_home(request):
    return render(request, 'pages/home.html')

def blog_view(request):
    # Aquí puedes obtener los datos de los blogs desde el modelo
    return render(request, 'pages/blogs.html')