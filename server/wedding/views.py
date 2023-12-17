from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import Q
from wedding.exceptions import SameSexException

from wedding.serializers import WeddingSerializer
from .models import Wedding
from users.models import Profile, Passport, User


class WeddingListView(APIView):
    def get(self, request):
        """Метод для получения списка всех заявлений на рассмотрении + одобренных"""
        weddings = Wedding.objects.filter(Q(status=4) | Q(status=1))
        weddings_clear = WeddingSerializer(weddings, many=True)
        return Response(weddings_clear.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Метод для создания заявления для брака"""
        user = User.objects.get(id=request.user.id) 

        married = len(Wedding.objects.filter(Q(user=user) | Q(profile=user.profile), status=2))
        if married == 1:
            return Response({"message": "Невозможно создать договор, данный пользователь уже состоит в браке!"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            passport = Passport.objects.get(
                numbers = request.data.get("numbers"),
                series = request.data.get("series"),
                registration_place = request.data.get("registration_place"),
                created_at = request.data.get("created_at")
            )
        except Passport.DoesNotExist:
            passport = Passport.objects.create(
                numbers = request.data.get("numbers"),
                series = request.data.get("series"),
                registration_place = request.data.get("registration_place"),
                created_at = request.data.get("created_at")
            )

        try:
            if user.profile.sex == request.data.get("sex"):
                raise SameSexException()
            profile = Profile.objects.get(
                last_name=request.data.get("last_name"),
                first_name=request.data.get("first_name"),
                patronymic=request.data.get("patronymic"),
                sex=request.data.get("sex"),
                birth_date=request.data.get("birth_date"),
                phone=request.data.get("phone"),
                passport=passport,
                address=request.data.get("address")
            )
        except SameSexException:
            return Response({"error": "Однополые браки запрещены!"}, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(
                last_name=request.data.get("last_name"),
                first_name=request.data.get("first_name"),
                patronymic=request.data.get("patronymic"),
                sex=request.data.get("sex"),
                birth_date=request.data.get("birth_date"),
                phone=request.data.get("phone"),
                passport=passport,
                address=request.data.get("address")
            )
        
        try:
            wedding = Wedding.objects.create(
                user=user,
                profile=profile,
                change_last_name=request.data.get("change_last_name"),
                event_datetime=request.data.get("event_datetime"),
            )
            wedding_clear = WeddingSerializer(wedding, many=False)
            return Response(wedding_clear.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"error": "договор для данных пользователей уже существует"}, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserWeddingView(APIView):
    def get(self, request):
        """Метод для отображения договоров текущего пользователя"""
        # Берем текущего пользователя
        user = User.objects.get(id=request.user.id)
        # Получаем список договоров (беруться договоры и как создателя, так и profile user)
        weddings = Wedding.objects.filter(Q(user=user) | Q(profile=user.profile))
        # Сериализируем данные
        weddings_clear = WeddingSerializer(weddings, many=True)
        # Возвращаем респонс
        return Response(weddings_clear.data, status=status.HTTP_200_OK)
    
class WeddingDetailView(APIView):
    def get(self, request, id):
        """Метод для отображение договора по id"""
        try:
            wedding = Wedding.objects.get(id=id)
            wedding_clear = WeddingSerializer(wedding, many=False)
            return Response(wedding_clear.data, status=status.HTTP_200_OK)
        except Wedding.DoesNotExist:
            return Response({"error": f"Договора с id {id} не существует!"}, status=status.HTTP_400_BAD_REQUEST)
