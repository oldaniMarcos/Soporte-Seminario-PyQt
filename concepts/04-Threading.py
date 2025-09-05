import sys, time
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

# Worker
class Worker(QThread):
    finished = pyqtSignal(str)   # señal para avisar cuando termina

    def run(self):
        time.sleep(3)
        self.finished.emit("Tarea completada")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo con Threads")

        self.label = QLabel("Esperando...")
        self.button = QPushButton("Iniciar tarea")
        self.button.clicked.connect(self.start_task)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_task(self):
        self.label.setText("Trabajando...")
        self.button.setEnabled(False)

        # crear y arrancar el hilo
        self.worker = Worker()
        self.worker.finished.connect(self.task_done)
        self.worker.start()

    def task_done(self, message):
        self.label.setText(message)
        self.button.setEnabled(True)

app = QApplication(sys.argv)

with open("./project/styles.qss", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
window.show()
app.exec()