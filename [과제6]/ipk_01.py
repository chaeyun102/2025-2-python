class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return f'승용차 {self.name}가 주행합니다.'
    
class Truck(Vehicle):
    def drive(self):
        return f'트럭 {self.name}가 화물을 싣고 주행합니다.'
    
car = Car('car1')
truck = Truck('truck1')

from tkinter import *

root = Tk()
root.title('문제1')
root.geometry('400x300')

Label(root, text = '버튼을 눌러보세요.').pack()

def carcar():
    label.config(text = car.drive())

def trucktruck():
    label.config(text = truck.drive())

button1 = Button(root, text = '자동차 주행', command = carcar)
button2 = Button(root, text = '트럭 주행', command = trucktruck)
button1.pack()
button2.pack()
label = Label(root, text = '')
label.pack()
root.mainloop()
