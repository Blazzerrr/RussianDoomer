from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('randomMusic', views.randomMusic, name='randomMusic'),
    path('sendMessage', views.sendMessage, name='sendMessage'),
    path('messages.json', views.messages, name='messages'),
    path('donations.json', views.donations, name='donations'),
]
