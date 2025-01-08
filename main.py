# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




#_________________________________________________________________________________________________

### - 08.01.25

### - 1) установка Django: - (.venv) D:\Rabota_12_24\Django_PostgreSQL_01_25 git:[main
#                                                            >>> pip install django
### - 2) Создание проекта: - (.venv) D:\Rabota_12_24\Django_PostgreSQL_01_25 git:[main
#                                                            >>> django-admin startproject Project_django_postge .
#                          - в конце проекта, через пробел поставить (.) , РАБОТАЕТ
### - 3) Создаем папку templates
### - 4) Создаем приложение App_django
#                                                            >>> python manage.py startapp App_django_postge

### - 5) Переход в директорию проекта:
#                                                            >>> cd D:\Rabota_12_24\Django_Paginator_01_25

### - 6) Создание файла зависимостей:
#            (.venv) D:\Rabota_12_24\Django_PostgreSQL_01_25 git:[main] >>> pip freeze > requirements.txt
#     6.a) вывод зависимостей в консоль:
#                                                                       >>> pip freeze

### - 7) В файле settings.py:
#             в строке TEMPLATES = [] дополняем значение 'DIRS': [] == 'DIRS': [BASE_DIR / "templates"],
#             в строке INSTALLED_APPS = [] в конце дописываем имя нашего приложения 'App_django_postge'

### - 8) создали модель в models.py class User(models.Model):

### - 9) Дополнение файла admin.py:
#                                   from django.contrib import admin
 #                                  from .models import *
  #                                 admin.site.register(User)


### - 10) Миграции не были выполнены: Возможно, Вы не применили миграции для Вашего приложения. Убедитесь,
# что Вы выполнили команды:
#                                          >>> python manage.py makemigrations    ### - Создаем миграцию
#                                          >>> python manage.py migrate           ### - Применяем миграцию




















### - 10) Создадим суперпользователя, который имеет доступ ко всем административным функциям нашего приложения:
#                                           >>> python manage.py createsuperuser / если не создан
                                # python manage.py createsuperuser
                                # Username (leave blank to use 'firebat'): testPavel
                                # Email address:
                                # Password:
                                # Password (again):
                                # This password is too common.
                                # This password is entirely numeric.
                                # Bypass password validation and create user anyway? [y/N]: y
                                # Superuser created successfully.

### - 11) Регистрируем модель в файле admin.py
#                               admin.site.register(Post)      ### - не консоль

### - 12) ЗАПУСK серверa разработки:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py runserver
# 10.44

