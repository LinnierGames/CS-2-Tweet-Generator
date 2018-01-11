import sys
from itertools import permutations
import progress_bar

# Usage: python anagram.py iceman
# Progress: |0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000| 100.00000% of 720 iterations
# cinema, anemic were found for iceman

def find_word_in_collection(word, collection):
    if collection.__contains__(word):
        return True
    return False


def collect_words_in_file(file_path):
    """
    opens a file by the given file_path and reads from top to bottom of file
    :param file_path: file to be read as read-only
    :return: complete content of open file
    """
    f_words = open(file_path, "rb")
    words = f_words.read()
    f_words.close()

    return words


def create_collection_of_permutation_of_word(word):
    """
    using a generator, create an array of all possible permutations using itertools.permutations
    :param word: the string to generate
    :return: an array of permutations
    """
    return [''.join(p) for p in permutations(word)]


def collection_of_real_words(collection_of_possible_words):
    """
    enumerates through each possible word and searches if it exists in a list of words found in "/usr/share/dict/words"
    :param collection_of_possible_words: an array of string elements containing words of possible english words
    :return: an array of the matches found in "/usr/share/dict/words"
    """
    str_words = collect_words_in_file("/usr/share/dict/words")
    arr_words = str_words.split('\n')

    len_possible_words = len(collection_of_possible_words)
    words_found = []
    progress_bar.print_progress_bar(0, len_possible_words, 'Progress:', 'Complete', 5)

    for i, permutation in enumerate(collection_of_permutations):
        if find_word_in_collection(permutation, arr_words) and permutation != str_word_term:
            words_found.append(permutation)
        progress_bar.print_progress_bar(i + 1, len_possible_words, 'Progress:',
                                        'of {} iterations'.format(len_possible_words), 5)

    return words_found


str_word_term = str(sys.argv[1]).lower()
collection_of_permutations = create_collection_of_permutation_of_word(str_word_term)
arr_permutations_found_as_a_real_word = collection_of_real_words(collection_of_permutations)

if len(arr_permutations_found_as_a_real_word) == 0:
    print("no other words were found for {}".format(str_word_term))
else:
    str_permutations = ", ".join(arr_permutations_found_as_a_real_word)
    grammar = "was" if len(arr_permutations_found_as_a_real_word) == 1 else "were"
    print("{} {} found for {}".format(str_permutations, grammar, str_word_term))
