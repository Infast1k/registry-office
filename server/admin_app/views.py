from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializers import UserSerializer


class UsersView(APIView):
    # Доступ только авторизированным пользователям
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        """Метод возвращает список всех пользователей"""
        # Берем текущего пользователя
        user = User.objects.get(id=request.user.id) 
        # Проверяем роль пользователя.
        if str(user.role) == "user" or str(user.role) == "employee":
            # Если он не админ, возвращаем сообщение с ошибкой доступа.
            return Response({"error": "Пользователь не имеет доступа к данному функционалу!"}, status=status.HTTP_403_FORBIDDEN)
        
        users = User.objects.all()
        users_clear = UserSerializer(users, many=True)
        return Response(users_clear.data, status=status.HTTP_200_OK)