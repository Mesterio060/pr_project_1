from utils import load_random_word
from config import WORDS_AS_JSON_URL

ff = load_random_word(WORDS_AS_JSON_URL)
print(ff)