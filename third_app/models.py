from django.db import models

# Create your models here.


class ThirdTask(models.Model):

    question = models.TextField(verbose_name="Savol matni")
    question_answer = models.IntegerField(
        blank=True, null=True, verbose_name="To'g'ri javob")
    question_image = models.ImageField(verbose_name="Savol uchun rasm")

    class Meta:
        verbose_name = "Kreativ savol"
        verbose_name_plural = "Kreativ savollar"

    def __str__(self) -> str:
        return self.question[:40] + ' . . .'
