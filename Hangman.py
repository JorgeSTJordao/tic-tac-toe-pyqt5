from DatabaseWords import DatabaseWords

"""
A representation of the man body (constant)
"""
life = len(["head", "body", "right arm", "left arm", "right leg", "left leg"])


class Hangman:
    def __init__(self):
        self.database_word = DatabaseWords()
        self.word = ""
        self.word_gamer = ""
        self.letters_selected = []
        self.life = life

    def select_word(self):
        """
        This function is going to get the word selected in database object

        :return: the word that user can see on screen
        """
        self.word = self.database_word.select_word()
        self.word_gamer = ["_" for i in range(len(self.word))]
        return self.word_gamer

    def attempt(self, letter):
        """
        It's going to check if user win, lose, guessed wrong or right one of the letters

        code list: [
            -1: lose
            2: win
            3: word already selected
        ]

        :param letter: The word chosen by user
        :return: the code that represents the state
        """
        if letter in self.letters_selected:
            print("Letter already selected")
            return 3
        elif letter in self.word:
            for i in range(len(self.word)):

                if letter == self.word[i]:
                    self.word_gamer[i] = letter

            if not ("_" in self.word_gamer):
                print("You win")
                return 2

            self.letters_selected.append(letter)
        else:
            self.life -= 1

            if self.life == 0:
                print("You Lose")
                return -1

            self.letters_selected.append(letter)

    def reset(self):
        """
        Restart the hangman
        """
        self.word = ""
        self.word_gamer = ""
        self.letters_selected = []
        self.life = life
