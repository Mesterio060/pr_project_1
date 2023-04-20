from config import WORDS_AS_JSON_URL
import utils
from player import Player


def main():
    print("Ввведите имя игрока")
    player_name = input()

    player = Player(player_name)
    basic_word = utils.load_random_word(WORDS_AS_JSON_URL)

    print("Привет", player.get_name())
    print(f'Составьте {basic_word.count_available_words()} слов из слова {basic_word.get_word().upper()}')
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
    print("Поехали, ваше первое слово?")

    while player.count_words() < basic_word.count_available_words():

        user_input = input().strip().lower()

        if user_input in ["стоп", "stop"]:
            """Закончить игру"""
            break

        elif len(user_input) < 3:
            print("Слишком короткое слово")

        elif not basic_word.has_available_words(user_input):
            print("Такое слово составить нельзя!")

        elif player.has_word(user_input):
            print("Такое слово уже угаданно!")

        else:
            print("Верно!")
            player.add_word(user_input)

    print(f"Игра завершена, вы угадали {player.count_words()} слов!")


main()
