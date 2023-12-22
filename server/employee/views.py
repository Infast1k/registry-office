from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from wedding.models import Wedding, WeddingStatus
from wedding.serializers import WeddingSerializer
from users.models import User
from django.db.models import Q

class ListOfWeddingsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Берем из бд пользователя который сделал запрос.
        user = User.objects.get(id=request.user.id) 
        # Проверяем роль пользователя.
        if str(user.role) == "user":
            # Если он не работник/админ, возвращаем сообщение с ошибкой доступа.
            return Response({"error": "Пользователь не имеет доступа к данному функционалу!"}, status=status.HTTP_403_FORBIDDEN)
        # Берем все из таблицы с договорами записи кроме "в браке" и "в разводе" 
        weddings = Wedding.objects.exclude(Q(status=2) | Q(status=3))
        # Преобразуем python-dict данные в json формат
        weddings_clear = WeddingSerializer(weddings, many=True)
        # Возращаем данные + статус код 200 OK
        return Response(weddings_clear.data, status=status.HTTP_200_OK)


class WeddingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        # Берем из бд пользователя который сделал запрос.
        user = User.objects.get(id=request.user.id) 
        # Проверяем роль пользователя.
        if str(user.role) == "user":
            # Если он не работник/админ, возвращаем сообщение с ошибкой доступа.
            return Response({"error": "Пользователь не имеет доступа к данному функционалу!"}, status=status.HTTP_403_FORBIDDEN)
        try:
            # Берем запись по id (который отправлен с фронта)
            wedding = Wedding.objects.get(id=id)
            # Берем новый статус из запроса
            req_status = request.data.get("status")
            # ищем instance статуса и берем её (если есть, если нет, то возвращаем ошибку)
            new_status = WeddingStatus.objects.get(status_name=req_status)
            # Изменяем статус этой записи
            wedding.status = new_status
            # Сохраняем её
            wedding.save()
            # Преобразуем python-dict формат в json формат
            wedding_clear = WeddingSerializer(wedding, many=False)
            # Возвращаем обновленную запись + статус код 200 OK
            return Response(wedding_clear.data, status=status.HTTP_200_OK)
        # Если записи с таким id не существует
        except Wedding.DoesNotExist:
            # Возвращаем сообщение с ошибкой
            return Response({"error": f"Запись с id {id} не найдена"}, status=status.HTTP_400_BAD_REQUEST)
        # Если такого статуса не существет
        except WeddingStatus.DoesNotExist:
            # Возвращаем сообщение с ошибкой 
            status_name = request.data.get("status")
            return Response({"error": f"Статуса '{status_name}' не существует!"}, status=status.HTTP_400_BAD_REQUEST)
