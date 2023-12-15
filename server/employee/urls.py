from django.urls import path
from .views import ListOfWeddingsView, WeddingDetailView

urlpatterns = [
    path('weddings/', ListOfWeddingsView.as_view()),
    path('weddings/<int:id>/', WeddingDetailView.as_view()),
]
