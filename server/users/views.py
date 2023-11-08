from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Passport, Profile
from .serializers import UserSerializer 


class ProfileView(APIView):
    def profile_exists(self, user_id):
        """Проверка существования профиля пользователя"""
        profile = User.objects.get(id=user_id).profile
        return True if profile else False

    def get(self, request):
        """Получение профиля пользователя, если он существует"""
        user_id = request.user.pk
        user = User.objects.get(id=user_id)
        serialize_data = UserSerializer(user, many=False)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Создание профиля если не существует/редактирование профиля если существует"""
        user_id = request.user.pk
        profile_exists = self.profile_exists(user_id)
        if profile_exists:
            # Редактирование существующего профиля
            return HttpResponse("Профиль существует, тут будет обновление")
        
        # Создание паспорта
        passport = Passport.objects.create(
            numbers = request.data.get("numbers"),
            series = request.data.get("series"),
            registration_place = request.data.get("registration_place"),
            created_at = request.data.get("created_at")
        )
        profile = Profile.objects.create(
            last_name = request.data.get("last_name"),
            first_name = request.data.get("first_name"),
            patronymic = request.data.get("patronymic", ""),
            sex = request.data.get("sex"),
            birth_date = request.data.get("birth_date"),
            phone = request.data.get("phone"),
            adress = request.data.get("adress"),
            passport_id = passport.id,
            image = request.data.get("image")
        )
        user = User.objects.get(id=user_id)
        user.profile_id = profile.id
        user.save()
        serialize_data = UserSerializer(user, many=False)
        return Response(serialize_data.data, status=status.HTTP_201_CREATED)
