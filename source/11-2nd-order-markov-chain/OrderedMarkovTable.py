import sys
import re

sys.path.insert(0, "../4-exercies")
from stochastic import Stochastic

sys.path.insert(0, "../")
from hashtable import HashTable


class OrderedMarkovChain(object):
    end_punctuation = [".","?","!"]

    def __init__(self, words, order):
        self.corpus = re.findall(r"[\w']+|[.,!?;]", words)
        self.words = HashTable(32)

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

            # check: at beginning of sentence, create/append current_word to self.words[None]
            if index == 0 or previous_word in OrderedMarkovChain.end_punctuation:
                stochastic_for_beginning_of_sentence = None
                try:
                    stochastic_for_beginning_of_sentence = self.words[None]
                except KeyError:
                    # stochastic for None is not made, so make one
                    stochastic_for_beginning_of_sentence = Stochastic()
                    self.words[None] = stochastic_for_beginning_of_sentence

                stochastic_for_beginning_of_sentence.add_count(current_word)

            # grab adjacent word, can be None to represent end of the sentence
            adjacent_word = get_adjacent_word()

            # if current_word is an ending puncuation, then adjacent_word is None
            if current_word in OrderedMarkovChain.end_punctuation:
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

        current_markov_word = None

        while True: # do-while
            stochastic = self.words[current_markov_word]
            current_markov_word = stochastic.choose_random_word_from_frequency()

            # check: end of sentence
            if current_markov_word is None or current_markov_word in OrderedMarkovChain.end_punctuation:
                # check: by a puncuation? if so, add it to the sentence
                if current_markov_word in OrderedMarkovChain.end_punctuation:
                    sentence += current_markov_word
                break
            else:
                sentence += " " + current_markov_word

        return sentence


if __name__ == '__main__':
    m = OrderedMarkovChain("one fish two . fish . red . fish blue ! fish", 1)
    print(m.generate_a_sentence())