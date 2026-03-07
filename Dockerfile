FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:${PATH}"

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser
RUN mkdir -p /home/appuser/app/staticfiles && chown appuser:appuser /home/appuser/app/staticfiles

WORKDIR /home/appuser/app

COPY --chown=appuser:appuser req.pip .
RUN pip install --no-cache-dir -r req.pip

COPY --chown=appuser:appuser . .
RUN chmod +x /home/appuser/app/entrypoint.sh

USER appuser

ENTRYPOINT ["/home/appuser/app/entrypoint.sh"]
