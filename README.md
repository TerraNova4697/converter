# Django Rest Framework проект конвертации валют

Это простой пример проекта Django Rest Framework, который настроен для работы в среде Docker с использованием Docker Compose.

## Запуск проекта

Для запуска проекта, убедитесь, что у вас установлены Docker и Docker Compose. Затем выполните следующие шаги:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/TerraNova4697/converter.git
   cd converter

2. Запустите проект с помощью Docker Compose

   ```bash
   docker-compose up --build

3. Приложение будет работать на http://localhost:8000/

4. Используется СУБД Postgres, данные кешируются в Redis

## URL маршруты

- GET /api/v1/rates
    Маршрут конвертации валют.
    Обязательные параметры:
        from (str)
        to (str)
    Опциональные:
        value (int) (default=1)
    Возвращает:
        <pre>
        ```json
           {
               "result": 96.82,
               "source": "api",
           }
        ```
        </pre>
- GET /api/v1/rates/currencies/
    Получить список доступных валют для конвертации
    Возвращает:
        <pre>
        ```json
        [
            {
                "title": "United States Dollar",
                "symbol": "USD",
            },
            {
                "title": "Bitcoin",
                "symbol": "BTC",
            },
        ]
        ```
        </pre>

- POST /api/v1/user/create/
    Маршрут регистрации пользователя
    Обязательные параметры:
        <pre>
        ```json
        {
            "email": "user@example.com",
            "password": "string",
            "name": "string",
        }
        ```
        </pre>
    Возвращает:
        <pre>
        ```json
        {
            "email": "user@example.com",
            "name": "string",
        }
        ```
        </pre>

- GET /api/v1/user/me/
    Получить данные аутентифицированного пользователя
    Возвращает:
        <pre>
        ```json
        {
            "email": "user@example.com",
            "name": "string",
        }
        ```
        </pre>

- POST /api/v1/user/token/
    Создать новый токен
    Обязательные параметры:
        <pre>
        ```json
        {
            "email": "user@example.com",
            "password": "string",
        }
        ```
        </pre>
    Возвращает:
        <pre>
        ```json
        {
            "email": "user@example.com",
            "password": "string",
        }
        ```
        </pre>