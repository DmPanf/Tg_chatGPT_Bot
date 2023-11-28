import numpy as np
import cv2

def draw_boxes(image: np.ndarray, results: list) -> np.ndarray:
    detected_classes = ""  # Переменная для хранения последовательности классов
    class_positions = []  # Список для хранения классов и их позиций

    # ... [Остальная часть вашего кода]

    for result in results:
        boxes = result.boxes
        for bbox, score, cl in zip(boxes.xyxy.tolist(), boxes.conf.tolist(), boxes.cls.tolist()):
            class_id = int(cl)

            # Сохранение класса и его позиции X
            if 0 <= class_id <= 9:
                class_positions.append((class_id, bbox[0]))  # bbox[0] это X координата левого верхнего угла

            # ... [Остальная часть вашего кода для рисования на изображении]

    # Сортировка классов по X координате
    class_positions.sort(key=lambda x: x[1])

    # Добавление отсортированных классов в detected_classes
    for class_id, _ in class_positions:
        detected_classes += str(class_id)

    print("\nDetected classes sequence:", detected_classes)
    return image, detected_classes
