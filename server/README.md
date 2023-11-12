# Users app
### <ins>**registration**</ins>
**url:** http://localhost:8000/api/v1/auth/

**method:** POST

**request data:**
```json
{
    "email": "example@mail.ru",
    "password": "example123"
}
```

**response data:**
```json
// Ответ на валидный запрос.
// Status: 201 Created.
{
    "email": "example@mail.ru",
    "id": 23
}

// Ответ на невалидный запрос.
// Status: 400 Bad Request.
{
    "email": [
        "user с таким email уже существует."
    ],
    "password": [
        "Введенный пароль слишком короткий. Он должен содержать минимум 8 символов.",
        "Введенный пароль слишком широко распространён"
    ]
}
```

<br>

### <ins>**login**</ins>
**url:** http://localhost:8000/api/v1/auth/token/login/

**method:** POST

**request data:**
```json
{
    "email": "example@mail.ru",
    "password": "example123"
}
```

**response data:**
```json
// Ответ на валидный запрос.
// Status: 200 OK
{
    "auth_token": "1381077e9610365f66c81afd55436e19a108000c"
}

// Ответ на невалидный запрос.
// Status: 400 Bad Request
{
    "non_field_errors": [
        "Невозможно войти с предоставленными учетными данными."
    ]
}
```

<br>

### <ins>**get profile**</ins>
**url:** http://localhost:8000/api/v1/profile/

**method:** POST

**headers:** Authorization: Token <auth_token>

**response data:**
```json
// Ответ на валидный запрос.
// Status: 200 OK.
{
    "email": "example@mail.ru",
    "profile": {
        "last_name": "Фамилия",
        "first_name": "Имя",
        "patronymic": "Отчетво",
        "sex": "мужчина",
        "birth_date": "2003-12-10",
        "phone": "89017583726",
        "passport": {
            "numbers": 1234,
            "series": 4321,
            "registration_place": "Ярославль",
            "created_at": "2023-11-08"
        },
        "birth_sertificate": {
            "registration_place": "Ярославль",
            "place_of_birth": "Ярославль",
            "vital_record": 1234
        },
        "address": "г. Москва, ул. Таганская, д. 78/19, кв. 121",
        "image": "/media/89010557301/2023-11-08_171908.269520.jpg"
    },
    "role": {
        "role_name": "admin"
    }
}

// Ответ на невалидный запрос.
// Status: 400 Bad Request.
{
    "detail": "Недопустимый токен."
}
```

<br>

### <ins>**create/update profile**</ins>
**url:** http://localhost:8000/api/v1/profile/

**method:** POST

**headers:** Authorization: Token <auth_token>

**request data:**
```json
// Поля для создания нового профиля
{
    "last_name": "Фамилия",
    "first_name": "Имя",
    "patronymic": "Отчество если есть",
    "sex": "мужчина/женщина",
    "birth_date": "yyyy-MM-DD",
    "phone": "89019482712",
    "address": "г. Город, ул. Улица, д. Дом, кв. Квартира",
    "image": "file",
    "numbers": "номер паспорта",
    "series": "серия паспорта",
    "registration_place": "паспорт выдан...",
    "created_at": "дата выдачи паспорта yyyy-MM-DD"
}

// Поля для обновления профиля.
// Идентичные поля, но с обновленной информацией,
// чтобы оставить старые данные, явно укажите их снова.
{
    "last_name": "Фамилия",
    "first_name": "Имя",
    "patronymic": "Отчество если есть",
    "sex": "мужчина/женщина",
    "birth_date": "yyyy-MM-DD",
    "phone": "89019482712",
    "address": "г. Город, ул. Улица, д. Дом, кв. Квартира",
    "image": "file",
    "numbers": "номер паспорта",
    "series": "серия паспорта",
    "registration_place": "паспорт выдан...",
    "created_at": "дата выдачи паспорта yyyy-MM-DD"
}
```

**response data:**
```json
// Невалидных данных быть не может, валидация проходит со стороны клиента.
// Валидные данные при создании нового профиля.
// Status: 201 Created.
{
    "email": "example@mail.ru",
    "profile": {
        "last_name": "Фамилия",
        "first_name": "Имя",
        "patronymic": "Отчетво",
        "sex": "мужчина",
        "birth_date": "2003-12-10",
        "phone": "89017583726",
        "passport": {
            "numbers": 1234,
            "series": 4321,
            "registration_place": "Ярославль",
            "created_at": "2023-11-08"
        },
        "birth_sertificate": {
            "registration_place": "Ярославль",
            "place_of_birth": "Ярославль",
            "vital_record": 1234
        },
        "address": "г. Москва, ул. Таганская, д. 78/19, кв. 121",
        "image": "/media/89010557301/2023-11-08_171908.269520.jpg"
    },
    "role": {
        "role_name": "admin"
    }
}

// Валидные данные при обновлении профлиля.
// Status: 200 OK
{
    "message": "данные были обновлены"
}
```

