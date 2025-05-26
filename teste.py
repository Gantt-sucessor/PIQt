from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget

class Tela1(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()
        botao = QPushButton("Ir para Tela 2")
        botao.clicked.connect(self.ir_para_tela2)
        layout.addWidget(botao)
        self.setLayout(layout)

    def ir_para_tela2(self):
        self.stacked_widget.setCurrentIndex(1)

class Tela2(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()
        botao = QPushButton("Voltar para Tela 1")
        botao.clicked.connect(self.voltar_para_tela1)
        layout.addWidget(botao)
        self.setLayout(layout)

    def voltar_para_tela1(self):
        self.stacked_widget.setCurrentIndex(0)

app = QApplication([])
stacked_widget = QStackedWidget()

tela1 = Tela1(stacked_widget)
tela2 = Tela2(stacked_widget)

stacked_widget.addWidget(tela1)
stacked_widget.addWidget(tela2)

stacked_widget.setCurrentIndex(0)
stacked_widget.show()
app.exec_()
