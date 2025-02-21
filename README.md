## Проект «API для YaTube»
#### Описание проекта:
Учебный проект по созданию backend-приложения блога с возможностью создания своего личного блога,  
комментрирования постов, группировки постов по тематикам и подписок на авторов постов.   
   
API реализован на Django Rest Framework и осуществляет все необходимые функции приложения.   
Аутентификация осуществляется по JWT-токену.   
   
#### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
  ```
  git clone https://github.com/Iceberen/api_final_yatube.git
  cd yatube_api
  ```
- Cоздать и активировать виртуальное окружение:
  - Windows
    ```
    python -m venv env
    source venv/Scripts/activate
    ```
  - Linux
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
- Установить зависимости из файла requirements.txt:
  - Windows
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
  - Linux
    ```
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
- Выполнить миграции:
  - Windows:
    ```
    python manage.py migrate
    ```
  - Linux:
    ```
    python3 manage.py migrate
    ```
- Запустить проект:
  - Windows:
    ```
    python manage.py runserver
    ```
  - Linux:
    ```
    python3 manage.py runserver
    ```

#### Документация:

После запуска проекта на dev-сервере документация в формате redoc доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```

#### Доступный функционал:
- Получить или создать публикаций:
  ```
  http://127.0.0.1:8000/api/v1/posts/
  ```
- Получить, обновить, частично обновить или удалить публикации по id:
  ```
  http://127.0.0.1:8000/api/v1/posts/{id}/
  ```
- Получить или добавить новый комментарий:
  ```
  http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
  ```
- Получить, обновить, частично обновить или удалить комментарий к публикации по id:
  ```
  http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
  ```
- Получить список сообществ:
  ```
  http://127.0.0.1:8000/api/v1/groups/
  ```
- Получить информацию о сообществе по id:
  ```
  http://127.0.0.1:8000/api/v1/groups/{id}/
  ```
- Получить все подписки пользователя, сделавшего запрос, или подписка на пользователя переданного в теле запроса:
  ```
  http://127.0.0.1:8000/api/v1/follow/
  ```
- Получить JWT-токена:
  ```
  http://127.0.0.1:8000/api/v1/jwt/create/
  ```
- Обновить JWT-токена:
  ```
  http://127.0.0.1:8000/api/v1/jwt/refresh/
  ```
- Проверить JWT-токена:
  ```
  http://127.0.0.1:8000/api/v1/jwt/verify/
  ```

  Автор: студент когорты 50+Python
      
  Васильев В.Г.