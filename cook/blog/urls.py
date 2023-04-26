from django.urls import path
from .views import *


urlpatterns = [
    path('<slug:slug>/', post_list, name='post_list'),
    path('', home, name='home'),
    
]