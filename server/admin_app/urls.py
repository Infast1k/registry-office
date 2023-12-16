from django.urls import path
from .views import UsersView, UserDetailView

urlpatterns = [
    path("users/", UsersView.as_view()),
    path("users/<int:id>/", UserDetailView.as_view()),
]