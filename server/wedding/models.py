from django.db import models

class Wedding(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    change_last_name = models.BooleanField(null=False, default=True)
    status = models.ForeignKey('wedding.WeddingStatus', on_delete=models.CASCADE, default=1)
    event_datatime = models.DateTimeField(blank=False, null=False)


class WeddingStatus(models.Model):
    status_name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self) -> str:
        return self.status_name
    
    class Meta:
        verbose_name = "wedding status"
        verbose_name_plural = "wedding statuses"


class Witnesses(models.Model):
    """Таблица для свидетелeй"""
    ...