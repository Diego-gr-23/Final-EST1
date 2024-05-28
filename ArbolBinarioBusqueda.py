import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class NodoArbol:
    def __init__(self, valor, data=None):
        self.valor = valor
        self.data = data
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor, data=None):
        if not self.raiz:
            self.raiz = NodoArbol(valor, data)
        else:
            self._insertar_recursivo(self.raiz, valor, data)

    def _insertar_recursivo(self, nodo, valor, data):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor, data)
            else:
                self._insertar_recursivo(nodo.izquierda, valor, data)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor, data)
            else:
                self._insertar_recursivo(nodo.derecha, valor, data)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._min_valor(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        return nodo

    def _min_valor(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return nodo.data
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def listar(self):
        result = []
        self._inOrden(self.raiz, result)
        return result

    def _inOrden(self, nodo, result):
        if nodo:
            self._inOrden(nodo.izquierda, result)
            result.append((nodo.valor, nodo.data))
            self._inOrden(nodo.derecha, result)

    def generar_texto_arbol(self):
        texto = ""
        if self.raiz:
            texto = self._generar_texto_arbol_recursivo(self.raiz)
        return texto

    def _generar_texto_arbol_recursivo(self, nodo):
        if nodo is None:
            return ""
        texto_izquierda = self._generar_texto_arbol_recursivo(nodo.izquierda)
        texto_derecha = self._generar_texto_arbol_recursivo(nodo.derecha)
        return f"({texto_izquierda}) {nodo.valor} ({texto_derecha})"

class Ui_VentanaPrincipal6(object):
    def __init__(self):
        super().__init__()

        self.arbol_busqueda = ArbolBinarioBusqueda()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 800)

        # Fondo
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Fotos/Fondo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()

        # Explicación
        self.explicacion_label = QtWidgets.QLabel('Árbol de Búsqueda Binario: Insertar, Eliminar, Buscar, Listar, Dibujar y Exportar a Archivo de Texto',
                                                   parent=Form)
        self.explicacion_label.setGeometry(QtCore.QRect(50, 20, 1300, 50))
        self.explicacion_label.setStyleSheet("font-size: 14pt;")
        self.explicacion_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Recuadro blanco para la interacción del usuario
        self.recuadro = QtWidgets.QFrame(Form)
        self.recuadro.setGeometry(QtCore.QRect(50, 100, 1300, 250))
        self.recuadro.setStyleSheet("background-color: white; border: 2px solid black;")

        # Texto del recuadro blanco
        self.texto_recuadro = QtWidgets.QTextEdit(self.recuadro)
        self.texto_recuadro.setGeometry(QtCore.QRect(20, 20, 1260, 100))
        self.texto_recuadro.setReadOnly(True)

        # Campo de entrada para el valor
        self.valor_txt = QtWidgets.QLineEdit(self.recuadro)
        self.valor_txt.setGeometry(QtCore.QRect(20, 150, 200, 30))

        self.datos_txt = QtWidgets.QLineEdit(self.recuadro)
        self.datos_txt.setGeometry(QtCore.QRect(240, 150, 200, 30))

        # Botones
        self.insertar_btn = QtWidgets.QPushButton('Agregar Estudiante', self.recuadro)
        self.insertar_btn.setGeometry(QtCore.QRect(20, 200, 200, 30))

        self.eliminar_btn = QtWidgets.QPushButton('Eliminar Estudiante', self.recuadro)
        self.eliminar_btn.setGeometry(QtCore.QRect(240, 200, 200, 30))

        self.buscar_btn = QtWidgets.QPushButton('Buscar Estudiante', self.recuadro)
        self.buscar_btn.setGeometry(QtCore.QRect(460, 200, 200, 30))

        self.listar_btn = QtWidgets.QPushButton('Listar Estudiantes', self.recuadro)
        self.listar_btn.setGeometry(QtCore.QRect(680, 200, 200, 30))

        self.ver_arbol_btn = QtWidgets.QPushButton('Dibujar Árbol', self.recuadro)
        self.ver_arbol_btn.setGeometry(QtCore.QRect(900, 200, 200, 30))

        self.exportar_txt_btn = QtWidgets.QPushButton('Exportar a Texto', self.recuadro)
        self.exportar_txt_btn.setGeometry(QtCore.QRect(1120, 200, 200, 30))

        # Área para mostrar el árbol
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(50, 370, 1300, 400))
        self.graphicsScene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.graphicsScene)

        self.insertar_btn.clicked.connect(self.insertar)
        self.eliminar_btn.clicked.connect(self.eliminar)
        self.buscar_btn.clicked.connect(self.buscar)
        self.listar_btn.clicked.connect(self.listar)
        self.ver_arbol_btn.clicked.connect(self.ver_arbol)
        self.exportar_txt_btn.clicked.connect(self.exportar_txt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestión de Estudiantes"))

    # Functions
    def insertar(self):
        valor = self.valor_txt.text()
        datos = self.datos_txt.text()
        if valor.isdigit():
            valor = int(valor)
            self.arbol_busqueda.insertar(valor, datos)
            texto_arbol = self.arbol_busqueda.generar_texto_arbol()
            self.actualizar_texto_recuadro(f'Insertado: {valor}, Datos: {datos}\nÁrbol: {texto_arbol}')
            self.valor_txt.clear()
            self.datos_txt.clear()
            self.ver_arbol()

    def eliminar(self):
        valor = self.valor_txt.text()
        if valor.isdigit():
            valor = int(valor)
            self.arbol_busqueda.eliminar(valor)
            texto_arbol = self.arbol_busqueda.generar_texto_arbol()
            self.actualizar_texto_recuadro(f'Eliminado: {valor}\nÁrbol: {texto_arbol}')
            self.valor_txt.clear()
            self.datos_txt.clear()
            self.ver_arbol()

    def buscar(self):
        valor = self.valor_txt.text()
        if valor.isdigit():
            valor = int(valor)
            datos = self.arbol_busqueda.buscar(valor)
            estado = f"encontrado: {datos}" if datos else "no encontrado"
            texto_arbol = self.arbol_busqueda.generar_texto_arbol()
            self.actualizar_texto_recuadro(f'Estudiante {valor} {estado}\nÁrbol: {texto_arbol}')

    def listar(self):
        lista = self.arbol_busqueda.listar()
        texto_lista = "\n".join([f"ID: {valor}, Datos: {data}" for valor, data in lista])
        self.actualizar_texto_recuadro(f'Estudiantes en orden ascendente:\n{texto_lista}')

    def ver_arbol(self):
        self.graphicsScene.clear()
        if self.arbol_busqueda.raiz is not None:
            self.dibujar_nodo(self.arbol_busqueda.raiz, 650, 30, 300)

    def dibujar_nodo(self, nodo, x, y, dx):
        if nodo is not None:
            elipse = QtWidgets.QGraphicsEllipseItem(x, y, 30, 30)
            texto = QtWidgets.QGraphicsTextItem(str(nodo.valor), elipse)
            texto.setPos(x + 7, y + 5)
            self.graphicsScene.addItem(elipse)

            if nodo.izquierda:
                self.graphicsScene.addLine(x + 15, y + 30, x - dx + 15, y + 70)
                self.dibujar_nodo(nodo.izquierda, x - dx, y + 70, dx // 2)

            if nodo.derecha:
                self.graphicsScene.addLine(x + 15, y + 30, x + dx + 15, y + 70)
                self.dibujar_nodo(nodo.derecha, x + dx, y + 70, dx // 2)

    def actualizar_texto_recuadro(self, texto):
        texto_actual = self.texto_recuadro.toPlainText()
        nuevo_texto = f"{texto}\n{texto_actual}"
        self.texto_recuadro.setPlainText(nuevo_texto)

    def exportar_txt(self):
        lista = self.arbol_busqueda.listar()
        nomber = "Lista de estudaintes.txt"
        with open("estudiantes.txt", "w") as file:
            for valor, data in lista:
                file.write(f"ID: {valor}, Datos: {data}\n")
        self.actualizar_texto_recuadro("Archivo de texto exportado con éxito")

class VentanaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_VentanaPrincipal6()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
