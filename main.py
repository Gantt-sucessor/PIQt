import sys
import locale
import webbrowser
import urllib.parse
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QSpinBox, QLabel, QLineEdit, QPushButton, QRadioButton
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

usuarios = {
    "jogoperdi@gmail.com": "123"
}

class InicioDesktop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("inicioDesktop.ui", self)
        QTimer.singleShot(2000, self.abrir_tela_principal)

    def abrir_tela_principal(self):
        self.tela_principal = TelaPrincipal()
        self.tela_principal.show()
        self.close()

class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("loginDesktopReal3.ui", self)
        self.iniciarButton_2.clicked.connect(self.verificar_login)

    def verificar_login(self):
        email = self.emailLogin.text()
        senha = self.senhaLogin.text()
        if email in usuarios and usuarios[email] == senha:
            self.escolher_cardapio = EscolherCardapio()
            self.escolher_cardapio.show()
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Email ou senha incorretos.")

class EscolherCardapio(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("escolherCardapioReal2.ui", self)

        self.labelFoto = self.findChild(QLabel, "label_6")

        self.imagens_pratos = [
            "imagens/2f4f06e26d086fbebec60b36e742b72c.jpg",
            "imagens/75c28cc86dc7645614634b118364208a.jpg",
            "imagens/7107a12cc89f3b3b097da65e9f871773.jpg",
            "imagens/442d3c0f809abf5e6432e204165efc55.jpg",
            "imagens/9c773caaecaa2b3df24aa4a523805bc2.jpg"
        ]
        self.indice_imagem = 0

        self.atualizar_imagem()

        self.timer = QTimer()
        self.timer.timeout.connect(self.trocar_imagem)
        self.timer.start(2000)

        self.label_2.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_6.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.pushButton_9.clicked.connect(self.abrirPratoDoDia)

    def atualizar_imagem(self):
        pixmap = QPixmap(self.imagens_pratos[self.indice_imagem])
        pixmap = pixmap.scaled(
            self.labelFoto.width(),
            self.labelFoto.height(),
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )
        self.labelFoto.setPixmap(pixmap)

    def trocar_imagem(self):
        self.indice_imagem = (self.indice_imagem + 1) % len(self.imagens_pratos)
        self.atualizar_imagem()

    def abrirPratoDoDia(self):
        self.prato_do_dia = PratoDoDia()
        self.prato_do_dia.show()
        self.close()

class PratoDoDia(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pageProdutoReal.ui", self)
        self.finalizarPedidoButton.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self.quantidadeSpinBox: QSpinBox = self.findChild(QSpinBox, "spinBox")
        self.pushButton.clicked.connect(self.abrirTelaPagamento)

    def abrirTelaPagamento(self):
        quantidade = self.quantidadeSpinBox.value()
        total = round(quantidade * 19.90, 2)

        self.tela_pagamento = FinalizarPagamento(total)
        self.tela_pagamento.show()
        self.close()

class FinalizarPagamento(QMainWindow):
    def __init__(self, total):
        super().__init__()
        uic.loadUi("finalizarPagamento.ui", self)
        self.finalizarPagamento.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self.label_8: QLabel = self.findChild(QLabel, "label_8")
        total_formatado = locale.currency(total, grouping=True)
        self.label_8.setText(total_formatado)

        self.total = total

        self.confirmarButton = self.findChild(QPushButton, "pushButton")  

        self.confirmarButton.clicked.connect(self.finalizar_pedido)

    def finalizar_pedido(self):
        rua = self.findChild(QLineEdit, "nomeRuaLineEdit").text()
        cep = self.findChild(QLineEdit, "cepLineEdit").text()
        bairro = self.findChild(QLineEdit, "nomeBairroLineEdit").text()
        telefone = self.findChild(QLineEdit, "telefoneLineEdit").text()

        if not rua or not cep or not bairro or not telefone:
            QMessageBox.warning(self, "Campos obrigatórios", "Preencha todos os campos antes de finalizar o pedido.")
            return
        
        if self.findChild(QRadioButton, "dinheiroRadioButton").isChecked():
            forma_pagamento = "Dinheiro"
        elif self.findChild(QRadioButton, "cartaoRadioButton").isChecked():
            forma_pagamento = "Cartão"
        elif self.findChild(QRadioButton, "pixRadioButton").isChecked():
            forma_pagamento = "Pix"
        else:
            QMessageBox.warning(self, "Forma de pagamento", "Selecione uma forma de pagamento.")
            return

        QMessageBox.information(
            self,
            "Pedido confirmado",
            f"Total: {locale.currency(self.total, grouping=True)}\n"
            f"Forma de pagamento: {forma_pagamento}\n"
            f"Entrega em: {rua}, {bairro}, {cep}\n"
            f"Telefone: {telefone}\n"
            f"Previsão de entrega: 45 minutos."
        )

        resposta = QMessageBox.question(
            self,
            "Enviar por WhatsApp",
            "Deseja enviar os detalhes do pedido para o restaurante via WhatsApp?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resposta == QMessageBox.Yes:
            mensagem = (
                f"Novo pedido!\n"
                f"Total: {locale.currency(self.total, grouping=True)}\n"
                f"Forma de pagamento: {forma_pagamento}\n"
                f"Endereço: {rua}, {bairro}, {cep}\n"
                f"Telefone de contato: {telefone}"
            )

            mensagem_codificada = urllib.parse.quote(mensagem)

            numero = "67992367780"  
            url = f"https://wa.me/{numero}?text={mensagem_codificada}"

            webbrowser.open(url)

        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = InicioDesktop()
    tela.show()
    sys.exit(app.exec_())
