import random

from data.WordApi import WordApi


class DatabaseWords:
    """
    This class works like the database or chooser
    """

    def __init__(self):
        self.word_api = WordApi()
        self.words = []

    def select_word(self):
        """
        It's going to choose a word from words list

        :return: the selected word
        """

        if len(self.words) == 0:
            self.add_new_words()

        word_selected = random.choice(self.words)

        self.pop_word_selected(word_selected)

        return word_selected


    def pop_word_selected(self, word_selected):
        """
        Remove the item selected by your index, from the words list

        :param word_selected: A string word which represents the word selected in the "select_word" function
        """

        i = self.words.index(word_selected)
        self.words.pop(i)

    def add_new_words(self):
        """
        Reset list of words already selected to keep the game looping
        """

        self.words = self.word_api.get_words()

        self.select_word()
