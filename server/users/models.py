from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    """Менеджер создания кастомных пользователей"""
    def _get_email(self, email: str):
        return self.normalize_email(email)
 
    def _create_user(
        self, 
        email: str, 
        password: str,
        commit: bool,
        is_staff: bool = False, 
        is_superuser: bool = False
    ):
         
        email = self._get_email(email)
         
        user = User(email=email, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
         
        if commit:
            user.save()
             
        return user
 
    def create_superuser(self, email: str, password: str, commit: bool = True):
        return self._create_user(email, password, is_staff=True, is_superuser=True, commit=commit)
 
    def create_user(self, email: str, password: str, commit: bool = True):
        return self._create_user(email, password, commit=commit)


class User(AbstractUser):
    "Auth-данный пользователей"
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    profile = models.OneToOneField(
        'users.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    role = models.ForeignKey(
        'users.Role',
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        default=1
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Role(models.Model):
    """Роли пользователей"""
    role_name = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.role_name
    
    class Meta:
        verbose_name = 'role'
        verbose_name_plural = 'roles'


class Profile(models.Model):
    """Профили пользователей"""
    last_name = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=20, null=False)
    patronymic = models.CharField(max_length=20, null=True)
    sex = models.CharField(max_length=10, null=False)
    birth_date = models.DateField(null=False)
    phone = models.CharField(max_length=20, null=False, unique=True)
    # TODO: Сделать таблицу паспорт и свидетельство о рождении + связи
    # pasport
    # birth_sertificate
    adress = models.CharField(max_length=100, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # Image

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
