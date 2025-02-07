class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"пополненный баланас: {self.balance} тг")
        else:
            print("счет на балансе должен быть положительным")
        
    def withdraw(self, amount): #снимаем
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"сняли {amount} тг, новый баланс: {self.balance} тг")
            else:
                print("недостаточно средств")
        else:
            print("сумма снятия должна быть положительной!!")
            
account = Account("User")
account.deposit(27500)
account.withdraw(13000)
account.withdraw(15000)
account.deposit(-200)
                