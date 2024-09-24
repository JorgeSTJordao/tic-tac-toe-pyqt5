from data.DatabaseWords import DatabaseWords


class Play:
    """
    This class is where all game logic happens
    """

    def __init__(self, url):
        self.database_word = DatabaseWords(url)
        self.word_selected = ""
        self.letters_selected = ""
        self.letters = []
        self.message = ""
        self.life = 7

    def split_word_selected(self):
        return ["_" for _ in range(len(self.word_selected))]

    def is_letter_already_selected(self, letter):
        return letter in self.letters_selected

    def is_still_alive(self):
        return self.life == 0

    def is_letter_inside(self, letter):
        return letter in self.word_selected

    def select_word(self):
        """
        This function is going to get the word selected in database object
        """

        self.word_selected = self.database_word.query()
        self.letters = self.split_word_selected()

    def attempt(self, letter):
        """
        It's going to check if user win, lose, guessed wrong or right one of the letters

        - letter already selected
        - lose
        - win


        :param letter: The word chosen by user
        :return: the code that represents the state
        """

        if self.is_letter_already_selected(letter):
            self.message = "Word already selected"

        elif self.is_letter_inside(letter):

            if not ("_" in self.letters):
                self.message = "You win"
        else:
            self.life -= 1

            if self.is_still_alive():
                self.message = "You Lose"

    def insert_letter(self, letter):

        for i in range(len(self.word_selected)):

            if letter == self.word_selected[i]:
                self.letters[i] = letter

        self.letters_selected + letter

    def reset(self):
        """
        Restart the hangman
        """

        self.word_selected = ""
        self.letters_selected = ""
        self.letters = []
        self.life = 7
        self.message = ""
