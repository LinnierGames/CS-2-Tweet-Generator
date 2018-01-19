from listogram import Listogram


class Stochastic(Listogram):

    def frequency_of_tokens(self):
        frequency = {}

        for token_key, token_value in self:
            max_number_entries = self.tokens

            frequency[token_key] = float(token_value) / float(max_number_entries)

        return frequency


str_sentence = "one fish two fish red fish blue fish"
arr_sentence = str_sentence.split()

stat = Stochastic(arr_sentence)

print(stat.frequency_of_tokens())