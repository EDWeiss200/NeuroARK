
FROM python:3.11-slim

        # Установите Git и Git LFS
RUN apt-get update && apt-get install -y git git-lfs

        # Инициализируйте Git LFS
RUN git lfs install

        # Создайте и перейдите в директорию приложения

WORKDIR /src
                # set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


        # Скопируйте файлы зависимостей
COPY requirements.txt .

        # Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

        # Скопируйте остальной код приложения
COPY . .

        # Скачайте файлы LFS (ВАЖНО!)
RUN git lfs pull