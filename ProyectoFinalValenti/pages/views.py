from django.views.generic import ListView, DetailView
from .models import Page

# Creo las vistas principales.

class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'pages'

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
