from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('send/', views.send_message, name='send_message'),
]
