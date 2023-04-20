class Player:

    """Класс хронит информацию о игроке и его слова"""

    def __init__(self, name, words=None):

        self.name = name

        if words is None:
            self.words = []
        else:
            self.words = words

    def __repr__(self):
        return f"Player(name={self.name}, words={self.words})"

    def get_name(self):
        return self.name

    def count_words(self):
        """Возвращает количество использованных слов"""
        return len(self.words)

    def add_word(self, word):
        """Добавляет слова в использованные слова"""
        self.words.append(word.strip().lower())

    def has_word(self, word):
        """Возавращает, если ли это слово у игрока"""
        return word in self.words
