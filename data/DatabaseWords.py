import random

from data.WordApi import WordApi


class DatabaseWords:
    """
    This class works like the database or chooser
    """

    def __init__(self, url):
        self.word_api = WordApi(url)
        self.words = []

    def is_empty(self):
        return len(self.words) == 0

    def get_words(self):
        word_selected = random.choice(self.words)

        self.delete(word_selected)

        return random.choice(self.words)

    def query(self):
        """
        Select a word from words list

        :return: the selected word
        """

        if self.is_empty:
            self.create()

        return self.get_words()

    def create(self):
        """
        Reset list of words already selected to keep the game looping
        """

        self.words = self.word_api.request()
        self.query()

    def delete(self, word_selected):
        """
        Remove the item selected by your index, from the words list

        :param word_selected: A string word which represents the word selected in the "select_word" function
        """

        i = self.words.index(word_selected)
        self.words.pop(i)
