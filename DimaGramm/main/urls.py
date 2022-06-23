from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('register', user_register, name='register')
]