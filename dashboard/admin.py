from django.contrib import admin
from .models import AllResult

# Register your models here.

@admin.register(AllResult)
class AllResultAdmin(admin.ModelAdmin):
    list_display = (
        'pupil',
        'type_task',
        'last_score',
        'max_score',
        'avarage_score',
        'attempt',
    )
