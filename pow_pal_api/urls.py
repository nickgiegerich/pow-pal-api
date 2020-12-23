from django.urls import path
from .views import StationAPIView, StationDetailsAPIView, StateAPIView

urlpatterns = [
    path('states/', StateAPIView.as_view()),
    path('stations/', StationAPIView.as_view()),
    path('stations/<int:id>/', StationDetailsAPIView.as_view()),
]