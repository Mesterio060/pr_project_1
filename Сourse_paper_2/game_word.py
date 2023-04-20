class BasicWord:
    def __init__(self, word="", available_words=None):

        self.word = word

        if available_words is None:
            self.available_words = []
        else:
            self.available_words = available_words

    def __repr__(self):
        return f"BasicWord(word={self.word}, available_words={self.available_words})"

    def get_word(self):
        """"Возвращаает слово"""
        return self.word

    def count_available_words(self):
        """"Подсчёт количество поlслов"""
        return len(self.available_words)

    def has_available_words(self, word):
        """"Возвращает наличие введенного слова в списке допустимых подслов (вернет bool)"""
        return word in self.available_words

        
