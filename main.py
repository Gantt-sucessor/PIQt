import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtCore import QTimer

# Dicionário de usuários simulando um banco de dados
usuarios = {
    "j": "123"
}

# Tela inicial com carregamento
class InicioDesktop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("inicioDesktop.ui", self)

        # Espera 3 segundos (3000ms) e chama a função para abrir a próxima tela
        QTimer.singleShot(90, self.abrir_tela_principal)

    def abrir_tela_principal(self):
        self.tela_principal = TelaPrincipal()
        self.tela_principal.show()
        self.close()


# Tela de login
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
        
# Tela de escolha de cardápio

class EscolherCardapio(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("escolherCardapioReal2.ui", self)
        
        self.label_2.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_6.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_8.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.label_9.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        
        
        self.pushButton.clicked.connect(self.mostrar_pop_up)
        self.pushButton_9.clicked.connect(self.abrirPratoDoDia)
        
        
    def mostrar_pop_up(self):
        QMessageBox.information(self, "Sucesso", "Ação realizada com sucesso!")
        
    def abrirPratoDoDia(self):
        self.prato_do_dia = PratoDoDia()
        self.prato_do_dia.show()
        self.close()
        
class PratoDoDia(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pageProdutoReal.ui", self)
        
        
        self.pushButton_20.clicked.connect(self.voltar)

    def voltar(self):
        self.tela_anterior.show()
        self.close()
        
# Inicialização da aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = InicioDesktop()
    tela.show()
    sys.exit(app.exec_())
