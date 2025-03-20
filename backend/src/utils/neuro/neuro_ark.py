import os
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf
from PIL import Image

# 1. Загрузка сохраненной модели
model_path = 'utils/neuro/Test2.h5'  # Убедитесь, что путь корректен
#model_path = r'backend\src\utils\neuro\TheBest97.h5'

model = load_model(model_path)
print("Модель успешно загружена.")

# 2. Загрузка и предварительная обработка изображения
def load_and_preprocess_image(img_path, target_size=(32, 32)):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Изображение не найдено по пути: {img_path}")
    
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  
    return img_array

def neuro_check(image: Image.Image):
    # Предобработка изображения 
    target_size = (32, 32) # Теперь мы точно знаем размер!
    img = image.resize(target_size)
    img_array = keras.utils.img_to_array(img) 
    img_array = np.expand_dims(img_array, axis=0)  
    img_array = img_array / 255.0  # Нормализация

    # 3. Предсказание класса на основе изображения
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)

    # Список названий классов 
    class_names = ['Актинический кератоз', 'Базальноклеточная карцинома', 'Доброкачественные кератозоподобные поражения', 'Дерматофиброма', 'Меланоцитарные невусы', 'Меланома', 'Сосудистые поражения']  # Замените на реальные названия классов

    predicted_label = class_names[predicted_class[0]]
    confidence = predictions[0][np.argmax(predictions, axis=1)[0]] 

    return f"Предсказанный класс: {predicted_label} с уверенностью {confidence*100:.2f}%"


