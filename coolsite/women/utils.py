from django.db.models import Count

from women.models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'}
        ]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):  # метод, формирующий нужный контекст по умолчанию
        context = kwargs  # формируем словарь из аргументов, переданных функции
        cats = Category.objects.annotate(Count('women'))  # формируем список категорий

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:  # если пользователь не авторизован
            user_menu.pop(1)  # удаляем {'title': "Добавить статью", 'url_name': 'add_page'},

        context['menu'] = user_menu  # формируем контекст для меню и рубрик

        context['cats'] = cats
        if 'cat_selected' not in context:  # если изначально не присутствовал ключ cat_selected, 0 добавляем
            context['cat_selected'] = 0
        return context
