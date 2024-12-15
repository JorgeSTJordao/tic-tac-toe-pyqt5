from config import *


class Page1(QWidget):
    go_to_page2 = pyqtSignal()  # Signal to go to Page 2

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Page 1")

        layout = QVBoxLayout()

        button = QPushButton("Go to Page 2")
        button.clicked.connect(self.go_to_page2.emit)  # Emit signal to navigate to Page 2

        layout.addWidget(button)
        self.setLayout(layout)
