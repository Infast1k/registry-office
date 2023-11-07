from django.urls import path, include, re_path
from .views import ProfileView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('profile/', ProfileView.as_view()),
]
