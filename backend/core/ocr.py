import json

from mistralai import Mistral

from ..config import load_config, load_env


def extract_ocr_data_from_id_card(base64_image: str) -> dict | None:
    """
    Extracts OCR data from an identity card image using Mistral AI.

    Args:
        base64_image (str): Base64 encoded image.

    Returns:
        dict | None: Extracted OCR data or None if an error occurred.
    """
    env = load_env()
    config = load_config()
    client = Mistral(api_key=env.MISTRAL_API_KEY)

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": config.ocr_prompt,
                },
                {
                    "type": "image_url",
                    "image_url": {"url": base64_image},
                },
            ],
        }
    ]

    try:
        response = client.chat.complete(
            model=config.ocr_model,
            messages=messages,
            response_format={"type": "json_object"},
        )
        json_content = response.choices[0].message.content

        try:
            parsed_json = json.loads(json_content)
            return parsed_json
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from model response.")
            print("Raw response:", json_content)
            return None
    except Exception as e:
        print(f"An API error occurred: {e}")
        return None
