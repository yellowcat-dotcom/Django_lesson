from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')  # список видимых полей в админке
    list_display_links = ('id', 'title')  # поля на которые можно кликнуть, чтобы изменить статью
    search_fields = ('title', 'content')  # по каким полям можно совершать поиск
    list_editable = ('is_published',)  # редактируемые поля
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # список видимых полей в админке
    list_display_links = ('id', 'name')  # поля на которые можно кликнуть, чтобы изменить статью
    search_fields = ('name',)  # по каким полям можно совершать поиск
    prepopulated_fields = {'slug': ('name',)}  # автоматическое заполнение на основе поля name


admin.site.register(Women, WomenAdmin)  # При регистрации указываем вспомогательный класс
admin.site.register(Category, CategoryAdmin)
