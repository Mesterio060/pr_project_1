counter = 0
max_counter = 0
game_counter = 0

# Указываем из какого файла мы импортируем функции.
from utils import load_words, random_letters

words_txt = 'words.txt'

# Приветствие пользователя.
user_name = input("Введите ваше имя: ")


# Запускаем цикол слов с перемешанными буквами.
words = load_words(words_txt)
for word in words:
    print(f"\nУгадайте слово: {random_letters(word)}")
    user_answer = input("Введите ответ: ")
    if user_answer == word:
        print("Верно! Вы получаете 10 очков.")
        counter += 10
    else:
        print(f"Неверно! Верный ответ – {word}")

# Записываем имя и рекорд пользователя в отдельный "history.txt" файл.
with open('history.txt', 'a') as fale:
    fale.write(f"{user_name} {counter}\n")


with open('history.txt', 'r', encoding='utf-8') as fale:
    for line in fale.readlines():
        game_counter += 1
        counter = int(line.split(' ')[1])
        if counter > max_counter:
            max_counter = counter


print(f"\nВсего игр сыграно: {game_counter}\n"
      f"Максимальный рекорд: {max_counter}")
