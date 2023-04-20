import random

from utils import load_questions, output_statistics


filename = 'questions.json'

questions = load_questions(filename)

random.shuffle(questions)

for question in questions:
    print(question.build_question())

    user_answer = input('Ваш ответ: ')
    question.user_answer = user_answer
    print(question.build_feedback())

print(output_statistics(questions))
