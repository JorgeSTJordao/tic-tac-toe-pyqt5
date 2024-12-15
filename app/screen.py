import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QFont

win_matches = ["012", "345", "678", "036", "147", "258", "048", "246"]


class TicTacToeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 400, 400)

        # Central widget and grid layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.grid_layout = QGridLayout()
        central_widget.setLayout(self.grid_layout)

        self.center_window()

        # Create a 3x3 grid of buttons
        self.create_board()

        # Define each turn
        self.turn = True

        # How many matches already have
        self.match_number = 0

        # Each match
        self.players_match = {"X": "", "O": ""}

    def center_window(self):
        # Center of the window

        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.frameGeometry()

        # Center point of screen
        screen_center = screen_geometry.center()

        # Move the windows to the screen's center
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
                button.setFixedSize(100, 100)      # Make the button a large square
                button.clicked.connect(lambda _, r=row, c=col: self.mark_x_or_o(r, c))

                # Add button to the grid
                self.grid_layout.addWidget(button, row, col)
                row_buttons.append(button)

            self.buttons.append(row_buttons)

    def show_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("GAME OVER")
        msg_box.setText("Do you want to restart?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.Yes)

        # Check user response
        response = msg_box.exec_()

        if response == QMessageBox.Yes:
            self.reset_screen()

    def mark_x_or_o(self, row, col):
        button = self.buttons[row][col]
        player = ""

        if button.text() == "":  # If the square is empty

            if self.turn:
                button.setText("X")  # Mark with "X"
                player = "X"  # Matches to check is from "X"

                self.players_match["X"] += str(row * 3 + col)
                self.turn = False
            else:
                button.setText("O")  # Mark with "O"
                player = "O"  # Matches to check is from "O"

                self.players_match["O"] += str(row * 3 + col)
                self.turn = True

        # Wait until we have four matches
        if self.match_number < 4:
            self.match_number += 1
        else:
            for win in win_matches:
                # If is true, someone wins
                if all(char in self.players_match[player] for char in win):
                    self.show_message()
                    break

    def reset_screen(self):
        # Reset everything to initial state

        # Clear all button texts
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.setText("")

        # Reset game state variables
        self.turn = True
        self.match_number = 0
        self.players_match = {"X": "", "O": ""}


# Main Application Loop
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a 3x3 matrix window with labels and input fields
    rows, cols = 3, 3
    window = TicTacToeWindow()
    window.show()

    sys.exit(app.exec_())