from Hangman import Hangman


class Interface:
    def __init__(self):
        self.hangman = Hangman()

    def options(self):

        option = int(input("""
            Select an option:
            [1] - Play 
            [2] - Exit
        """))

        if option == 1:
            self.hangman.select_word()
            return 1

        return 2

    def play(self):
        while True:
            print(f"Letters selected: {self.hangman.letters_selected}")
            print(f"Life: {self.hangman.life}")

            print(f"{self.hangman.word_gamer}")

            letter_selected = input("Select a letter: ")

            value = self.hangman.attempt(letter_selected)

            if value == -1:
                break
            elif value == 2:
                break

