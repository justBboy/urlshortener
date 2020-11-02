from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signUp, name='signup'),
    path('<str:urlid>', views.resolve_url, name='resolve-url'),
]