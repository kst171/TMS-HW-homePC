#!/bin/bash

# 1. Собираем docker образ
docker build -t kst-nginx .

# 2. Запускаем контейнер
docker run -d --name kst-nginx-1 -p 8085:80 kst-nginx

# 3. Проверяем
docker ps

# 4. Создаем Volume
docker volume create kst-nginx-volume-1

# 5. Перезапускаем контейнер с подключением volume
docker rm -f kst-nginx-1
docker run -d --name kst-nginx-1 -p 8085:80 -v kst-nginx-volume-1:/usr/share/nginx/ kst-nginx

# 6. Создаем сеть
docker network create kst-nginx-net

# 7. Перезапускаем контейнер в созданной сети
docker stop kst-nginx-1
docker rm kst-nginx-1
docker run -d --name kst-nginx-1 --network kst-nginx-net -p 8085:80 -v kst-nginx-volume-1:/usr/share/nginx/html kst-nginx
# Либо подключаем уже работающий контейнер к сети
docker network connect kst-nginx-net kst-nginx-1

# 8 Cоздаем второй контейнер и подключаем в ту же сеть
docker run -d --name kst-nginx-2 --network kst-nginx-net nginx:latest

# 9. Заходим в контейнер и устанавливаем утилиту ping
docker exec -u root kst-nginx-1 sh -c "apt-get update && apt-get install -y iputils-ping"

# 10. Запуск ping на второй контейнер по имени (3 пакета)
docker exec kst-nginx-1 ping -c 3 kst-nginx-2

# 11. Проверка какие контейнеры в network
docker network inspect kst-nginx-net

# 12. Просмотр конфига контейнера для отображения подключенного volume
docker inspect kst-nginx-1

# 13. Остановка контейнера
docker stop 49b902349cc3

# 14. Удвление контейнера
docker rm 49b902349cc3

# Удаление volume и сетей аналогично