from fastapi import UploadFile, File, Form
import io
import cv2
import numpy as np

@app.post('/predict')
async def predict(file: UploadFile = File(...), mdl_name: str = Form('./models/09_cds2_s-seg_1280_100e.pt')):
    if not file:
        return {"‼️ error": "🚷 No file uploaded"}
    
    # Получение расширения файла
    file_extension = file.filename.split('.')[-1].lower()

    # Поддерживаемые форматы
    supported_formats = ["jpg", "jpeg", "png", "bmp", "tiff"]
    if file_extension not in supported_formats:
        return {"error": f"Unsupported file format: {file_extension}"}

    image_stream = io.BytesIO(await file.read())
    image_stream.seek(0)
    image = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), 1)
    image_stream.close()

    if image is None:
        return {"error": "Invalid image file"}

    # ... [Остальная часть вашего кода для обработки изображения]
