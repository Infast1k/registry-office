from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
 


class ProfileView(APIView):
    def profile_exists(self, user_id):
        """Проверка существования профиля пользователя"""
        return Profile.objects.filter(account=user_id).exists()

    def get(self, request):
        """Получение профиля пользователя, если он существует"""
        user_id = request.user.pk
        profile_exists = self.profile_exists(user_id)
        if profile_exists:
            profile = Profile.objects.get(account=user_id)
            serialize_data = ProfileSerializer(profile, many=False)
            return Response(serialize_data.data)
        return Response({'message': 'Профиль не найден'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """Создание профиля если не существует/редактирование профиля если существует"""
        return HttpResponse("asdfasdf")
