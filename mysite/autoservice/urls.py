from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name='automobilis'),
    path('paslaugos/', views.paslaugos, name='paslaugos'),
    path('uzsakymai/', views.UzsakymasListView.as_view(), name='uzsakymai'),
    path('uzsakymai/<int:pk>', views.UzsakymasDetailView.as_view(), name='uzsakymas-detail'),
    path('search/', views.search, name='search_link'),
    path('myorders/', views.OrdersByUserListView.as_view(), name='my-orders')
]
