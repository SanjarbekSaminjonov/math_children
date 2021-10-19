from django.contrib import admin
from .models import SecondTask

# Register your models here.


@admin.register(SecondTask)
class SecondTaskAdmin(admin.ModelAdmin):
    list_display = (
        'question', 'answer_true',
    )
