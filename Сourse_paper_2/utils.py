import random

import requests

from Сourse_paper_2.game_word import BasicWord


def load_data_from_url(path):
    """Выполняет загрузку по указанному пути"""
    result = requests.get(path)

    if result.status_code != 200:
        return None

    data = result.json()
    return data


def load_random_word(path):
    """Получает данные из удаленного хранилища, возвращает экземпляр BasicWord"""

    data = load_data_from_url(path)

    if data is None:
        return None

    random_word_date = random.choice(data)

    new_word = BasicWord(
        word=random_word_date["word"],
        available_words=random_word_date["subwords"]
    )

    return new_word
