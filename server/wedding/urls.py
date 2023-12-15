from django.urls import path
from .views import WeddingListView, CurrentUserWeddingView

urlpatterns = [
    path("weddings/", WeddingListView.as_view()),
    path("my-weddings/", CurrentUserWeddingView.as_view()),
]
