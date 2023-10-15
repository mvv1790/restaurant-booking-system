from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tables, name='list_tables'),
    path('home/', views.home, name='home'),
    path('book/', views.book_table, name='book_table'),
    path('menu/<int:table_id>/', views.view_menu, name='menu'),
    path('general_menu/', views.general_menu, name='general_menu'),
]
