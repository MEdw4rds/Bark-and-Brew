from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_time_slot, name='book_time_slot'),
    path('profile/', views.profile, name='profile'),
    path('edit-booking/<int:booking_id>/',
         views.edit_booking, name='edit_booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
]
