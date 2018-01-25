
# counts_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])]

class Historgram_Of_Lists(list):

    def __init__(self, list_word=None):
        super(Historgram_Of_Lists, self).__init__()  # Initialize this as a new list
        self.tokens = 0
        self.types = 0

        # when an iteration of a search word and the loop breaks, the index is saved here
        self.__prev_index__ = None
        self.__prev_count__ = None

        if list_word is not None:
            for word in list_word:
                self.add_token(word)

    def add_token(self, word, count=1):
        # this list is always sorted by the count value, thus words with 1 frequency are at the first index and so on
        #

        def insert_token_at(index_to_insert):
            token = (1,[word])
            if index_to_insert is not None:
                self.insert(index, token)
            else:
                self.append(token)
            self.types += 1

        def append_token_at(index_to_append):
            pass

        # if list is empty

        if len(self) == 0:
            ## create a count of (1,[word])
            ## types++
            insert_token_at(0,word)
        else:
            ## iterate existing counts: to find word
            is_found_at_index = None
            is_found_at_count = None
            for index, list_count_n_list_of_words in enumerate(self):
                list_words_for_iterator = list_count_n_list_of_words[1]
                if word in list_words_for_iterator:
                    is_found_at_index = index
                    is_found_at_count = list_count_n_list_of_words[0]
                    break
            ### if word is found
            if is_found_at_index is not None:
                #### remove word from its original count
                list_og = self[is_found_at_index]
                index_of_word_in_og_list = list_og[1].index(word)
                list_og.pop(index_of_word_in_og_list)
                #### cleanup if count is empty of words
                if len(list_og[1]) == 0:
                    del self[is_found_at_index]

                new_count = is_found_at_count + count
                #### if new count does exist, append the word to the list
                if self.words_for_count(new_count) is not None:
                    new_index = self.__prev_index__ + 1
                    if new_index == len(self): # out of bounds, create a new element
                        insert_token_at(None, word)
                    list_adjacent_to_index = self[]
                #### if new count doesn't exist, create a count of (the_new_count, [word])

                ### else: word is not found
                #### does the count for (1,..) exists?
                ##### append word to the count of (1,..)
                #### else
                ##### create a count of (1,[word])
            # token++
            self.tokens += 1

    def words_for_count(self, count_to_find):
        for index, list_count_n_list_of_words in enumerate(self):
            count_for_iterator = list_count_n_list_of_words[0]
            if count_for_iterator == count_to_find:
                self.__prev_index__ = index
                self.__prev_count__ = list_count_n_list_of_words[0]

                return list_count_n_list_of_words[1]

        return None

    def count_for_word(self, word):
        for index, list_count_n_list_of_words in enumerate(self):
            words_for_iterator = list_count_n_list_of_words[1]
            if word in words_for_iterator:
                self.__prev_index__ = index
                self.__prev_count__ = list_count_n_list_of_words[0]

                return list_count_n_list_of_words[0]

        return None


str_sentence = "one fish two fish red fish four fish"
arr_sentence = str_sentence.split()

h = Historgram_Of_Lists(arr_sentence)
print(h.count_for_word("one"))
# print(h)


