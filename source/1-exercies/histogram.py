import string


def histogram(content):
    s= ""
    s.lower()
    content = content.translate(None, string.punctuation)
    content = content.replace('\n',' ')
    arr_content = content.split(" ")
    dic_histogram = {}

    for a_word in arr_content:
        key = a_word.lower()
        value = dic_histogram.get(key, None)
        if value is not None:
            dic_histogram[key] = value +1
        else:
            if a_word != "":
                dic_histogram[key] = 1

    return dic_histogram


def historgram_list(content):
    pass


def histogram_tuple(content):
    pass


def histogram_counts(content):
    pass


def write_histogram_dic_to_file(content):
    pass


def most_key_in_historgram(histogram):
    most_key = None

    for index, key in enumerate(histogram):
        if most_key is not None:
            most_value = histogram[most_key]
            value = histogram[key]
            if value > most_value:
                most_key = key
        else:
            most_key = key

    return most_key


def mean_in_histogram(histogram):
    sum = 0.0
    for value in histogram.viewvalues():
        sum += value

    return sum / len(histogram)


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histogram.get(word, 0)


file = open("book.txt", "rb")
str_content = file.read()
file.close()

histogram_value = histogram(str_content).dictionary

print("Here's the historgram:\n{}".format(histogram_value))

most_key = most_key_in_historgram(histogram_value)

print("Most key is '{}' at {}".format(most_key,histogram_value[most_key]))

print("There are {} different words".format(unique_words(histogram_value)))

mean_value = mean_in_histogram(histogram_value)

print("The mean of the histogram is {}".format(mean_value))

print("\"Mystery\" appears {} times".format(frequency("mystery",histogram_value)))
