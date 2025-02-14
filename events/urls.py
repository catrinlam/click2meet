from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView, name='event_list'),
    path('<int:event_id>/', views.EventDetailView, name='event_detail'),
]
