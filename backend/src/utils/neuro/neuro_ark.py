import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf

# 1. Загрузка сохраненной модели
model_path = 'TheBest97.h5'  # Убедитесь, что путь корректен
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Модель не найдена по пути: {model_path}")

model = load_model(model_path)
print("Модель успешно загружена.")

# 2. Загрузка и предварительная обработка изображения
def load_and_preprocess_image(img_path, target_size=(32, 32)):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Изображение не найдено по пути: {img_path}")
    
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Нормализация (так же, как в обучении)
    return img_array

# Укажите путь к вашему изображению
def neuro_check(image_path):
    user_image_path = image_path  # Замените на реальный путь
    processed_image = load_and_preprocess_image(user_image_path)

    # 3. Предсказание класса на основе изображения
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions, axis=1)

    # Список названий классов (проверьте, что он совпадает с тем, что использовалось при обучении)
    class_names = ['class_0', 'class_1', 'class_2', 'class_3', 'class_4', 'class_5', 'class_6']  # Замените на реальные названия классов

    predicted_label = class_names[predicted_class[0]]
    confidence = predictions[0][predicted_class[0]]

    return f"Предсказанный класс: {predicted_label} с уверенностью {confidence*100:.2f}%"

# 4. Отображение изображения с предсказанием
