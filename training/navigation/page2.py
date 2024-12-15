from config import *


class Page2(QWidget):
    go_to_page1 = pyqtSignal()  # Signal to go to Page 1

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Page 2")
        layout = QVBoxLayout()

        button_to_page1 = QPushButton("Go to Page 1")
        button_to_page1.clicked.connect(self.go_to_page1.emit)  # Emit signal to navigate to Page 1

        layout.addWidget(button_to_page1)
        self.setLayout(layout)
