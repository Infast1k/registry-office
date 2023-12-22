from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import Q
from wedding.exceptions import SameSexException

from wedding.serializers import WeddingSerializer
from .serializers import ChildrenSerializer, WitnessSerializer
from .models import Wedding, Witnesses, Children, Child, BirthSertificate, ChildStatus
from users.models import Profile, Passport, User
from relationships.models import AbstractProfile


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
            return Response({"error": "Невозможно создать договор, данный пользователь уже состоит в браке!"},
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


class WitnessesView(APIView):
    def get(self, request, id):
        """Метод для получения списка свидетелей к определенной свадьбе (по id)"""
        try:
            wedding = Wedding.objects.get(id=id)
            witnesses = Witnesses.objects.filter(wedding=wedding)
            witnesses_clear = WitnessSerializer(witnesses, many=True)
            return Response(witnesses_clear.data, status=status.HTTP_200_OK)
        except Wedding.DoesNotExist:
            return Response({"error": f"Свадьбы с id {id} не существует!"})
        
    def delete(self, request, id):
        """Метод для удаления свидетeля"""
        try:
            witness = Witnesses.objects.get(id=id)
            witness.delete()
            return Response({"message": "свидетель успешно удален!"}, status=status.HTTP_200_OK)
        except Witnesses.DoesNotExist:
            return Response({"error": f"Свидетеля с id {id} не существует!"},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id):
        """Метод для добавления свидетелей к определенной свадьбе (по id)"""
        try:
            # Получаем свадьбу по id
            wedding = Wedding.objects.get(id=id)
            # Ищем абстрактный профиль по номеру телефона
            abstract_profile = AbstractProfile.objects.get(phone=request.data.get("phone"))
        # Если профиля с таким телефоном нет
        except AbstractProfile.DoesNotExist:
            # Создаем его
            abstract_profile = AbstractProfile.objects.create(
                last_name = request.data.get("last_name"),
                first_name = request.data.get("first_name"),
                patronymic = request.data.get("patronymic"),
                phone = request.data.get("phone"),
                birth_date = request.data.get("birth_date"),
                address = request.data.get("address")
            )
        # Если свадьбы с таким id не сущесвтует
        except Wedding.DoesNotExist:
            # Возвращаем информативное сообщение + статус 400 bad request
            return Response({"error": f"Свадьбы с id {id} не существует!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # Создаем запись в таблицу со свидетелями
            witness = Witnesses.objects.create(
                wedding = wedding,
                witness = abstract_profile
            ) 
            # Преобразуем данные из Python-dict в json
            witness_clear = WitnessSerializer(witness, many=False)
            # Возвращаем созданную запись + статус 200 ok
            return Response(witness_clear.data, status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response({"error": "Данный человек уже является свидетелем для данной свадьбы"},
                            status=status.HTTP_400_BAD_REQUEST)


class ChildrenView(APIView):
    def get(self, request, id):
        """Метод для получения списка всех детей свадьбы по id"""
        try:
            wedding = Wedding.objects.get(id=id)
            children = Children.objects.filter(wedding=wedding)
            children_clear = ChildrenSerializer(children, many=True)
            return Response(children_clear.data, status=status.HTTP_200_OK)
        except Wedding.DoesNotExist:
            return Response({"error": f"Свадьбы с id {id} не существует!"}, 
                            status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, requset, id):
        """Метод для добавления ребенка по id свадьбы"""
        try:
            wedding = Wedding.objects.get(id=id)
            child = Child.objects.get(
                last_name=requset.data.get("last_name"),
                first_name=requset.data.get("first_name"),
                patronymic=requset.data.get("patronymic"),
                sex=requset.data.get("sex"),
                birth_date=requset.data.get("birth_date")
            )    
        except Child.DoesNotExist:
            child = Child.objects.create(
                last_name=requset.data.get("last_name"),
                first_name=requset.data.get("first_name"),
                patronymic=requset.data.get("patronymic"),
                sex=requset.data.get("sex"),
                birth_date=requset.data.get("birth_date")
            )
        except Wedding.DoesNotExist:
            return Response({"error": f"Свадьбы с id {id} не существует!"})
        
        try:
            birth_sertificate = BirthSertificate.objects.get(
                place_of_birth = requset.data.get("place_of_birth"),
                vital_record = requset.data.get("vital_record")
            )
        except BirthSertificate.DoesNotExist:
            birth_sertificate = BirthSertificate.objects.create(
                place_of_birth = requset.data.get("place_of_birth"),
                vital_record = requset.data.get("vital_record")
            )
        
        status_name = ChildStatus.objects.get(status_name = requset.data.get("status"))
        Children.objects.create(
            child=child,
            wedding=wedding,
            birth_sertificate=birth_sertificate,
            address=requset.data.get("address"),
            status=status_name
        )
        return Response({"message": "Ребенок успешно добавлен!"}, status=status.HTTP_200_OK)
        

    def delete(self, request, id):
        """Метод для удаления записи из таблицы children по id"""
        try:
            child = Children.objects.get(id=id)
            child.delete()
            return Response({"message": f"Запись с id {id} успешно удалена!"})
        except Children.DoesNotExist:
            return Response({"error": f"Записи с id {id} не существует!"})


class ChildDetail(APIView):
    def get(self, request, id):
        """Получение ребенка по его id"""
        try:
            child = Children.objects.get(id=id)
            child_clear = ChildrenSerializer(child, many=False)
            return Response(child_clear.data, status=status.HTTP_200_OK)
        except Children.DoesNotExist:
            return Response({"error": f"Ребенка с id {id} не существет!"})