import numpy as np
import cv2

# Ваша функция draw_boxes
def draw_boxes(image: np.ndarray, results: list) -> np.ndarray:
    # ... [Остальная часть вашего кода]

    for result in results:
        boxes = result.boxes
        for bbox, score, cl in zip(boxes.xyxy.tolist(), boxes.conf.tolist(), boxes.cls.tolist()):
            input_box = np.array(bbox)

            # Вычисление ширины и высоты bounding box
            width = input_box[2] - input_box[0]  # x2 - x1
            height = input_box[3] - input_box[1] # y2 - y1

            # Проверка условия: ширина больше высоты
            if width > height:
                wh_check = "✅ W > H"
            else:
                wh_check = "❌ W ≤ H"

            # Вывод сообщения на изображение
            cv2.putText(image, wh_check, (int(input_box[0]), int(input_box[1]) - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # ... [Остальная часть вашего кода для рисования на изображении]

    # ... [Остальная часть вашего кода]

    return image
