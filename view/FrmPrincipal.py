# coding: utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QDialog, QMessageBox, QInputDialog
from PyQt5.uic import loadUi
from Controller.ProdutividadeCTR import ProdutividadeCTR

class FrmPrincipal(QMainWindow):
    def __init__(self):
        super(FrmPrincipal, self).__init__()
        loadUi('View/UI/produtividade.ui', self)

        self.buttonEnviarEmail.clicked.connect(self.gerar_email)

        self.radio_sim.clicked.connect(lambda: self.habilitar_desabilitar_campo())
        self.radio_nao.clicked.connect(lambda: self.habilitar_desabilitar_campo())



    def anexo_def(self):
        anexo = True
    def gerar_email(self):
        anexo = False
        if self.radio_sim.isChecked() == True:
            anexo = True

        chamados_atendidos = self.input_chamados_atendidos.toPlainText()
        total = len(chamados_atendidos.split("\n"))
        chamados_atendidos = chamados_atendidos.replace("\n", "<br>")

        chamados_n_atendidos = self.input_chamados_nao_atendidos.toPlainText()
        if (chamados_n_atendidos == ""):
            chamados_n_atendidos = "<br> segue anexo planilha <br>"
        chamados_n_atendidos = chamados_n_atendidos.replace("\n", "<br>")
        emails = "p630421@mail.caixa"
        emails_copias = "p535943@mail.caixa"

        ProdutividadeCTR.email_produtividade(anexo,chamados_atendidos,chamados_n_atendidos,emails,emails_copias,total)

    def habilitar_desabilitar_campo(self):
        if (self.radio_sim.isChecked() == True):
            self.input_chamados_nao_atendidos.setEnabled(False)
        else:
            self.input_chamados_nao_atendidos.setEnabled(True)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmPrincipal()
    widget.show()
    sys.exit(app.exec())