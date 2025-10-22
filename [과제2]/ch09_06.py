class BankAccount:
  def __init__(self, name, number, balance):
    self.name = name
    self.number = number
    self.balance = balance

  def deposit(self, addmoney):
    self.balance = self.balance + addmoney

  def withdraw(self, minusmoney):
    if self.balance < minusmoney:
      print('잔액부족')
    else:
      self.balance = self.balance - minusmoney

account = BankAccount('Kim', '123456789', 1000)
print('초기 잔고:', account.balance)
account.deposit(500)
print('저축 후 잔고:', account.balance)
account.withdraw(200)
print('인출 후 잔고:', account.balance)
account.withdraw(1500)
