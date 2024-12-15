import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QMessageBox, QDesktopWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

win_matches = ["012", "345", "678", "036", "147", "258", "048", "246"]


class TicTacToeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 400, 400)

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()  # Main vertical layout
        central_widget.setLayout(self.main_layout)

        self.center_window()

        # Add turn indicator label
        self.turn_label = QLabel("X's Turn")
        self.turn_label.setFont(QFont("Arial", 15))
        self.turn_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.turn_label)

        # Create grid layout for the Tic-Tac-Toe board
        self.grid_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_layout)

        # Create the game board
        self.create_board()

        # Define each turn
        self.turn = True

        # How many matches already have
        self.match_number = 0

        # Each match
        self.players_match = {"X": "", "O": ""}

    def center_window(self):
        # Center the window on the screen
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.frameGeometry()

        # Center point of screen
        screen_center = screen_geometry.center()

        # Move the window to the screen's center
        window_geometry.moveCenter(screen_center)
        self.move(window_geometry.topLeft())

    def create_board(self):
        self.buttons = []  # Store buttons for later reference

        for row in range(3):
            row_buttons = []
            for col in range(3):
                # Create a button
                button = QPushButton("")
                button.setFont(QFont("Arial", 40))  # Set large font size for the "X"
                button.setFixedSize(100, 100)  # Make the button a large square
                button.clicked.connect(lambda _, r=row, c=col: self.mark_x_or_o(r, c))

                # Add button to the grid
                self.grid_layout.addWidget(button, row, col)
                row_buttons.append(button)

            self.buttons.append(row_buttons)

    def show_message(self, title, text):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.Yes)

        # Check user response
        response = msg_box.exec_()

        if response == QMessageBox.Yes:
            self.reset_screen()
        else:
            self.close()

    def mark_x_or_o(self, row, col):
        button = self.buttons[row][col]
        player = ""

        if button.text() == "":  # If the square is empty
            if self.turn:
                button.setText("X")  # Mark with "X"
                player = "X"  # Matches to check are from "X"
                self.players_match["X"] += str(row * 3 + col)
                self.turn = False
                self.turn_label.setText("O's Turn")  # Update turn label
            else:
                button.setText("O")  # Mark with "O"
                player = "O"  # Matches to check are from "O"
                self.players_match["O"] += str(row * 3 + col)
                self.turn = True
                self.turn_label.setText("X's Turn")  # Update turn label

        # Wait until we have four matches
        if self.match_number < 4:
            pass
        else:
            for win in win_matches:
                # If true, someone wins
                if all(char in self.players_match[player] for char in win):
                    self.show_message(f"{player} has won!", "Do you want to restart?")
                    return  # Exit the function once the game is over

        self.match_number += 1

        if self.match_number == 9:
            self.show_message("DRAW", "Do you want to restart?")

    def reset_screen(self):
        # Reset everything to initial state
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.setText("")

        # Reset game state variables
        self.turn = True
        self.match_number = 0
        self.players_match = {"X": "", "O": ""}
        self.turn_label.setText("X's Turn")  # Reset turn label


# Main Application Loop
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a 3x3 matrix window with labels and input fields
    window = TicTacToeWindow()
    window.show()

    sys.exit(app.exec_())