<br>
<br>

# Relationships

### <ins>**get your relatives**</ins>
**url:** http://localhost:8000/api/v1/relatives/

**method:** GET

**headers:** Authorization: Token <auth_token>

**response data:**
```json
// Ответ на валидные данные.
// Status: 200 OK.
[
    {
        "id": 8,
        "abstract_profile": {
            "last_name": "Изменил",
            "first_name": "Изменил",
            "patronymic": "Изменил",
            "phone": "Изменил",
            "birth_date": "2003-10-11",
            "address": "Изменил"
        },
        "status": {
            "status_name": "Дедушка"
        }
    },
    {
        "id": 9,
        "abstract_profile": {
            "last_name": "Насонов",
            "first_name": "Алексей",
            "patronymic": "Игоревич",
            "phone": "891344532395",
            "birth_date": "2023-11-09",
            "address": "г. Москва, ул. Таганская, д. 15, кв. 121"
        },
        "status": {
            "status_name": "Брат"
        }
    },
    {
        "id": 10,
        "abstract_profile": {
            "last_name": "Фамилия",
            "first_name": "Имя",
            "patronymic": "Отчество",
            "phone": "89348372847",
            "birth_date": "1980-12-01",
            "address": "г. Ярославль, ул. Победы, д. 78/19, кв. 121"
        },
        "status": {
            "status_name": "Бабушка"
        }
    }
]

// Ответ на невалидные данные.
// Status: 401 Unauthorized
{
    "detail": "Недопустимый токен."
}
```

<br>


### <ins>**add a new relative**</ins>
**url:** http://localhost:8000/api/v1/relatives/

**method:** POST

**headers:** Authorization: Token <auth_token>

**request data:**
```json
{
    "last_name": "Фамилия",
    "first_name": "Имя",
    "patronymic": "Отчество",
    "phone": "89015738172",
    "birth_date": "yyyy-MM-DD",
    "address": "г. Город, ул. Улица, д. Дом, кв. Квартира",
    "status_name": "Мать/Отец/Бабушка/Дедушка/Тетя/Дядя"
}
```

**response data:**
```json
// Ответ на валидные данные.
// Status: 201 Created.
{
    "message": "запись была успешно сохранена"
}

// Ответ на невалидные данные.
// Status: 400 Bad Request.
{
    "message": "пользователь с такими данными уже существует"
}

// Ответ на невалидный токен
// Status: 401 Unauthorized
{
    "detail": "Недопустимый токен."
}
```

<br>

### <ins>**delete relative by id**</ins>
**url:** http://localhost:8000/api/v1/relatives/7/

**method:** DELETE

**headers:** Authorization: Token <auth_token>

**response data:**
```json
// Ответ на валидные данные.
// Status: 200 OK.
{
    "message": "запись была успешно удалена"
}

// Ответ на невалидные данные.
// Status: 400 Bad Request.
{
    "message": "записи с id 7 не существует"
}

// Ответ на невалидный токен
// Status: 401 Unauthorized
{
    "detail": "Недопустимый токен."
}
```

<br>

### <ins>**update relative by id**</ins>
**url:** http://localhost:8000/api/v1/relatives/8/

**method:** PUT

**headers:** Authorization: Token <auth_token>

**request data:**
```json
// Если нужно оставить старые данные, то нужно явно их указать снова.
{
    "last_name": "новая фамилия",
    "first_name": "новое имя",
    "patronymic": "новое отчество",
    "phone": "новый телефон",
    "birth_date": "yyyy-MM-DD",
    "address": "новый адрес (г. Город, ул. Улица, д. Дом, кв. Квартира)",
    "status_name": "новый статус (Мать/Отец/Бабушка/Дедушка/Тетя/Дядя)"
}
```

**response data:**
```json
// Ответ на валидные данные.
// Status: 200 OK.
{
    "message": "запись была успешно обновлена"
}

// Ответ на невалидные данные.
// Status: 400 Bad Request.
{
    "message": "записи с id 7 не существует"
}

// Ответ на невалидный токен
// Status: 401 Unauthorized
{
    "detail": "Недопустимый токен."
}
```
