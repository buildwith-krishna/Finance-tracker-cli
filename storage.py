import json
from config import FILE_NAME

def load():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data

    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save(data):

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
