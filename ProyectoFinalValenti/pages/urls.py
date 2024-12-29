from django.urls import path
from . import views
from .views import PageListView, PageDetailView

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('', PageListView.as_view(), name='page-list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    
]
