import random


def load_words(falename):
    '''

    '''
    new_lines = []
    with open(falename, 'r', encoding='utf-8') as fale:
        for line in fale.readlines():
            new_lines.append(line.strip('\n'))
    return new_lines


def random_letters(letter):
    '''
    Перемешиваем буквы в словах
    '''
    letter = list(letter)
    random.shuffle(letter)
    return ''.join(letter)

