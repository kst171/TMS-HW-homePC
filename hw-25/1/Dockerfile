FROM ubuntu:24.04

# Блокируем интерактивные окна при сборке
ARG DEBIAN_FRONTEND=noninteractive

# Устанавливаем Nginx и curl
RUN apt-get update && apt-get install -y \
    nginx \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем ваш конфиг в папку sites-enabled
COPY nginx.conf /etc/nginx/sites-enabled/default

# Копируем файлы статики
COPY static /app/static

EXPOSE 8080

# ИСПРАВЛЕНИЕ: Запускаем через главный конфиг Nginx, который сам подключит ваш default
CMD ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]
