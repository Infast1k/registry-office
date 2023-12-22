from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Passport, Profile
from .serializers import UserSerializer 
from django.db import IntegrityError


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
        """Создание профиля"""
        user_id = request.user.pk
        user = User.objects.get(id=user_id)

        try:
            # Создание нового профиля
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
                address = request.data.get("address"),
                passport_id = passport.id,
                image = request.data.get("image")
            )
            user.profile = profile
            user.save()
            serialize_data = UserSerializer(user, many=False)
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
             return Response({"error": "Профиль с такими данными уже сущестует!"}, status=status.HTTP_400_BAD_REQUEST)
        

    # def put(self, request):
            # Редактирование пасспорта
            # passport = Passport.objects.get(id=user.profile.passport.id)
            # passport.numbers = request.data.get("numbers", passport.numbers)
            # passport.series = request.data.get("series", passport.series)
            # passport.registration_place = request.data.get("registration_place", passport.registration_place)
            # passport.created_at = request.data.get("created_at", passport.created_at)
            # passport.save()

            # # Редактирование профиля
            # profile = Profile.objects.get(id=user.profile.id)
            # profile.last_name = request.data.get("last_name", profile.last_name)
            # profile.first_name = request.data.get("first_name", profile.first_name)
            # profile.patronymic = request.data.get("patronymic", profile.patronymic)
            # profile.sex = request.data.get("sex", profile.sex)
            # profile.birth_date = request.data.get("birth_date", profile.birth_date)
            # profile.phone = request.data.get("phone", profile.phone)
            # profile.address = request.data.get("address", profile.address)
            # profile.image = request.data.get("image", profile.image)
            # profile.save()
            # return Response({"message": "данные были обновлены"}, status=status.HTTP_202_ACCEPTED)