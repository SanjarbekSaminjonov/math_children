from django.db import models

# Create your models here.

class FirstTask(models.Model):

    question = models.TextField()
    question_answer = models.IntegerField(blank=True, null=True)
    question_image = models.ImageField()

    def __str__(self) -> str:
        return self.question[:40] + ' . . .'