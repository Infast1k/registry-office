from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Relatives, AbstractProfile, RelativeStatus
from users.models import User
from .serializers import RelativeSerializer


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
            relative = Relatives.objects.get(id=id)
            # Находим статус по имени
            status_name = request.data.get("status_name")
            relative_status = RelativeStatus.objects.get(status_name=status_name)
            # Обновляем запись
            # Второй параметр снова упускаем, т.к. с фронта нам будут приходить все поля.
            relative.abstract_profile.last_name = request.data.get("last_name")
            relative.abstract_profile.first_name = request.data.get("first_name")
            relative.abstract_profile.patronymic = request.data.get("patronymic")
            relative.abstract_profile.phone = request.data.get("phone")
            relative.abstract_profile.birth_date = request.data.get("birth_date")
            relative.abstract_profile.address = request.data.get("address")
            relative.status = relative_status
            # Сохраняем обновление абстрактного профиля
            relative.abstract_profile.save()
            # Сохраняем обновление статуса
            relative.save()
            # Возвращаем сообщение о том, что запись успешно обновлена + статус 200_OK
            return Response({"message": "запись была успешно обновлена"}, status=status.HTTP_200_OK)
        except Relatives.DoesNotExist:
            # Возвращаем сообщение о том, что записи с таким id не существет + статус 400_BAD_EEQUEST
            return Response({"message": f"записи с id {id} не существует"}, status=status.HTTP_400_BAD_REQUEST)
        except RelativeStatus.DoesNotExist:
            return Response({"message": f"статуса {request.data.get("status_name")} не существует"},
                            status=status.HTTP_400_BAD_REQUEST)
