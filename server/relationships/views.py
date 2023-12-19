from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Relatives, AbstractProfile, RelativeStatus
from users.models import User
from .serializers import AbstractUserSerializer, RelativeSerializer


class RelativesView(APIView):
    def get(self, request):
        """Метод для получения всех родственников текущего пользователя"""
        # Получение id текущего пользователя
        user_id = request.user.pk
        # Получение всех родственников текущего пользователя
        relatives = Relatives.objects.filter(user=user_id)
        # Преобразование данных QuerySet -> JSON
        serialize_data = RelativeSerializer(relatives, many=True)
        # Возвращаем чистые данные (чистые = JSON)
        return Response(serialize_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Метод для добавления родственника текущему пользователю"""
        try:
            user_id = request.user.pk
            user = User.objects.get(id=user_id)
            relative_status = RelativeStatus.objects.get(status_name=request.data.get("status_name"))
            profile = AbstractProfile.objects.get(phone=request.data.get("phone"))
        except RelativeStatus.DoesNotExist:
            return Response({"message": f"Статуса {request.data.get("status_name")} не сущестует"},
                            status=status.HTTP_400_BAD_REQUEST)
        except AbstractProfile.DoesNotExist:
            profile = AbstractProfile.objects.create(
                last_name = request.data.get("last_name"),
                first_name = request.data.get("first_name"),
                patronymic = request.data.get("patronymic"),
                phone = request.data.get("phone"),
                birth_date = request.data.get("birth_date"),
                address = request.data.get("address")
            )
        Relatives.objects.create(
            user = user,
            abstract_profile = profile,
            status = relative_status
        )
        return Response({"message": "запись была успешно сохранена"}, status=status.HTTP_201_CREATED)


class RelativeDetailView(APIView):

    def get(self, request, id):
        """Метод для получения записи о родственнике по id"""
        try:
            relateve = AbstractProfile.objects.get(id=id)
            relateve_clear = AbstractUserSerializer(relateve, many=False)
            return Response(relateve_clear.data, status=status.HTTP_200_OK)
        except Relatives.DoesNotExist:
            return Response({"message": f"Профиля с id {id} не существует"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Метод для удаления записи о родственнике текущего пользователя"""
        # Находим нужную запись по id
        relative = Relatives.objects.filter(id=id)
        # Если запись с таким id существует, то заходим в блок if.
        if relative:
            # Удаляем запись
            relative.delete()
            # Возвращаем сообщение об успешном удалении записи + статуст 200_OK
            return Response({"message": "запись была успешно удалена"}, status=status.HTTP_200_OK)
        # Возвращаем сообщение о том, что запись с таким id не существуте + статус 400_BAD_REQUEST
        return Response({"message": f"записи с id {id} не существует"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """Метод для обновления записи о родственнике текущего пользователя"""
        # Находим нужную запись по id
        try:
            relative = AbstractProfile.objects.get(id=id)
            relative.last_name = request.data.get("last_name")
            relative.phone = request.data.get("phone")
            relative.address = request.data.get("address")
            relative.save()
            return Response({"message": "запись была успешно обновлена"}, status=status.HTTP_200_OK)
        except AbstractProfile.DoesNotExist:
            return Response({"message": f"Профиля с id {id} не существует"}, status=status.HTTP_400_BAD_REQUEST)
