import os


def load_openai_api_key():
    with open(".openai", "r") as file:
        api_key = file.read().strip()
    os.environ["OPENAI_API_KEY"] = api_key
