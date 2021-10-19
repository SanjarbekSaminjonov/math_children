from django.db import models

# Create your models here.


class SecondTask(models.Model):
    question = models.TextField(verbose_name="Savol matni")
    answer_true = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="To'g'ri javob")
    answer_1 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Qo'shimcha javob")
    answer_2 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Qo'shimcha javob")
    answer_3 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Qo'shimcha javob")

    class Meta:
        verbose_name = "Mantiqiy savol"
        verbose_name_plural = "Mantiqiy savollar"

    def __str__(self) -> str:
        return self.question[:20] + ' . . .'
