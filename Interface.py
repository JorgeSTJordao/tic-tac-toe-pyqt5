from Hangman import Hangman


class Interface:
    def __init__(self):
        self.hangman = Hangman()

    def options(self):
        """
        Select an option from the home screen. It could be play or leave

        code list: [
            1: play the game
            2: leave the game
        ]

        :return: code from the list
        """
        print("SELECT AN OPTION")
        print("[1] - Play")
        print("[2] - Exit")

        option = int(input("R: "))

        if option == 1:
            self.hangman.select_word()
            self.play()

        print("Bye bye!")

    def play(self):
        """
        Show the main information to the user
        """
        while True:
            print(f"Letters selected: {self.hangman.letters_selected}")
            print(f"Life: {self.hangman.life}")

            print(f"{self.hangman.word_gamer}")

            letter_selected = input("Select a letter: ")

            value = self.hangman.attempt(letter_selected)

            if value == -1:
                self.hangman.reset()
                break
            elif value == 2:
                self.hangman.reset()
                break

        self.options()
