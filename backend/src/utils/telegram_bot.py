from telebot import TeleBot
from PIL import Image
import io

# Assuming neuro_ark.py is in a subdirectory named 'neuro'
from neuro.neuro_ark import neuro_check  # Corrected import

API_KEY = '8109035980:AAHEEvg4sQWJvhybnFMZzYhB9GzzvBczAMk'  # Replace with your actual API key

bot = TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    user_name = message.from_user.username

    bot.send_message(user_id, f'Привет, {user_name}! NSCheck - сервис первичной оценки онкологии кожи по фотографии. Я бот-аналог веб приложения NSCheck. Отправьте мне фотографию с потенциальным заболеванием, и наш искусственный интеллект даст ответ. ')


@bot.message_handler(content_types=['photo'])
def handle_photo_message(message):
    user_id = message.from_user.id

    try:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Convert downloaded bytes to a file-like object
        image = Image.open(io.BytesIO(downloaded_file))

        result = neuro_check(image) # Pass the Pillow Image object to neuro_check

        bot.send_message(user_id, result)

    except Exception as e:
        print(f"Error processing image: {e}")
        bot.send_message(user_id, "Произошла ошибка при обработке изображения.  Попробуйте еще раз или свяжитесь с поддержкой.")

@bot.message_handler(content_types=['document'])
def handle_photo_message(message):
    user_id = message.from_user.id

    try:
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Convert downloaded bytes to a file-like object
        image = Image.open(io.BytesIO(downloaded_file))

        result = neuro_check(image) # Pass the Pillow Image object to neuro_check

        bot.send_message(user_id, result)

    except Exception as e:
        print(f"Error processing image: {e}")
        bot.send_message(user_id, "Произошла ошибка при обработке изображения.  Попробуйте еще раз или свяжитесь с поддержкой.")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Бот принимает только ФОТОГРАФИИ. Пожалуйста отправьте фото")

bot.polling(none_stop=True)