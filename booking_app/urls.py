from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.list_tables, name='list_tables'),
    path('home/', views.home, name='home'),
    path('book/', views.book_table, name='book_table'),
    path('menu/<int:table_id>/', views.view_menu, name='menu'),
    path('general_menu/', views.general_menu, name='general_menu'),
    path('booking/', views.booking_view, name='booking_view'),
    path('booking/<int:table_id>/', views.booking_view, name='booking_view_with_id'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
