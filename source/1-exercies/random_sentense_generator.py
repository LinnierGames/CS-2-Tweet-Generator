import random
random.seed(999)

import sys

# Picks from words file and randomly picks the given amount
#
# Usage: python random_sentense_generator.py 8
# adrostral undutifulness crystallomancy inscription organogeny Puru pubotibial
# amanori

with open("/usr/share/dict/words", "r") as f:
    str_words = f.read()

arr_words = str_words.split('\n')
int_word_array_size = len(arr_words)

int_nWords_to_pick = int(sys.argv[1])
# arr_collection_of_selected_words = []
str_collection_of_selected_words = ""

for i in range(0,int_nWords_to_pick):
    int_random_index = int(random.uniform(0, int_word_array_size -1))
    # arr_collection_of_selected_words.append(arr_words[int_random_index])
    str_collection_of_selected_words += arr_words[int_random_index] + ' '

# sentense = " ".join(arr_collection_of_selected_words)

print(str_collection_of_selected_words)
