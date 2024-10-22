from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = False
        for form in self.forms:
            # В form.cleaned_data будет находиться словарь с данными
            # каждой отдельной формы, которые можно проверить
            if form.cleaned_data.get('is_main'):
                if is_main:
                    raise ValidationError('Уже существует is_main')
                else:
                    is_main = True
            '''вызовом исключения ValidationError можно указать админ панели наличие ошибки
            таким образом объект не будет сохранен,
            пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Здесь перманентная ошибка')'''
        if not is_main:
            raise ValidationError('Нет is_main')

        return super().clean()  # вызов базового кода переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass