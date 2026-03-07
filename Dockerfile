FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:${PATH}"

ENV APP_HOME=/home/appuser/app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser

WORKDIR $APP_HOME
RUN chown -R appuser:appuser $APP_HOME

RUN mkdir -p staticfiles && chown appuser:appuser staticfiles

COPY --chown=appuser:appuser req.pip .
RUN pip install --no-cache-dir -r req.pip

COPY --chown=appuser:appuser . .
RUN chmod +x entrypoint.sh

USER appuser

ENTRYPOINT ["./entrypoint.sh"]
