




from django.urls import path
from . import views
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView
)

app_name = 'pages'

urlpatterns = [
    path('', PageListView.as_view(), name='page-list'),
    path('', views.pages_home, name='home'),
    path('<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('create/', PageCreateView.as_view(), name='page-create'),
    path('<int:pk>/update/', PageUpdateView.as_view(), name='page-update'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
    path('blogs/', views.blog_view, name='blogs'),
    
]
