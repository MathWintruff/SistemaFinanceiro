from PyQt5 import QtCore, QtGui, QtWidgets
from SistemaFinanceiro_UI import Ui_Form

#region Ui and UiFunctions

def AddConnects(self):
        #self.BtnConfirma.clicked.connect()
        self.TbwEmprestimos.itemSelectionChanged.connect(self.EnableConfirmButton)
        self.BtnProcura.clicked.connect(self.SetTableContent)
Ui_Form.AddConnects = AddConnects


def SetCmbItens(self):
    usuarios = GetUsuarios()
    for usuario in usuarios:
        self.CmbCredor.addItem(usuario)
        self.CmbDevedor.addItem(usuario)
Ui_Form.SetCmbItens = SetCmbItens
        

def SetTableContent(self):
    self.TxbSenha.setEnabled(False)
    self.BtnConfirma.setEnabled(False)
    emprestimos = GetEmprestimosRelacionados(self.CmbCredor.currentText(), self.CmbDevedor.currentText())
    self.TbwEmprestimos.setRowCount(len(emprestimos))

    for i, emprestimo in enumerate(emprestimos):
        credor = QtWidgets.QTableWidgetItem(emprestimo[0])
        credor.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        devedor = QtWidgets.QTableWidgetItem(emprestimo[1])
        devedor.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        data = QtWidgets.QTableWidgetItem(emprestimo[2])
        data.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        valor = QtWidgets.QTableWidgetItem(emprestimo[3])
        valor.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

        self.TbwEmprestimos.setItem(i, 0, credor)
        self.TbwEmprestimos.setItem(i, 1, devedor)
        self.TbwEmprestimos.setItem(i, 2, data)
        self.TbwEmprestimos.setItem(i, 3, valor)

    self.TbwEmprestimos
Ui_Form.SetTableContent = SetTableContent

def EnableConfirmButton(self):
    self.TxbSenha.setEnabled(True)
    self.BtnConfirma.setEnabled(True)
Ui_Form.EnableConfirmButton = EnableConfirmButton

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

#region DataFunctions
def GetUsuarios():
    return ["maria","joao","claudia","marcos","dede do dodo da dada di didi"]

def GetEmprestimosRelacionados(credor, devedor):
    emprestimos = GetEmprestimos()
    emprestimosRelacionados = []
    for emprestimo in emprestimos:
        if emprestimo[0] == credor and emprestimo[1] == devedor:
            emprestimosRelacionados.append(emprestimo)
    return emprestimosRelacionados

def GetEmprestimos():
    return [["maria", "joao", "diatal", 53], ["claudia", "marcos", "diaoutro", 23], ["maria", "marcos", "diatal", 53], ["maria", "joao", "diaoutro", 25], ["dede do dodo da dada di didi", "maria", "diatdfal", 535]]
#endregion

StartApplication()