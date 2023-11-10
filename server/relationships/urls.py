from django.urls import path
from .views import RelativesView

urlpatterns = [
    path('relatives/', RelativesView.as_view())
]
