from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home', index, name='index'),
    path('booking_list/', booking_list, name='booking_list'),
    path('booking_details/<int:booking_id>/', booking_details, name='booking_details'),
    path('booking_create/', booking_create, name='booking_create'),
    path('booking_delete/<int:booking_id>/', booking_delete, name='booking_delete'),
    path('booking_update/<int:booking_id>/', booking_update, name='booking_update'),
]