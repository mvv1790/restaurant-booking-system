from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tables, name='list_tables'),
    path('home/', views.home, name='home'),
    path('book/', views.book_table, name='book_table'),
    path('menu/', views.view_menu, name='menu'),
]

