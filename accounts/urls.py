from django.http import request
from django.urls import path
from . import views

urlpatterns = [
    path('', views.default),
    path('signup', views.signup),
    path('login', views.login),
    path('logout', views.logout),
]
