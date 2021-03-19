from PyQt5 import QtCore, QtGui, QtWidgets
from SistemaFinanceiro_UI import Ui_Form
from DataClasses import *

#region UiFunctions

def AddConnects(self):
        self.BtnConfirma.clicked.connect(self.RegisterPayment)
        self.TbwEmprestimos.itemClicked.connect(self.EnableConfirmButton)
        self.BtnProcura.clicked.connect(self.SetTableContent)
Ui_Form.AddConnects = AddConnects


def SetCmbItens(self):
    usuarios = mainSystem.GetUsers()
    for usuario in usuarios:
        self.CmbCredor.addItem(usuario)
        self.CmbDevedor.addItem(usuario)
Ui_Form.SetCmbItens = SetCmbItens
        

def SetTableContent(self):
    self.TxbSenha.setEnabled(False)
    self.BtnConfirma.setEnabled(False)
    emprestimos = mainSystem.GetRelatedLoans(self.CmbCredor.currentText(), self.CmbDevedor.currentText())
    self.TbwEmprestimos.setRowCount(len(emprestimos))

    for i, emprestimo in enumerate(emprestimos):
        Primarikey = QtWidgets.QTableWidgetItem(emprestimo[0])
        Primarikey.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        credor = QtWidgets.QTableWidgetItem(emprestimo[1])
        credor.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        devedor = QtWidgets.QTableWidgetItem(emprestimo[2])
        devedor.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        data = QtWidgets.QTableWidgetItem(emprestimo[3])
        data.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        valor = QtWidgets.QTableWidgetItem(f"{emprestimo[4]} R$")
        valor.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

        self.TbwEmprestimos.setItem(i, 0, Primarikey)
        self.TbwEmprestimos.setItem(i, 1, credor)
        self.TbwEmprestimos.setItem(i, 2, devedor)
        self.TbwEmprestimos.setItem(i, 3, data)
        self.TbwEmprestimos.setItem(i, 4, valor)

Ui_Form.SetTableContent = SetTableContent

def EnableConfirmButton(self):
    self.TxbSenha.setEnabled(True)
    self.BtnConfirma.setEnabled(True)
Ui_Form.EnableConfirmButton = EnableConfirmButton

def RegisterPayment(self):
    if mainSystem.RegisterPayment(int(self.TbwEmprestimos.item(self.TbwEmprestimos.currentRow(),0).text()), self.TxbSenha.text()) == True:
        self.SetTableContent()
    self.TxbSenha.setText("")
Ui_Form.RegisterPayment = RegisterPayment

def ExecAllExtFunctions(self):
    self.AddConnects()
    self.SetCmbItens()
    self.SetTableContent()
Ui_Form.ExecAllExtFunctions = ExecAllExtFunctions

def StartApplication():
    import sys
    ApplicationInstance = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    UiDesign = Ui_Form()
    UiDesign.setupUi(Window)
    Window.show()
    UiDesign.ExecAllExtFunctions()
    sys.exit(ApplicationInstance.exec_())

#endregion

mainSystem = LoanSystem()
mainSystem.CreateBaseData()

StartApplication()