from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('paslaugos/', views.paslaugos, name='paslaugos')
]
