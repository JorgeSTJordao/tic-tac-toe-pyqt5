import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matrix Example")
        self.setGeometry(100, 100, 400, 400)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()  # Create a grid layout
        central_widget.setLayout(grid_layout)

        # Populate the grid with a 3x3 matrix of buttons
        for row in range(3):
            for col in range(3):
                button = QPushButton(f"Button {row+1}, {col+1}")  # Button with row/column label
                grid_layout.addWidget(button, row, col)  # Add button to the grid


# Main Application Loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
