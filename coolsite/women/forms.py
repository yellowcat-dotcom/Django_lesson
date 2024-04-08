from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):

    # создаем конструктор для того, чтобы при невыбранной категории не было "---" а было "Категория не выбрана"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Women  # связь с моделью
        # fields = '__all__'  # показываем все поля
        # рекомендуется вручную прописывать поля!!!
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']

        # описывание стилей форм
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    # создание собственного валидатора формы
    def clean_title(self):
        title = self.cleaned_data['title']  # получаем значение поля по ключу title
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title
