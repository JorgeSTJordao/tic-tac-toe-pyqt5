from DatabaseWords import DatabaseWords

life = len(["head", "body", "right arm", "left arm", "right leg", "left leg"])


class Hangman:
    def __init__(self):
        self.database_word = DatabaseWords()
        self.word = ""
        self.word_gamer = ""
        self.letters_selected = []
        self.life = life

    def select_word(self):
        self.word = self.database_word.select_word()
        self.word_gamer = ["_" for i in range(len(self.word))]
        return self.word_gamer

    def attempt(self, letter):
        if not ("_" in self.word_gamer):
            print("You win")
            return 2
        elif letter in self.letters_selected:
            print("Letter already selected")
            return 3

        if letter in self.word:
            for i in range(len(self.word)):

                if letter == self.word[i]:
                    self.word_gamer[i] = letter

            self.letters_selected.append(letter)

        else:
            self.life -= 1

            if self.life == 0:
                print("You Lose")
                return -1

            self.letters_selected.append(letter)

    def reset(self):
        self.word = ""
        self.word_gamer = ""
        self.letters_selected = []
        self.life = life
