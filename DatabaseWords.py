import random

'''It works like the brain of the chooser'''


class DatabaseWords:

    def __init__(self):
        self.words = ["banana", "bow", "weapon", "game", "brazil"]
        self.words_selected = []

    def select_word(self):
        """
        It's going to choose a word from words list

        :return: the selected word
        """
        if len(self.words) != 0:
            word_selected = random.choice(self.words)

            self.words_already_selected(word_selected)

            return word_selected

        self.reset_words_selected()

    def words_already_selected(self, word_selected):
        """
        Pop an item just selected, by your index, from the words list

        :param word_selected: the word selected in the "select_word" function
        """
        self.words_selected.append(word_selected)

        i = self.words.index(word_selected)

        self.words.pop(i)

    def reset_words_selected(self):
        """
        Reset list of words already selected to keep the game looping
        """
        self.words = self.words_selected

        self.words_selected = []
