class BankAccount:
    def __init__(self,owner,__balance = 0):
        self.owner = owner
        self.__balance = __balance
        print(f'{self.owner} 계좌가 생성되었습니다.')

    def get_balance(self):
        print(self.__balance)

    def get_balance(self,amount = 0):
        if amount >=0:
            self.__balance = amount

    def deposit(self, pmoney):
        if pmoney>=0:
            self.__balance = self.__balance + pmoney

    def withdraw(self, mmoney):
        if mmoney<= self.__balance:
            self.__balance = self.__balance - mmoney

a = BankAccount('A')
b = BankAccount('B')

a.deposit(100)
b.deposit(200)
a.withdraw(30)
b.withdraw(50)

print(f'{a.owner} 계좌의 현재 잔액:',a.get_balance())

print(f'{b.owner}계좌의 현재 잔액:',b.get_balance())

a.set_balance(500)
print(f'{a.ower} 계좌의 수정된 잔액:',a.get_balance())