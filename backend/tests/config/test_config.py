from rich import print

from ...config import load_config, load_env


def test_config():
    config = load_config()
    env = load_env()
    print(config)
    print(env)
