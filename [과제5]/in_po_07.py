from tkinter import *
from tkinter import messagebox

class Food:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    
    def total_price(self, qty):
        return self.price * qty
    
    def __str__(self):
        return f'메뉴: {self.name}, 단가: {self.price}원'
    
class DeliveryFood(Food):
    def __init__(self, name, price, delivery_fee):
        super().__init__(name, price)
        self.delivery_fee = delivery_fee

    def total_price(self, qty):
        return (self.price * qty) + self.delivery_fee
    
    def __str__(self):
        return f'메뉴: {self.name}, 단가: {self.price}원, 배달비: {self.delivery_fee}원'
    
class Order:
    def __init__(self):
        self.items = []

    def add(self, food, qty):
        self.items.append((food, qty))

    def clear(self):
        self.items.clear()

    def total(self):
        total_price = 0
        for food, qty in self.items:
            total_price += food.total_price(qty)
        return total_price
    
    def summary_lines(self):
        receipt = []
        for food, qty in self.items:
            receipt.append(f'{food.name} x {qty} → {food.total_price(qty):,}원')
        receipt.append(f'합계: {self.total():,}원')
        return receipt
    
def add_to_cart():
    sel = menu_list.curselection()
    if not sel:
        messagebox.showwarning('안내', '메뉴를 선택하세요.')
        return
    try:
        qty = int(qty_var.get())
    except ValueError:
        messagebox.showwarning('안내', '수량은 숫자만 입력하세요.')
        return
    qty = max(1, qty)
    order.add(menu_items[sel[0]], qty)
    cart_list.insert('end', f'{menu_items[sel[0]].name} x {qty}')
    total_label.config(text=f'합계: {order.total():,}원')

def place_order():
    if not order.items:
        messagebox.showinfo('알림', '장바구니가 비어 있습니다.')
        return
    receipt_text = '\n'.join(order.summary_lines())
    messagebox.showinfo('영수증', receipt_text)

def clear_cart():
    if not order.items:
        messagebox.showinfo('알림', '이미 장바구니가 비어 있습니다.')
        return
    if messagebox.askyesno('확인', '장바구니를 모두 비우시겠습니까?'):
        order.clear()
        cart_list.delete(0, 'end')
        total_label.config(text='합계: 0원')

root = Tk()
root.title('주문 배달 시스템')
root.geometry('680x440')

order = Order()
menu_items = [
    Food('김밥', 3000),
    Food('라면', 4000),
    Food('떡볶이', 5000),
    DeliveryFood('치킨', 18000, 3000),
    DeliveryFood('피자', 20000, 3000),
]

left = Frame(root, padx=8, pady=8)
left.pack(side='left', fill='both', expand=True)

right = Frame(root, padx=8, pady=8)
right.pack(side='right', fill='both', expand=True)

Label(left, text='메뉴 목록').pack(anchor='w')
menu_list = Listbox(left, height=10)
menu_list.pack(fill='both', expand=True)
for m in menu_items:
    menu_list.insert('end', str(m))

ctrl = Frame(left)
ctrl.pack(pady=6)
Label(ctrl, text='수량').pack(side='left')

qty_var = IntVar(value=1)
Spinbox(ctrl, from_=1, to=20, width=5, textvariable=qty_var, justify='center').pack(side='left', padx=6)
Button(ctrl, text='장바구니 담기', command=add_to_cart).pack(side='left')

Label(right, text='장바구니').pack(anchor='w')
cart_list = Listbox(right, height=10)
cart_list.pack(fill='both', expand=True)

bottom = Frame(right)
bottom.pack(fill='x', pady=8)

total_label = Label(bottom, text='합계: 0원')
total_label.pack(side='left')

btn_frame = Frame(bottom)
btn_frame.pack(side='right')

Button(btn_frame, text='전체 비우기', command=clear_cart).pack(side='right', padx=5)
Button(btn_frame, text='주문하기', command=place_order).pack(side='right')

root.mainloop()
