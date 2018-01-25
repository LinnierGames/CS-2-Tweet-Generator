import sys
sys.path.insert(0,"../4-exercies")

from stochastic import Stochastic

class Markov(object):

    def __init__(self, list_words=None):

        self.corpus = list_words
        self.words = {} # [String: Stochastic]

        # iterate corpus
        for index, current_word in enumerate(self.corpus):
            adjacent_word = None # None is equal to stop

            def get_adjacent_word():
                try:
                    return self.corpus[index + 1]
                except IndexError:
                    return None

            adjacent_word = get_adjacent_word()

            stochastic_for_current_word = None

            if current_word in self.words:
                stochastic_for_current_word = self.words[current_word]
            else:
                stochastic_for_current_word = Stochastic()
                self.words[current_word] = stochastic_for_current_word

            stochastic_for_current_word.add_count(adjacent_word)

        ## check if current_worrd is already in self.worlds
        ### add adjacent_word to the self.words[current_word]histogram

    def generate_a_sentense(self):
        pass


m = Markov("one fish two fish red fish blue fish".split())
for word, stochastic in m.words.items():
    print(word, stochastic.frequency_of_tokens())
