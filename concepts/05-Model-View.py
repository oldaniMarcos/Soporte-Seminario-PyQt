from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtWidgets import QApplication, QListView
import sys

class NameModel(QAbstractListModel):
    def __init__(self, names=None):
        super().__init__()
        self.names = names or []
        
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.names[index.row()]

    def rowCount(self, index):
        return len(self.names)

app = QApplication(sys.argv)

with open("./project/styles.qss", "r") as f:
    app.setStyleSheet(f.read())

model = NameModel(["Nombre 1", "Nombre 2", "Nombre 3"])
view = QListView()
view.setWindowTitle('Patrón Model/View')
view.setModel(model)

view.show()
app.exec()