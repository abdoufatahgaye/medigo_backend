# prescription_api/urls.py

from django.urls import path
from .views import OrdonnanceUploadAPIView, OrdonnanceDetailAPIView

urlpatterns = [
    path('upload/', OrdonnanceUploadAPIView.as_view(), name='ordonnance_upload'),
    path('<int:pk>/', OrdonnanceDetailAPIView.as_view(), name='ordonnance_detail'),
]