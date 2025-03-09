# Тестовое задание fullstack(?) mycego
## Создание приложения для скачивания фалов с Yandex.Disk
[Тестовое задание](https://docs.google.com/document/d/1LPFktOxgFiV1A7KU-mq44FnEt-ykeKK1-4Yv40BsXho/edit?tab=t.0)  
</br>

## Оглавление:
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Описание работы](#описание-работы)
- [Удаление](#удаление)

## Технологии
<details>
  <summary>Подробнее</summary>
    <p><strong>Языки программирования:</strong> python-10</p>
    <p><strong>Фреймворк и модули:</strong> Django-5</p>
    <p><strong>Базы данных и инструменты работы с ними:</strong>SQLite</p>
    <p><strong>Кеш:</strong> Redis, hiredis</p>  
    <p><strong>CI/CD:</strong> Docker Hub, Gunicorn</p>
    <p><strong>Others:</strong> Yandex.Dick REST API</p>
</details>

## Установка и запуск

<details>
  <summary>Локальный запуск</summary>
  
  1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (если запускаете в VScode launch или Docker-compose, в противном случае пишите в settings.py):
    
    git clone https://github.com/s0ull877/mycego-test-assigment.git && \
    cd mycego-test-assigment && \
    cp .env_example .env && \
    nano .env

  2. Создайте venv и скачайте зависимости:

    Windows: python -m venv venv
            venv/Script/activate
    Linux: python3 -m venv venv
          venv/bin/activate
          
    pip install -r requirements.txt
    pip3 install -r requirements.txt


  3. Перейдите в дирректорию app и выполните команды:

    Windows: python manage.py migrate 
    Linux: python3 manage.py migrate 
    
    После чего запустите wsgi сервер
    python manage.py runserver
    python3 manage.py runserver

</details>

---

При первом запуске будет создано виртуальное окружение, скачаны зависимости, применены миграции для корректной работы аутентификации django.
      
URL проекта:

  - `http://127.0.0.1:8000/admin/` - Вход в админку
  - `http://127.0.0.1:8000/accounts/login/` - Авторизация
  - `http://127.0.0.1:8000/accounts/logout/` - Выход из аккаунта
  - `http://127.0.0.1:8000/signup/` - Регистрация
  - `http://127.0.0.1:8000/` - Сам сервис собственно

  - `http://127.0.0.1:8000/list/` - Получение файлов при помощи js fetch
  - `http://127.0.0.1:8000/download/` - Скачивание файла(ов) с помощью js 
   


## Описание работы

На странице http://<hostname>:8000/ неавторизованного пользователя переправит на страницу регистрации
В nav кадждого шаблона присутвует кнопка авторизации/выхода, реализованного встроенной django auth
Регистрация производится самой простой FBV, т.к. встроенная auth не имеет такого функционала
После регистрации пользователя перенаправит на главную страницу с полем ввода ссылки

После корректного ввода страница отобразит все доступные файлы, которые можно скачать нажам на блок <a>
или отметить несколько и скачать zip архивом

Файлы также можно сортировать по изображение/документ/видео



## Удаление
Для удаления проекта выполните следующие действия:

  `cd ../.. && rm -fr mycego-test-assigment && deactivate`

[Оглавление](#оглавление)

## <a id="#автор">Автор</a>
[Radmir Galiullin](https://github.com/s0ull877)
