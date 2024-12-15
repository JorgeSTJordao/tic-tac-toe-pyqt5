import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First PyQT5 App")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, heigth


if __name__ == "__main__":
    # Application object
    app = QApplication(sys.argv)

    # Creating the main window
    window = MainWindow()

    # Show the window
    window.show()
    # Run the event loop
    sys.exit(app.exec_())
