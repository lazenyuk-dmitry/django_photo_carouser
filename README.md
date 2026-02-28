# NASA Gallery

Проект представляет собой интерактивную галерею изображений космической тематики.
Сборка выполнена в рамках технического задания с использованием инструментов разработки на Python и Django.

## 🚀 Стек технологий

- Backend: Python 3.12, Django 5.2
- Database: MySQL
- Frontend: Bootstrap 5, SCSS (django-sass-processor)
- Slider: Slick Slider & Fancybox (Slider Syncing mode)
- Media Management: django-filer
- Admin UI: django-admin-sortable2 (Drag&Drop сортировка)
- Optimizing and other: thumbnail, sekizai_tags

## 🧱 Структура проекта

```bash
django_photo_carouser/
├─ 📂 app/ # основное приложение
├─ 📂 slider/ # slider
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
├─ 📄 .gitignore
├─ 📄 LICENSE
├─ 📄 README.md
├─ 📄 docker-compose.yaml
├─ 📄 manage.py
└─ 📄 req.pip
```

## 📃 Функционал

### Слайдер (Slick Slider)

- Реализован режим Slider Syncing: основное большое фото синхронизировано с лентой миниатюр снизу.
- По клику на основное изображение открывается полноэкранный режим просмотра (LightBox).
- Слайдер можно использовать в любом месте с помощью include используется sekizai_tags ждя вставки js и css.

### Панель управления (Admin)

- Русификация: Все модели и поля отображаются на русском языке.
- Визуализация: В списке записей отображаются миниатюры изображений и названия.
- Drag&Drop: Изменение порядка слайдов осуществляется простым перетаскиванием строк в админке.
- Хранилище: Для управления медиафайлами интегрирован пакет django-filer.

## 🛠️ Установка и запуск

### 1. Настройка виртуального окружения

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

### 3. Установка зависимостей

Все необходимые пакеты зафиксированы в req.pip:

```bash
pip install -r req.pip
```

### 4. Настройка базы данных

Убедитесь, что у вас запущен сервер MySQL и создана база данных.
Настройте подключение в .env по шаблону .env.example в секции DATABASES.

```bash
# Быстро создать .env

# Linux / macOS / Git Bash
cp .env.example .env
# В Windows (PowerShell)
copy .env.example .env
```

```ini
# Django settings
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

# MySQL Database
DB_NAME=django_db
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=127.0.0.1
DB_PORT=3306
```

***Если нужно то можно запустить базу в докере***

```bash
docker-compose up --build -d
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
