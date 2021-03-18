from PyQt5 import QtCore, QtGui, QtWidgets
from SistemaFinanceiro_UI import Ui_Form

#region Ui and UiFunctions

def AddConnects(self):
        self.BtnConfirma.clicked.connect(self.SetTableContent)
Ui_Form.AddConnects = AddConnects


def SetCmbItens(self):
    usuarios = GetUsuarios()
    for usuario in usuarios:
        self.CmbCredor.addItem(usuario)
        self.CmbDevedor.addItem(usuario)
Ui_Form.SetCmbItens = SetCmbItens
        

def SetTableContent(self):
    emprestimos = GetEmprestimosRelacionados(self.CmbCredor.currentText(), self.CmbDevedor.currentText())
    self.TbwEmprestimos.setRowCount(len(emprestimos))
    for i, emprestimo in enumerate(emprestimos):
        self.TbwEmprestimos.setItem(i, 0, QtWidgets.QTableWidgetItem(emprestimo[0]))
        self.TbwEmprestimos.setItem(i, 1, QtWidgets.QTableWidgetItem(emprestimo[1]))
        self.TbwEmprestimos.setItem(i, 2, QtWidgets.QTableWidgetItem(emprestimo[2]))
        self.TbwEmprestimos.setItem(i, 3, QtWidgets.QTableWidgetItem(str(emprestimo[3])))
    self.TbwEmprestimos
Ui_Form.SetTableContent = SetTableContent

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