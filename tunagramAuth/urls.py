from django.shortcuts import render
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token
from tunagramAuth.views import obtain_jwt_token

# Create your views here.
urlpatterns = [
    path('token', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
]