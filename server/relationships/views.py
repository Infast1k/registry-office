from django.http import HttpResponse
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
        # Получаем id текущего пользователя т.к.
        # Родственника мы сохраняем только для него.
        user_id = request.user.pk
        # Получаем пользователя по id т.к. иначе не работает (не понял сам почему)
        user = User.objects.get(id=user_id)
        # Создание обстрактного пользователя
        # Он содержит меньше данных чем обычный профиль
        # т.к. для родственников нам много не надо.
        profile = AbstractProfile.objects.create(
            # request.data имеет структуру типа словаря, поэтому мы можем использовать
            # метод get, который берет значение по ключу (первый аргумент),
            # если такого ключа нет, то возвращает значение по умолчанию (второй аргумент).
            # В нашем случае мы его не пишем, т.к. в моделях мы указали,
            # что все поля имеют ограничение blank=False.
            # Это означает, что поле обязательно при отправке запроса.
            last_name = request.data.get("last_name"),
            first_name = request.data.get("first_name"),
            patronymic = request.data.get("patronymic"),
            phone = request.data.get("phone"),
            birth_date = request.data.get("birth_date"),
            address = request.data.get("address")
        )
        # Получаем значение поля status_name из запроса.
        status_name = request.data.get("status_name")
        # Получаем статус по его имени.
        # метод get возвращает первое совпадение, он нам подходит т.к.
        # поле status_name имеет ограничение unique=True.
        relative_status = RelativeStatus.objects.get(status_name=status_name)
        # Создание записи о родственнике
        Relatives.objects.create(
            user = user,
            abstract_profile = profile,
            status = relative_status
        )
        # Возврат сообщения об успешном сохранении записи о родственнике.
        # Ошибки не может быть т.к. с клиентской стороны будет проходить валидация данных,
        # если данные не валидны, то он просто не сможет попасть в этот метод.
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
        return Response({"message": f"запись с id {id} не существует"}, status=status.HTTP_400_BAD_REQUEST)
