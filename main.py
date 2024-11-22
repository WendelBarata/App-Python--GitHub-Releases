from PySide6.QtWidgets import QApplication, QMainWindow
from ui_py.MainScreen import Ui_MainWindow


class MainScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setText("Version 1.0.0 by Wendel Barata")


if __name__ == "__main__":
    app = QApplication([])
    window = MainScreen()
    window.show()
    app.exec()
