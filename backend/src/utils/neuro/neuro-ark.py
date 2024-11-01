from PIL import Image
import torch
from ultralytics import YOLO

# Загружаем модель YOLOv8
model = YOLO(r"backend\src\utils\neuro\neuro-ark_model.pt") 

# Загружаем изображение
image_path = r'backend\src\utils\neuro\ISIC_0024313.jpg'
image = Image.open(image_path)

# Выполните детектирование
results = model(image, verbose=False) # Добавлено verbose=False

object_counts = {}
if results: # Проверка, есть ли обнаруженные объекты
  for result in results:
    
    for i in range(len(result.boxes.cls)):
      object_name = result.names[result.boxes.cls[i].item()]
      if object_name in object_counts:
        object_counts[object_name] += 1
      else:
        object_counts[object_name] = 1

# Вывод количества каждого объекта
for object_name, count in object_counts.items():
  print(f"{count} {object_name}")