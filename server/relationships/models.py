from django.db import models


class RelativeStatus(models.Model):
    status_name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self) -> str:
        return self.status_name

    class Meta:
        verbose_name = "relative status"
        verbose_name_plural = "relative statuses"


class AbstractProfile(models.Model):
    last_name = models.CharField(max_length=25, null=False, blank=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    patronymic = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=15, null=False, blank=False, unique=True)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = "abstract profile"
        verbose_name_plural = "abstract profiles"


class Relatives(models.Model):
    user = models.ForeignKey("users.User", null=False, on_delete=models.CASCADE)
    abstract_profile = models.ForeignKey("relationships.AbstractProfile", null=False, on_delete=models.CASCADE)
    status = models.ForeignKey("relationships.RelativeStatus", null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} - {self.abstract_profile}"

    class Meta:
        verbose_name = "relative"
        verbose_name_plural = "relitives"
