from django.db import models

class Wedding(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    change_last_name = models.BooleanField(null=False, default=True)
    status = models.ForeignKey('wedding.WeddingStatus', on_delete=models.CASCADE, default=1)
    event_datetime = models.DateTimeField(blank=False, null=False)

    def __str__(self) -> str:
        user = self.user.profile
        profile = self.profile
        return f"{user.last_name, user.first_name, user.patronymic} - {profile.last_name, profile.first_name, profile.patronymic}"
    
    class Meta:
        verbose_name = "wedding"
        verbose_name_plural = "weddings"
        unique_together = ["user", "profile"]


class WeddingStatus(models.Model):
    status_name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self) -> str:
        return self.status_name
    
    class Meta:
        verbose_name = "wedding status"
        verbose_name_plural = "wedding statuses"


class Witnesses(models.Model):
    """Таблица для свидетелeй"""
    wedding = models.ForeignKey('wedding.Wedding', on_delete=models.CASCADE)
    witness = models.ForeignKey('relationships.AbstractProfile', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.wedding.id}. {self.witness.last_name} {self.witness.first_name} {self.witness.patronymic}"

    class Meta:
        unique_together = ['wedding', 'witness']
        verbose_name = "witness"
        verbose_name_plural = "witnesses"


class Child(models.Model):
    """Таблица детей"""
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    patronymic = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=25, null=False)
    birth_date = models.DateField(null=False)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        unique_together = ["last_name", "first_name", "patronymic", "birth_date"]
        verbose_name = "Child"


class ChildStatus(models.Model):
    """Статус ребенка"""
    status_name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self) -> str:
        return self.status_name
    
    class Meta:
        verbose_name = "child status"
        verbose_name_plural = "child statuses"


class BirthSertificate(models.Model):
    """Свидетельства о рождении пользователей"""
    place_of_birth = models.CharField(max_length=100, null=False)
    vital_record = models.PositiveIntegerField(unique=True)

    def __str__(self) -> str:
        return f"{self.vital_record}"

    class Meta:
        verbose_name = 'birth sertificate'
        verbose_name_plural = 'birth sertificates'


class Children(models.Model):
    """Таблица детей (many to many таблица wedding + child)"""
    child = models.ForeignKey('wedding.Child', on_delete=models.CASCADE, null=False)
    wedding = models.ForeignKey('wedding.Wedding', on_delete=models.CASCADE, null=False)
    birth_sertificate = models.ForeignKey('wedding.BirthSertificate', on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=100, null=False)
    status = models.ForeignKey('wedding.ChildStatus', on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return f"{self.child.last_name} {self.child.first_name} - {self.wedding.user.last_name} {self.wedding.user.first_name}"

    class Meta:
        verbose_name = "children"
        unique_together = ["child", "wedding", "birth_sertificate", "status"]