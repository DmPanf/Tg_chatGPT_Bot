import json

# Предполагается, что функция generate_file_name и переменные model_name, number, speed, и т.д. уже определены.

# Генерация имени файла для изображения
image_file_name = generate_file_name(model_name)

# Формирование данных для сохранения
image_data = {
    "model_name": model_name,
    "object_count": number,
    "inference": speed,
    "current_time": current_time,
    "counter": counter,
    "wh_check": wh_check,
    "file_name": image_file_name
}

# Замена расширения файла на .json
json_file_name = image_file_name.rsplit('.', 1)[0] + '.json'

# Путь к папке для сохранения
save_path = './images'

# Сохранение данных в JSON файл
with open(f"{save_path}/{json_file_name}", 'w') as json_file:
    json.dump(image_data, json_file, indent=4)
