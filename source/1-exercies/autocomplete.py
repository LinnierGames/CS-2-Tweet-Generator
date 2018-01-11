import file, sys

# Usage: python autocomplete.py Hell
# Helladian
# Helladic
# Helladotherium
# Helleborine
# Helleborus
# Hellelt
# Hellen
# ...

collection_words = file.collect_words_in_file()
arr_words = collection_words.split("\n")
str_autocomplete_to = sys.argv[1]

arr_possible_words_to_autocomplete = []
for term in arr_words:
    if term.startswith(str_autocomplete_to):
        arr_possible_words_to_autocomplete.append(term)

str_possible_words_to_autocomplete = "\n".join(arr_possible_words_to_autocomplete)

print str_possible_words_to_autocomplete
