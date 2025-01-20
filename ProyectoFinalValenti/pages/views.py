





from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .models import Page

# Creo las vistas principales.

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'

class PageDetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'content']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page-list')

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'content']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page-list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page-list')

def pages_home(request):
    return render(request, 'pages/home.html')

def blog_view(request):
    # Aquí puedes obtener los datos de los blogs desde el modelo
    return render(request, 'pages/blogs.html')