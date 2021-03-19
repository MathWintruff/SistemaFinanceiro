class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def GetName(self):
        return str(self.name)

    def ConfirmPassword(self, password):
        return True if self.password == password else False

##-----------------------------------------------------------------------------------------------------------------------------##

class Loan:
    def __init__(self, creditor, debtor, data = "01/01/2000", price = 0):
        self.creditor = creditor
        self.debtor = debtor
        self.data = data
        self.price = price

    def IsRelated(self, creditorName, debtorName):
        return True if self.creditor.GetName() == creditorName and self.debtor.GetName() == debtorName else False
    
    def GetData(self):
        return str(self.data)

    def GetPrice(self):
        return str("{:.2f}".format(self.price))

    def GetAjustedPrice(self):
        return str("{:.2f}".format(self.price + 2))

##-----------------------------------------------------------------------------------------------------------------------------##

class LoanSystem:
    def __init__(self):
        self.users = list()
        self.loans = list()

    def RegisterUser(self, name, password):
        user = User(name, password)
        self.users.append(user)

    def RegisterLoan(self, creditor, debtor, data = "01/01/2000", price = 0):
        loan = Loan(creditor, debtor, data, price)
        self.loans.append(loan)

    def GetRelatedLoans(self, creditorName, debtorName):
        relatedLoans = list()
        for i,loan in enumerate(self.loans):
            if loan.IsRelated(creditorName, debtorName):
                loanReference = [str(i), loan.creditor.GetName(), loan.debtor.GetName(), loan.GetData(), loan.GetPrice(), loan.GetAjustedPrice()]
                relatedLoans.append(loanReference)
        return relatedLoans

    def GetUsers(self):
        users = list()
        for user in self.users:
            users.append(user.GetName())
        return users
         
    def RegisterPayment(self, loanIndex, creditorPassword):
        if self.loans[loanIndex].creditor.ConfirmPassword(creditorPassword):
            del self.loans[loanIndex]
            return True
        else: return False

    def CreateBaseData(self):
        joao = self.RegisterUser("Joao","123")
        maria = self.RegisterUser("Maria","456")
        antonio = self.RegisterUser("Antonio","789")
        jose = self.RegisterUser("Jose","147")
        Carlos = self.RegisterUser("Carlos","458")
        Daniela = self.RegisterUser("Daniela","753")

        self.RegisterLoan(self.users[0], self.users[1],"03/09/2011",10.00)
        self.RegisterLoan(self.users[2], self.users[1],"04/09/2011",12.00)
        self.RegisterLoan(self.users[2], self.users[3],"04/09/2011",5.00)
        self.RegisterLoan(self.users[2], self.users[1],"05/09/2011",3.00)
        self.RegisterLoan(self.users[3], self.users[1],"05/09/2011",18.00)

        self.RegisterLoan(self.users[0], self.users[1],"09/09/2011",6.00)
        self.RegisterLoan(self.users[2], self.users[1],"10/09/2011",25.00)
        self.RegisterLoan(self.users[2], self.users[3],"10/09/2011",32.00)
        self.RegisterLoan(self.users[2], self.users[1],"12/09/2011",67.00)
        self.RegisterLoan(self.users[3], self.users[1],"15/09/2011",83.54)

        self.RegisterLoan(self.users[4], self.users[5],"20/09/2011",15.50)
        self.RegisterLoan(self.users[4], self.users[5],"21/09/2011",25.32)
        self.RegisterLoan(self.users[5], self.users[4],"20/09/2011",120.00)
        self.RegisterLoan(self.users[5], self.users[4],"22/09/2011",200.00)
        self.RegisterLoan(self.users[5], self.users[4],"27/09/2011",125.00)