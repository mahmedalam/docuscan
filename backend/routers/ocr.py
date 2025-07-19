from fastapi import APIRouter, UploadFile

from backend.services.ocr import ocr_service

router = APIRouter()


@router.post("/ocr/")
async def ocr(file: UploadFile):
    image_content = await file.read()
    data = ocr_service(image_content)

    return data
