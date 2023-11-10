from django.urls import path
from .views import RelativesView, RelativeDetailView

urlpatterns = [
    path('relatives/', RelativesView.as_view()),
    path('relatives/<int:id>/', RelativeDetailView.as_view())
]
