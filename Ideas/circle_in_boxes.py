import numpy as np
import cv2

# Ваша функция draw_boxes
def draw_boxes(image: np.ndarray, results: list) -> np.ndarray:
    # ... [Остальная часть вашего кода]

    for result in results:
        boxes = result.boxes
        for bbox, score, cl in zip(boxes.xyxy.tolist(), boxes.conf.tolist(), boxes.cls.tolist()):
            input_box = np.array(bbox)

            # Координаты вершины бокса
            vertex = (int(input_box[0]), int(input_box[1]))

            # Рисуем точку на вершине бокса
            cv2.circle(image, vertex, radius=5, color=(0, 0, 255), thickness=-1) # Красная точка

            # ... [Остальная часть вашего кода для рисования на изображении]

    # ... [Остальная часть вашего кода]

    return image
