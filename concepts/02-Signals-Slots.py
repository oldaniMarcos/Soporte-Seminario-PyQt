import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App")
        self.setContentsMargins(10, 10, 10, 10)

        button = QPushButton("Esto es un botón")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self):
        print("Botón presionado")

app = QApplication(sys.argv)

with open("./project/styles.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
window.show()

app.exec()