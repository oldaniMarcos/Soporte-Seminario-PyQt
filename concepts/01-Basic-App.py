import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App")
        self.setContentsMargins(10, 10, 10, 10)

        button = QPushButton("Esto es un botón")

        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(button)

app = QApplication(sys.argv)

with open("./project/styles.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
window.show()

app.exec()