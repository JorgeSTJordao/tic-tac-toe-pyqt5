from config import *
from page1 import Page1
from page2 import Page2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigation")
        self.setGeometry(100, 100, 600, 400)

        # QStackWdiget to hold pages
        self.stacked_widget = QStackedWidget()

        # Instances
        self.page1 = Page1()
        self.page2 = Page2()

        # Add pages to QStackWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Connect pages by signals (navigation)
        self.page1.go_to_page2.connect(self.show_page2)
        self.page2.go_to_page1.connect(self.show_page1)

        # Central widget
        self.setCentralWidget(self.stacked_widget)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)

    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)


# Main Application Loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())