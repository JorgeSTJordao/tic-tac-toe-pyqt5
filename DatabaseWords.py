import random

'''It works like the brain of the chooser'''


class DatabaseWords:

    def __init__(self):
        self.words = ["banana", "bow", "weapon", "game", "brazil"]
        self.words_selected = []

    '''Return a selected word from the main list of words'''

    def select_word(self):
        if len(self.words) != 0:
            word_selected = random.choice(self.words)

            self.words_already_selected(word_selected)

            return word_selected

        self.reset_words()

    '''Pop an item already selected from the main list'''

    def words_already_selected(self, word_selected):
        self.words_selected.append(word_selected)

        i = self.words.index(word_selected)

        self.words.pop(i)

    '''Reset list of words already selected to keep the game in loop'''

    def reset_words(self):
        self.words = self.words_selected

        self.words_selected = []
