# DraftMaster — API Contract

**Base URL:** /api/v1

**Format:** JSON

## 1. Users

| Method | Endpoint | Description |
|---|---|---|
| POST | /users | Создать пользователя |
| GET | /users | Получить список пользователей |
| GET | /users/{user_id} | Получить пользователя по ID |
| PUT | /users/{user_id} | Обновить пользователя |
| DELETE | /users/{user_id} | Удалить пользователя |

## 2. Heroes

| Method | Endpoint | Description |
|---|---|---|
| POST | /heroes | Создать героя |
| GET | /heroes | Получить список героев |
| GET | /heroes/{hero_id} | Получить героя по ID |
| PUT | /heroes/{hero_id} | Обновить информацию о герое |
| DELETE | /heroes/{hero_id} | Удалить героя |

## 3. Drafts

| Method | Endpoint | Description |
|---|---|---|
| POST | /drafts | Создать драфт |
| GET | /drafts | Получить список драфтов |
| GET | /drafts/{draft_id} | Получить драфт по ID |
| PUT | /drafts/{draft_id} | Обновить драфт |
| DELETE | /drafts/{draft_id} | Удалить драфт |

## 4. DraftPicks

| Method | Endpoint | Description |
|---|---|---|
| POST | /drafts/{draft_id}/picks | Добавить героя в драфт |
| GET | /drafts/{draft_id}/picks | Получить список выбранных героев |
| GET | /picks/{pick_id} | Получить пик по ID |
| PUT | /picks/{pick_id} | Обновить пик |
| DELETE | /picks/{pick_id} | Удалить пик |

## 5. Response codes

| Code | Description |
|---|---|
| 200 | OK — запрос успешно выполнен |
| 201 | Created — ресурс создан |
| 204 | No Content — ресурс удалён |
| 400 | Bad Request — неправильный запрос |
| 404 | Not Found — ресурс не найден |
| 422 | Validation Error — ошибка валидации данных |
| 500 | Internal Server Error — внутренняя ошибка сервера |

## 6. Data format

Все запросы и ответы, содержащие данные, используют формат JSON.

### Пример создания драфта

POST /api/v1/drafts

json
{
  "user_id": 1,
  "title": "Ranked Match"
}


### Пример ответа

{
  "id": 1,
  "user_id": 1,
  "title": "Ranked Match",
  "created_at": "2026-11-20T15:00:00"
}
