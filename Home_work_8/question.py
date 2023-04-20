class Question:
    def __init__(self, text, complexity, right_answer):
        self.text = text
        self.complexity = complexity
        self.right_answer = right_answer

        self.is_asked = False
        self.user_answer = None
        self.score_dall = self.complexity * 10

    def get_points(self):

        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """

        return self.score_dall

    def is_correct(self):

        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """

        return self.right_answer == self.user_answer

    def build_question(self):

        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f'Вопрос: {self.text} \n'\
               f'Сложность: {self.complexity}/5'

    def build_feedback(self):

        """
        Возвращает :
        Ответ верный, получено __ баллов
        Ответ неверный, верный ответ: __
        """

        if self.is_correct():
            return f'Ответ верный, получено {self.score_dall} баллов\n'
        else:
            return f'Ответ неверный, верный ответ: {self.right_answer}\n'
