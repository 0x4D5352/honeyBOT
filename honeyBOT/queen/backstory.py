import gpt4all
from datetime import date
from secrets import randbelow

def get_models():
    # useful for testing out different models later
    return [model["filename"] for model in gpt4all.GPT4All.list_models()]