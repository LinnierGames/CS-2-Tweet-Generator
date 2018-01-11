import random
import sys

from benchmark import Benchmark

# does not check if the argument is present

f_words = open("/usr/share/dict/words", "rb")
str_words = f_words.read()
f_words.close()

arr_words = str_words.split('\n')
int_word_array_size = len(arr_words)

int_nWords_to_pick = int(sys.argv[1])
arr_collection_of_selected_words = []

def f():
    for i in range(0,int_nWords_to_pick):
        random.seed()
        int_random_index = int(random.uniform(0, int_word_array_size -1))
        arr_collection_of_selected_words.append(arr_words[int_random_index])

    sentence = " ".join(arr_collection_of_selected_words)

Benchmark(f).fire(5)