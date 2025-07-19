import time
from base64 import b64encode

from backend.core.image_converter import convert_image_for_ocr
from backend.core.ocr import extract_ocr_data_from_id_card


def ocr_service(image_content: bytes) -> dict | None:
    image_processing_time = time.perf_counter()
    processed_image = convert_image_for_ocr(image_content, max_width=600)
    image_processing_time = time.perf_counter() - image_processing_time
    encoded_image = b64encode(processed_image).decode("utf-8")
    ocr_time = time.perf_counter()
    data = extract_ocr_data_from_id_card(f"data:image/jpeg;base64,{encoded_image}")
    ocr_time = time.perf_counter() - ocr_time

    return {
        "image_processing_time": f"{image_processing_time:.2f}",
        "ocr_time": f"{ocr_time:.2f}",
        "data": data
    }
