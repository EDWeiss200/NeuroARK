    # Пример, адаптируйте к вашему случаю
FROM python:3.11-slim-buster

WORKDIR /app  # Или другое подходящее место

    # Копируем зависимости (requirements.txt)
COPY requirements.txt .

    # Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

    # Устанавливаем Git и Git LFS (если еще не установлены)
RUN apt-get update && apt-get install -y git git-lfs

    # Инициализируем Git LFS
RUN git lfs install

    # Копируем все файлы проекта (включая указатели LFS)
COPY . .

    # Загружаем LFS-файлы
RUN git lfs pull

    # Теперь копируем код приложения в WORKDIR
COPY src/ /app/src