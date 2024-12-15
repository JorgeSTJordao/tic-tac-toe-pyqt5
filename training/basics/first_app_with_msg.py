import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First PyQT5 App")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, heigth

        # First Widgets
        label = QLabel("Hello, World!", self)
        button = QPushButton("Click", self)

        # Arrange widgets in a layout
        layout = QVBoxLayout(label)
        layout.addWidget(button)

        # Creating a container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    # Application object
    app = QApplication(sys.argv)

    # Creating the main window
    window = MainWindow()

    # Show the window
    window.show()
    # Run the event loop
    sys.exit(app.exec_())
