from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_booking, name='user_booking'),
    path('booking_form/<int:event_id>/<int:ticket_type_id>/', views.booking_form, name='booking_form'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
