# 🚀 NASA Gallery

Проект представляет собой интерактивную галерею изображений космической тематики.
Сборка выполнена в рамках технического задания с использованием инструментов разработки на Python и Django.
Полнофункциональное веб-приложение с автоматизированным CI/CD циклом, контейнеризацией, облачной базой данных и хранилищем S3.

- DEMO сайта доступно здесь: https://django-photo-carousel.onrender.com
- Monitoring: https://stats.uptimerobot.com/H1UsNvDDlZ/802499598

Могу предоставить доступ к админке для тестов, по запросу [@lazenyuk-dmitry](http://github.com/lazenyuk-dmitry)

## 📚 Стек технологий

- Backend: Python 3.12, Django 5.2
- Database: MySQL
- Frontend: Bootstrap 5, SCSS (django-sass-processor)
- Slider: Slick Slider & Fancybox (Slider Syncing mode)
- Media Management: django-filer
- Admin UI: django-admin-sortable2 (Drag&Drop сортировка)
- Optimizing and other: thumbnail, sekizai_tags

## 📈 Infrastructure

- Build: Docker, Docker Compose.
- Database: TiDB Cloud (Serverless MySQL) + SSL Encryption.
- Storage: Supabase S3.
- Deployment: Render (PaaS).
- DevOps: Bash-скрипты для автоматизации (entrypoint, wait-for-db).
- Monitoring: uptimerobot.com & Discord alerts.

## 📃 Функционал

### Слайдер (Slick Slider/Fancybox)

- Реализован режим Slider Syncing: основное большое фото синхронизировано с лентой миниатюр снизу.
- По клику на основное изображение открывается полноэкранный режим просмотра (Fancybox).
- Синхронизация работает как между двумя слайдерами так и при прокрутки в Fancybox, в слайдере переключается фокус на активный слайдер в Fancybox.
- Слайдер можно использовать в любом месте с помощью include используется sekizai_tags ждя вставки js и css.

### Панель управления (Admin)

- Русификация: Все модели и поля отображаются на русском языке.
- Визуализация: В списке записей отображаются миниатюры изображений и названия.
- Drag&Drop: Изменение порядка слайдов осуществляется простым перетаскиванием строк в админке.
- Хранилище: Для управления медиафайлами интегрирован пакет django-filer.

## 🗳️ Архитектурные особенности

### Контейнеризация

Использование многоэтапной сборки и запуск от не-root пользователя (appuser) для повышения безопасности.

### Умный Entrypoint

Скрипт автоматической проверки доступности БД через TCP-сокеты перед запуском миграций.

### Оптимизация ресурсов

Настройка Gunicorn воркеров с использованием /dev/shm (Shared Memory) для стабильной работы на ограниченных ресурсах (Free Tier).

### Безопасность

Поддержка SSL-соединений с базой данных и управление секретами через переменные окружения.

### Мониторинг

Мониторинг доступен по адресу `/_/healthz/` только с авторизацией по bearer token.
Проверка настроена через uptimerobot.com с отправкой оповещений об инцидентах в приватный канал Discord.

Примерный ответ `healthz`

```json
{
    "status": "healthy",
    "uptime": "0:40:00",
    "checks": {
        "db": {
            "status": "healthy",
            "error": null,
            "latency": 0.060978060006164014
        },
        "storage": {
            "status": "healthy",
            "error": null,
            "latency": 0.6303582119871862
        },
        "disk": {
            "status": "healthy",
            "error": null,
            "latency": 0.002901647996623069
        }
    }
}
```

## 🧱 Структура проекта

```bash
django_photo_carouser/
├─ 📂 app/ # основное приложение
├─ 📂 slider/ # slider
├─ 📂 health/ # health check
├─ 📂 static/ # статика
│ ├─ 📂 favicon/
│ ├─ 📂 icons/
│ │ └─ 📄 sprite.svg # спрайт с иконками
│ ├─ 📂 images/
│ └─ 📁 styles/ # стили (SCSS)
│   ├─ 📂 abstract/
│ │ │ └─ 📄 _config.scss
│   ├─ 📂 base/
│ │ │ ├─ 📄 _base.scss
│ │ │ └─ 📄 _typography.scss
│   ├─ 📂 components/
│ │ │ ├─ 📄 _icon.scss
│ │ │ └─ 📄 _slider.scss
│   ├─ 📂 layouts/
│ │ │ └─ 📄 _header.scss
│   └─ 📄 main.scss # точка сборки стилей, переменных и конфигов
├─ 📂 staticfiles/ # сюда django собирает статику
├─ 📂 templates/ # html шаблоны
│ ├─ 📂 includes/ # общие подключаемые компоненты
│ │ ├─ 📄 _header.html
│ │ └─ 📄 _icon.html
│ └─ 📄 index.html
├─ 📄 .env
├─ 📄 .env.example
├─ 📄 .dockerignore
├─ 📄 .gitignore
├─ 📄 LICENSE
├─ 📄 README.md
├─ 📄 Dockerfile
├─ 📄 docker-compose.yaml
├─ 📄 entrypoint.sh
├─ 📄 manage.py
└─ 📄 req.pip
```

## 🚩 Быстрый старт (Docker)

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/lazenyuk-dmitry/django_photo_carousel.git
cd django_photo_carousel
```

### 2. Настройте переменные окружения (скопируйте и переименуйте .env.example -> .env)

Можно создать копию командой в терминале

```bash
# Linux / macOS / Git Bash
cp .env.example .env
# В Windows (PowerShell)
copy .env.example .env
```

Заполните своими данными

```ini
# Django settings
DEBUG=False
SECRET_KEY='django-insecure-....'
ALLOWED_HOSTS=localhost,127.0.0.1
HEALTH_CHECK_TOKEN="secret123" # Bearer token
GUNICORN_WORKERS=1 # количество воркеров для Gunicorn (2 * {CPU Cores}) + 1

# путь к сертификату если требует база данных
# при запуске в Docker генерируется автоматически
SSL_CA='/etc/ssl/certs/ca-certificates.crt' # стандартный путь для Debian/Ubuntu

# SuperUser (только для полного запуска в Docker)
# Cоздает супер пользователя если еще нету
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@email.com
DJANGO_SUPERUSER_PASSWORD=123456789

# MySQL Database
DB_NAME=django_db
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=db
DB_PORT=3306

#S3
USE_S3=True
AWS_ACCESS_KEY_ID="..."
AWS_SECRET_ACCESS_KEY="..."
AWS_STORAGE_BUCKET_NAME="..."
AWS_S3_ENDPOINT_URL="..."
AWS_S3_REGION_NAME='us-east-1'
```

### 3. Запустите через Docker Compose

```bash
docker-compose up --build -d
```

---

## 🛠️ Запуск для разработки (Dev)

### 1. Настройте виртуальное окружение

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

### 3. Установите зависимости

Все необходимые пакеты зафиксированы в req.pip:

```bash
pip install -r req.pip
```

### 4. Настройте переменных окружения `.env`

Смотрите быстрый запуск шаг 2

### 5. Настройка базы данных

Убедитесь, что у вас запущен сервер MySQL и создана база данных.
Настройте подключение в .env по шаблону .env.example в секции *# MySQL Database*.

Если быстро нужна база и не хочется заморачивать можно запустить в докере только сервис базы данных.
База запуститься с настройками из `.env` файла.

```bash
docker-compose up db --build -d
```

### 5. Миграции и создание администратора

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Запуск сервера

```bash
python manage.py runserver
```

---

## ℹ️ Прочие команды

### Сборка статики

```bash
python manage.py compilescss
python manage.py collectstatic --ignore=*.scss --noinput
```

### Запуск сервера gunicorn

```bash
gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3
```
