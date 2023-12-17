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
