# 🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from model.produto import Produto
from controller.globals import carrinho
from view.inicio_desktop import inicio_desktop

class ProdutoPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/pageProduto.ui", self)

        self.produto = Produto("Macarrão com almôndegas", "Massa artesanal com molho sugo", 29.90)

    self.contadorMaisButton.clicked.connect(self.incrementar)
    self.contadorMenosButton.clicked.connect(self.decrementar)
    self.adicionarAoCarrinhoButton.clicked.connect(self.adicionarAoCarrinho)
    self.finalizarPedido.clicked.connect(self.voltarInicio)
        self.atualizarInterface()
    
    def atualizarInterface(self):
        self.findChild(QWidget, "labelQuantidade").setText(str(self.produto.quantidade))

    def incrementar(self):
        self.produto.aumentarQuantidade()
        self.atualizarInterface()

    def decrementar(self):
        self.produto.diminuirQuantidade()
        self.atualizarInterface()

    def adicionarAoCarrinho(self):
        carrinho.append(self.produto)
        QMessageBox.information(self, "carrinho",f"{self.produto.nome} adicionado ao carrinho!")

    def finalizarPedido(self):
        total = sum(p.calcularTotal() for p in carrinho)
        QMessageBox.information(self, "Pedido",f"Total do pedido: R${total:.2f}")

    def valorInicio(self):
        self.close()
        self.inicio = inicio_desktop()
        self.inicio.show()

# 🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬🚬