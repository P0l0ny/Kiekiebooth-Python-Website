from django.urls import path
from . import views

#url specifications with names to refer to in base template
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]