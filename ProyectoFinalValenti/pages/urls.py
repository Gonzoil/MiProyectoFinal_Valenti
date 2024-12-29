from django.urls import path
from . import views
from .views import PageListView, PageDetailView

app_name = 'pages'

urlpatterns = [
    path('', views.pages_home, name='home'),
    path('<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('blogs/', views.blog_view, name='blogs'),
    
]
