import sys
sys.path.insert(0,"../4-exercies")
import random
from stochastic import Stochastic


class Markov(object):
    punctuation = [".","?","!"]

    def __init__(self, list_words=None):

        # TODO: separate ending puncuation from words in the list_words, such as . ? and !
        self.corpus = list_words
        self.words = {} # [String: Stochastic]

        # iterate corpus
        previous_word = None
        for index, current_word in enumerate(self.corpus):
            adjacent_word = None  # None is equal to stop

            def get_adjacent_word():
                try:
                    return self.corpus[index + 1]
                except IndexError:
                    # end of list_words, thus end of sentence
                    return None

            # if current_word is an ending puncation, then adjacent_word is None

            # check: at beginning of sentence
            if index == 0 or previous_word in Markov.punctuation:
                stochastic_for_beginning_of_sentence = self.words.get(None, None)
                if stochastic_for_beginning_of_sentence is None:
                    stochastic_for_beginning_of_sentence = Stochastic()
                    self.words[None] = stochastic_for_beginning_of_sentence

                stochastic_for_beginning_of_sentence.add_count(current_word)

            # grab adjacent word, can be None to represent end of the sentence
            adjacent_word = get_adjacent_word()

            # check: at end of sentence or
            if current_word in Markov.punctuation:
                adjacent_word = None
                continue

            stochastic_for_current_word = None
            if current_word in self.words:
                stochastic_for_current_word = self.words[current_word]
            else:
                stochastic_for_current_word = Stochastic()
                self.words[current_word] = stochastic_for_current_word

            stochastic_for_current_word.add_count(adjacent_word)
            previous_word = current_word


    def generate_a_sentence(self):
        sentence = ""

        if len(self.words) == 0:
            return sentence

        # pick a random starting word
        current_markov_word = None

        while True:
            stochastic = self.words[current_markov_word]
            current_markov_word = stochastic.choose_random_word_from_frequency()
            # check: end of sentence
            if current_markov_word is None or current_markov_word in Markov.punctuation:
                # check: by a puncuation? if so, add it to the sentence
                if current_markov_word in Markov.punctuation:
                    sentence += " " + current_markov_word
                break
            else:
                sentence += " " + current_markov_word

        return sentence


if __name__ == '__main__':
    m = Markov("one fish two . fish . red . fish blue ! fish .".split())
    print(m.words)
    print(m.generate_a_sentence())
