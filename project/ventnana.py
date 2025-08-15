#Generar una app con una barra lateral que me permita navegar entre diferentes páginas. El proyecto usará pyqt6

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QWidget, QLabel, QDockWidget,QListWidget
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit, QGridLayout
from PyQt6.QtWidgets import QTextEdit, QFileDialog, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QAction, QKeySequence
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.create_sidebar()
        
    def initialize_ui(self):
        self.setWindowTitle("Aplicación con Barra Lateral")
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(self.crear_pagina_inicial("Bienvenido a la Página Principal"))
        self.create_action()
        self.create_menu()
        self.show()

    def create_sidebar(self):
        self.lista = QListWidget()
        self.lista.addItem("Proyecto 1")
        self.lista.addItem("Proyecto 2")
        self.lista.addItem("Proyecto 3")

        self.lista.itemClicked.connect(self.cambiar_pagina)
        self.lista.setFixedWidth(150)

        self.dock_list = QDockWidget("Navegación", self)
        self.dock_list.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        self.dock_list.setWidget(self.lista)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_list)

    def cambiar_pagina(self, item):
        pagina = item.text()
        if pagina == "Proyecto 1":
            self.setCentralWidget(self.crear_proyecto_uno("Esta es la Página 1"))
        elif pagina == "Proyecto 2":
            self.setCentralWidget(self.crear_proyecto_dos("Esta es la Página 2"))
        elif pagina == "Proyecto 3":
            self.setCentralWidget(self.crear_proyecto_tres("Esta es la Página 3"))
    
    def crear_pagina_inicial(self, texto):
        pagina = QWidget()
        layout = QVBoxLayout()
        label = QLabel(texto)
        layout.addWidget(label)
        pagina.setLayout(layout)
        return pagina

    def create_action(self):
        self.barra = QAction("Barra", self, checkable=True)
        self.barra.setChecked(True)
        self.barra.setShortcut(QKeySequence("Ctrl+l"))
        self.barra.setStatusTip("Muestra u oculta la barra lateral")
        self.barra.triggered.connect(self.barra_lateral)
        

    def create_menu(self):
        self.menuBar()
        menu_vista = self.menuBar().addMenu("Opciones")
        menu_vista.addAction(self.barra)

    def barra_lateral(self):
        if self.barra.isChecked():
            self.dock_list.show()
        else:
            self.dock_list.hide()

    #El proyecto uno debe ser una calculadora simple
    def crear_proyecto_uno(self, texto):
        pagina = QWidget()
        layout = QVBoxLayout()

        # Campo de texto para mostrar el resultado
        self.resultado = QLineEdit()
        self.resultado.setReadOnly(True)
        self.resultado.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.resultado.setFixedHeight(50)
        layout.addWidget(self.resultado)

        # Botones de la calculadora
        botones = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
        '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
        '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
        '0': (3, 0), 'C': (3, 1), '=': (3, 2), '+': (3, 3),
        }

        grid_layout = QGridLayout()
        for texto_boton, posicion in botones.items():
            boton = QPushButton(texto_boton)
            boton.setFixedSize(50, 50)
            boton.clicked.connect(self.manejar_click_boton)
            grid_layout.addWidget(boton, *posicion)

        layout.addLayout(grid_layout)
        pagina.setLayout(layout)
        return pagina

    def manejar_click_boton(self):
        boton = self.sender()
        texto = boton.text()

        if texto == 'C':
            self.resultado.clear()
        elif texto == '=':
            try:
                expresion = self.resultado.text()
                resultado = eval(expresion)  # Evalúa la expresión matemática
                self.resultado.setText(str(resultado))
            except Exception:
                self.resultado.setText("Error")
        else:
            self.resultado.setText(self.resultado.text() + texto)

    #El proyecto dos debe ser un bloc de notas simple
    def crear_proyecto_dos(self, texto):
        pagina = QWidget()
        layout = QVBoxLayout()

        # Área de texto para el bloc de notas
        self.text_area = QTextEdit()
        layout.addWidget(self.text_area)

        # Botones para guardar y cargar
        botones_layout = QHBoxLayout()

        boton_guardar = QPushButton("Guardar")
        boton_guardar.clicked.connect(self.guardar_texto)
        botones_layout.addWidget(boton_guardar)

        boton_cargar = QPushButton("Cargar")
        boton_cargar.clicked.connect(self.cargar_texto)
        botones_layout.addWidget(boton_cargar)

        layout.addLayout(botones_layout)
        pagina.setLayout(layout)
        return pagina

    def guardar_texto(self):
        # Abrir un cuadro de diálogo para guardar el archivo
        #opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "Archivos de Texto (*.txt);;Todos los Archivos (*)")
        if archivo:
            with open(archivo, 'w', encoding='utf-8') as file:
                file.write(self.text_area.toPlainText())

    def cargar_texto(self):
        # Abrir un cuadro de diálogo para cargar un archivo
        #opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "Archivos de Texto (*.txt);;Todos los Archivos (*)")
        if archivo:
            with open(archivo, 'r', encoding='utf-8') as file:
                self.text_area.setPlainText(file.read())

    #El proyecto tres debe ser un visor de imágenes simple
    def crear_proyecto_tres(self, texto):
        pagina = QWidget()
        layout = QVBoxLayout()

        # Etiqueta para mostrar la imagen
        self.imagen_label = QLabel("No se ha cargado ninguna imagen")
        self.imagen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.imagen_label)

        # Botón para cargar la imagen
        boton_cargar_imagen = QPushButton("Cargar Imagen")
        boton_cargar_imagen.clicked.connect(self.cargar_imagen)
        layout.addWidget(boton_cargar_imagen)

        pagina.setLayout(layout)
        return pagina

    def cargar_imagen(self):
        # Abrir un cuadro de diálogo para seleccionar una imagen
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir Imagen", "", "Archivos de Imagen (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los Archivos (*)")
        if archivo:
            pixmap = QPixmap(archivo)
            self.imagen_label.setPixmap(pixmap.scaled(self.imagen_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("WindowsVista") #Alternativas Fusion, Windows, WindowsVista, MacOS
    ventana = VentanaPrincipal()
    sys.exit(app.exec())