FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install -r req.pip

# Предварительная подготовка
RUN python manage.py compilesass
RUN python manage.py collectstatic --noinput

# Запуск мониторинга (тот самый /healthy) и сервера
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
