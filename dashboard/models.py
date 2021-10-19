from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class AllResult(models.Model):

    APP_CHOICES = (
        (1, 'NOSTANDART TOPSHIRIQ'),
        (2, 'MANTIQIY SAVOLLAR'),
        (3, 'KREATIV FIKRLASH'),
    )

    pupil = models.ForeignKey(User, on_delete=CASCADE, verbose_name="O'quvchi")
    type_task = models.IntegerField(
        choices=APP_CHOICES, default=0, verbose_name="Topshiriq turi")
    last_score = models.IntegerField(
        default=0, blank=True, null=True, verbose_name="Oxirgi natija")
    max_score = models.IntegerField(
        default=0, blank=True, null=True, verbose_name="Eng yuqori natija")
    avarage_score = models.IntegerField(
        default=0, blank=True, null=True, verbose_name="O'rtacha natija")
    attempt = models.IntegerField(
        default=0, blank=True, null=True, verbose_name="Urinishlar soni")

    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"

    def add_attempt(self):
        self.avarage_score = round((
            self.avarage_score * self.attempt + self.last_score) / (self.attempt + 1))
        self.attempt += 1

        if self.max_score < self.last_score:
            self.max_score = self.last_score

    def __str__(self) -> str:
        return self.pupil.first_name + ' ' + self.pupil.last_name + 'ning natijasi'
