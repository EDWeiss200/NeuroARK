FROM python:3.11.1-slim

# set work directory
WORKDIR /src

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
RUN apt-get update && apt-get install -y git git-lfs

    # Инициализируем Git LFS
RUN git lfs install

    # Копируем все файлы проекта (включая указатели LFS)
COPY . .

    # Загружаем LFS-файлы
RUN git lfs pull

    # Теперь копируем код приложения в WORKDIR
COPY src/ /app/src
