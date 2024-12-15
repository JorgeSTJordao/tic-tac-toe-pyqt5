import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals and Slots")
        self.setGeometry(100, 100, 400, 300)

        # Create a Button
        button = QPushButton("Click Me", self)

        # Connect the Button Click Signal to a Slot (Function)
        button.clicked.connect(self.on_button_click)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def on_button_click(self):
        print("Button was clicked!")



if __name__ == "__main__":
    # Application object
    app = QApplication(sys.argv)

    # Creating the main window
    window = MainWindow()

    # Show the window
    window.show()
    # Run the event loop
    sys.exit(app.exec_())
