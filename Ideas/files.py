import os
import time
import re
import glob

def generate_file_name(model_name, images_dir='./images'):
    # Получение текущего времени
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

    # Выделение первых двух цифр из названия модели
    model_digits = re.findall(r'\d+', model_name)[:2]
    model_prefix = ''.join(model_digits)[:2]  # Берем только первые две цифры

    # Определение порядкового номера файла
    existing_files = glob.glob(os.path.join(images_dir, '*.jpg'))  # предполагаем, что изображения в формате .jpg
    next_file_number = len(existing_files) + 1

    # Генерация имени файла
    file_name = f"{current_time}_{str(next_file_number).zfill(5)}_M{model_prefix}.jpg"

    return file_name

# Пример использования
model_name = "model10"  # Пример названия модели
file_name = generate_file_name(model_name)
print(file_name)
