import os

from dotenv import load_dotenv
from pydantic import BaseModel
import yaml


class Config(BaseModel):
    ocr_model: str
    ocr_prompt: str
    test_data_dir: str


class Env(BaseModel):
    MISTRAL_API_KEY: str
    DATABASE_URL: str
    UPLOADTHING_TOKEN: str
    CLERK_SECRET_KEY: str
    CLERK_JWT_KEY: str


def load_config(config_path: str = "config.yaml") -> Config:
    """
    Load configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        Config: A Config object containing the configuration settings.
    """
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        return Config(**config)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found at {config_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file {config_path}: {e}")


def load_env() -> Env:
    """
    Load environment variables from a .env file.

    Returns:
        Env: An Env object containing the environment variables.
    """
    try:
        load_dotenv()
        return Env(
            MISTRAL_API_KEY=os.environ["MISTRAL_API_KEY"],
            DATABASE_URL=os.environ["DATABASE_URL"],
            UPLOADTHING_TOKEN=os.environ["UPLOADTHING_TOKEN"],
            CLERK_SECRET_KEY=os.environ["CLERK_SECRET_KEY"],
            CLERK_JWT_KEY=os.environ["CLERK_JWT_KEY"],
        )
    except KeyError as e:
        raise KeyError(f"Missing environment variable: {e}")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error loading environment variables: {e}")
