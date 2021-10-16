from django.contrib import admin
from .models import FirstTask

# Register your models here.

@admin.register(FirstTask)
class FirstTaskAdmin(admin.ModelAdmin):
    list_display = (
        'question', 'question_answer',
    )
