from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
 


class ProfileView(APIView):
    def profile_exists(self, id: int) -> bool:
        profile = Profile.objects.filter(account=id)
        return True if profile else False

    def get(self, request):
        # Получение своего профиля
        user_id = request.user.pk
        profile_exists = self.profile_exists(user_id)
        if profile_exists:
            profile = Profile.objects.filter(account=user_id)
            return HttpResponse(profile)
        return HttpResponse("Профиль не существует")
