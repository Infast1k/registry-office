from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.models import User, Role
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
            return Response({"error": "Пользователь не имеет доступа к данному функционалу!"},
                            status=status.HTTP_403_FORBIDDEN)
        
        users = User.objects.all()
        users_clear = UserSerializer(users, many=True)
        return Response(users_clear.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request, id):
        """Метод обновляет роль пользователя"""
        # Берем текущего пользователя
        admin = User.objects.get(id=request.user.id) 
        # Проверяем роль пользователя.
        if str(admin.role) == "user" or str(admin.role) == "employee":
            # Если он не админ, возвращаем сообщение с ошибкой доступа.
            return Response({"error": "Пользователь не имеет доступа к данному функционалу!"},
                            status=status.HTTP_403_FORBIDDEN)
        
        try:
            user = User.objects.get(id=id)
            role = Role.objects.get(role_name=request.data.get("role"))
            user.role = role
            user.save()
            user_clear = UserSerializer(user, many=False)
            return Response(user_clear.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": f"пользователя с id {id} не существует!"},
                            status=status.HTTP_400_BAD_REQUEST)
        except Role.DoesNotExist:
            return Response({"error": f"роли {request.data.get("role")} не существует!"},
                            status=status.HTTP_400_BAD_REQUEST) 
