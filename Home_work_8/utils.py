import json

from Home_work_8.question import Question


def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        datas = json.load(file)

    questions = []

    for data in datas:
        text = data['q']
        complexity = int(data['d'])
        right_answer = data['a']

        question = Question(text, complexity, right_answer)

        questions.append(question)

    return questions


def output_statistics(questions):
    """
    Делам подсчёт правильных ответов и количество набранных баллов
    Выводим статистику
    """
    score = 0
    count = 0

    for question in questions:
        if question.is_correct():
            score = score + question.score_dall
            count += 1

    number_questions = len(questions)

    if count == 1:
        end_query = 'вопрос'
    elif 2 >= count <= 4:
        end_query = 'вопроса'
    else:
        end_query = 'вопросов'

    return f'Вот и всё!\n'\
           f'Отвечено на {count} {end_query} из {number_questions}\n'\
           f'Набрано баллов: {score}'
