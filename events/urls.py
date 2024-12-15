from django.urls import path
from .views import (
    EventListCreateAPIView, 
    EventDetailAPIView,
    EventJoinAPIView,
)

urlpatterns = [
    path('', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('<int:pk>/join/', EventJoinAPIView.as_view(), name='event-join'),
]
