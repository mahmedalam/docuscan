from base64 import b64encode

from rich import print

from ...config import load_config
from ...core import extract_ocr_data_from_id_card


def test_extract_ocr_data_from_id_card():
    config = load_config()

    with open(f"{config.test_data_dir}/id-card-1.jpg", "rb") as f:
        image_data = b64encode(f.read()).decode("utf-8")

    base64_image = f"data:image/jpeg;base64,{image_data}"
    data = extract_ocr_data_from_id_card(base64_image)

    assert data is not None
    assert "name" in data
    assert "gender" in data
    assert "country" in data
    assert "cnic_number" in data
    assert "date_of_birth" in data
    assert "date_of_expiry" in data
    assert "extras" in data

    print(data)
