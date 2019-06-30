from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('listings', views.listings, name='listings'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]
