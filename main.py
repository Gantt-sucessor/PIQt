import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QTimer


class InicioDesktop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("inicioDesktop.ui", self)
        
        # Espera 3 segundos (3000ms) e chama a função para abrir a próxima tela
        QTimer.singleShot(3000, self.abrir_tela_principal)

    def abrir_tela_principal(self):
        self.tela_principal = TelaPrincipal()
        self.tela_principal.show()
        self.close()

usuarios = {
    "jogoperdi@gmail.com": "123",
    "mitsuki.koga@gmail.com": "12345"
}


class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Entrou na TelaPrincipal")  # Confirma que a função foi chamada
        uic.loadUi("loginDesktopReal3.ui", self)
        
        self.iniciarButton_2.clicked.connect(self.verificar_login)

    def verificar_login(self):
        email = self.emailLogin.text()
        senha = self.senhaLogin.text()
        
        
        if email in usuarios and usuarios[email] == senha:
            QMessageBox.information(self, "Login", "Login bem sucedido!")
        else:
            QMessageBox.warning(self, "Erro", "Email ou senha incorretos.")



# 🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬



# 🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬


# Inicialização do app
app = QApplication(sys.argv)
tela = InicioDesktop()
tela.show()
sys.exit(app.exec_())
