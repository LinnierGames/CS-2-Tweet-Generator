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
        self.order = order

        # iterate corpus
        previous_element = None
        previous_element_list = None
        if len(self.corpus) < self.order + 1 and self.order > 0:
            print("invalid corpus")
        else:
            max_iteration = len(self.corpus) - self.order + 1
            for index in range(0, max_iteration):
                adjacent_index = index + self.order
                current_element_list = self.corpus[index:adjacent_index]
                current_element = ' '.join(current_element_list)

                # check: at beginning of sentence, create/append current_word to self.words[None]
                if index == 0 or previous_element_list[0] in OrderedMarkovChain.end_punctuation:
                    stochastic_for_beginning_of_sentence = None
                    try:
                        stochastic_for_beginning_of_sentence = self.words[None]
                    except KeyError:
                        # stochastic for None is not made, so make one
                        stochastic_for_beginning_of_sentence = Stochastic()
                        self.words[None] = stochastic_for_beginning_of_sentence

                    stochastic_for_beginning_of_sentence.add_count(current_element)

                # grab adjacent word, can be None to represent end of the sentence

                def get_adjacent_word():
                    try:
                        adjacent_word = self.corpus[adjacent_index]
                        temp_list = current_element_list[1:] # current_element without the first index
                        temp_element = ' '.join(temp_list)

                        return adjacent_word
                    except IndexError:
                        # end of list_words, thus end of sentence
                        return None

                adjacent_element = get_adjacent_word()
                print(current_element, "->{}".format(adjacent_element))

                # if current_word is an ending puncuation, then adjacent_word is None
                if current_element_list[-1] in OrderedMarkovChain.end_punctuation:
                    adjacent_element = None
                    # continue

                stochastic_for_current_word = None
                if current_element in self.words:
                    stochastic_for_current_word = self.words[current_element]
                else:
                    stochastic_for_current_word = Stochastic()
                    self.words[current_element] = stochastic_for_current_word

                stochastic_for_current_word.add_count(adjacent_element)
                previous_element = current_element
                previous_element_list = current_element_list

    def generate_a_sentence(self):
        sentence = ""

        if len(self.words) == 0:
            return sentence

        current_markov_element = None

        # start sentence with None frequency
        current_markov_element = self.words[None].choose_random_word_from_frequency()
        sentence += current_markov_element

        prev = current_markov_element.split()[-2]
        curr = current_markov_element.split()[-1]

        while True:  # do-while
            key = prev + " " + curr
            stochastic = self.words[key]
            current_markov_element = stochastic.choose_random_word_from_frequency()

            # check: end of sentence
            if current_markov_element is None or current_markov_element in OrderedMarkovChain.end_punctuation:
                # check: by a puncuation? if so, add it to the sentence
                if current_markov_element in OrderedMarkovChain.end_punctuation:
                    sentence += current_markov_element
                break
            else:
                pass
            sentence += " " + current_markov_element

            prev = curr
            curr = current_markov_element

        return sentence


if __name__ == '__main__':
    m = OrderedMarkovChain("one fish two fish red fish. blue fish.", 2)
    print(m.words)
    print("Sentence: {}".format(m.generate_a_sentence()))