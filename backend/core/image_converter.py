from io import BytesIO

from PIL import Image, ImageOps


def convert_image_for_ocr(
        file_bytes: bytes,
        output_format: str = "JPEG",
        max_width: int = 1280,
        grayscale: bool = True,
        quality: int = 85,
) -> bytes:
    """
    Converts image to resized, grayscale JPG.

    Args:
        file_bytes (bytes): Original image bytes
        output_format (str): Output format, default = JPEG
        max_width (int): Max image width
        grayscale (bool): Convert to grayscale or not
        quality (int): JPEG quality (1-100)

    Returns:
        bytes: Processed image as byte stream
    """
    with Image.open(BytesIO(file_bytes)) as img:
        # Convert to RGB
        img = img.convert("RGB")

        # Resize while preserving aspect ratio
        ratio = max_width / float(img.width)
        new_height = int((float(img.height) * float(ratio)))
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Convert to grayscale
        if grayscale:
            img = ImageOps.grayscale(img)

        # Save to buffer
        buffer = BytesIO()
        img.save(buffer, format=output_format, quality=quality, optimize=True)
        buffer.seek(0)
        return buffer.read()
