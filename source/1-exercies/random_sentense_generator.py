import random
import sys

# Picks from words file and randomly picks the given amount
#
# Usage: python random_sentense_generator.py 8
# adrostral undutifulness crystallomancy inscription organogeny Puru pubotibial
# amanori

f_words = open("/usr/share/dict/words", "rb")
str_words = f_words.read()
f_words.close()

arr_words = str_words.split('\n')
int_word_array_size = len(arr_words)

int_nWords_to_pick = int(sys.argv[1])
arr_collection_of_selected_words = []

for i in range(0,int_nWords_to_pick):
    random.seed()
    int_random_index = int(random.uniform(0, int_word_array_size -1))
    arr_collection_of_selected_words.append(arr_words[int_random_index])

sentense = " ".join(arr_collection_of_selected_words)

print(sentense)
