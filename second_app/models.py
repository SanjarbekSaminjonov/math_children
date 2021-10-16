from django.db import models

# Create your models here.


class SecondTask(models.Model):
    question = models.TextField()
    answer_true = models.CharField(max_length=100, blank=True, null=True)
    answer_1 = models.CharField(max_length=100, blank=True, null=True)
    answer_2 = models.CharField(max_length=100, blank=True, null=True)
    answer_3 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.question[:20] + ' . . .'
