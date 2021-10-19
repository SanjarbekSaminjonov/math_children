from django.contrib import admin
from .models import ThirdTask

# Register your models here.


@admin.register(ThirdTask)
class ThirdTaskAdmin(admin.ModelAdmin):
    list_display = (
        'question', 'question_answer',
    )
