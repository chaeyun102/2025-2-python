class Inventory:
    def __init__(self,amount=0):
        self.amount = amount
        print('새 상품이 등록되었습니다.')

    def get_stock(self):
        return self.amount

    def set_stock(self, amount):
        self.amount = amount
        

    def add_stock(self, amount):
        self.amount += amount
        print(f'{amount}개가 입고되었습니다.')

    def remove_stock(self, amount):
        self.amount = self.amount - amount
        print(f'{amount}개가 출고되었습니다.')


item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print('현재 재고 수량:', item1.get_stock())

item1.set_stock(20)
print('수정된 재고 수량:', item1.get_stock())