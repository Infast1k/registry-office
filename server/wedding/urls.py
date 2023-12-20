from django.urls import path
from .views import (
    WeddingListView,
    CurrentUserWeddingView,
    WeddingDetailView,
    WitnessesView,
    ChildrenView,
    ChildDetail
    )

urlpatterns = [
    path("weddings/", WeddingListView.as_view()),
    path("my-weddings/", CurrentUserWeddingView.as_view()),
    path("weddings/<int:id>/", WeddingDetailView.as_view()),
    path("weddings/witnesses/<int:id>/", WitnessesView.as_view()),
    path("weddings/children/<int:id>/", ChildrenView.as_view()),
    path("wedding/child/<int:id>/", ChildDetail.as_view()),
]
