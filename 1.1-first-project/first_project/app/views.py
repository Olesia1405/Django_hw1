from datetime import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = f"Текущее время: {datetime.now().time()} <br><a href='{reverse('homepage')}'>На главную</a>"
    return HttpResponse(current_time)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    path = "/home/ideapad5/Нетология. Python-разработчик с нуля. PD-58/Django/1. Знакомство с Django. Подготовка и запуск проекта./Django_Homework1_Introduction"
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))
    all_dir_files = f"Содержимое рабочей директории: {filelist} <br><a href='{reverse('homepage')}'>На главную</a>"

    return HttpResponse(all_dir_files)
