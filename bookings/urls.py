from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_booking, name='user_booking'),
    path('create/', views.create_booking, name='create_booking'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]

