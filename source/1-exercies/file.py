def collect_words_in_file(file_path="/usr/share/dict/words"):
    """
    opens a file by the given file_path and reads from top to bottom of file
    :param file_path: file to be read as read-only, if none is given, open the words file in the user directory
    :return: complete content of open file
    """
    f_words = open(file_path, "rb")
    words = f_words.read()
    f_words.close()

    return words
