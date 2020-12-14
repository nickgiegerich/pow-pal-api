from django.urls import path
from .views import StationAPIView, StationDetailsAPIView

urlpatterns = [
    path('stations/', StationAPIView.as_view()),
    path('stations/<int:id>/', StationDetailsAPIView.as_view()),
]