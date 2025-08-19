from django.contrib import admin
from tasks.models import Category, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'completed', 'created_at')
    list_filter = ('completed', 'category')
    search_fields = ('title', 'description')
