class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return '멍멍!'
class Cat(Animal):
    def speak(self):
        return '야옹!'
class Duck(Animal):
    def speak(self):
        return '꽥꽥!'

def make_sound(animal):
    sound = animal.speak()
    label2.config(text=sound)

from tkinter import *

root = Tk()
root.geometry('400x320')
root.title('동물 소리 듣기')

label1 = Label(root, text = '동물 버튼을 눌러 소리를 들어보세요.')
label1.pack()

bframe = Frame(root)
bframe.pack()

button1 = Button(bframe, text = '강아지', command = lambda: make_sound(Dog()))
button2 = Button(bframe, text = '고양이', command = lambda:make_sound(Cat()))
button3 = Button(bframe, text = '오리', command = lambda:make_sound(Duck()))

button1.pack(side = 'left', padx = 4)
button2.pack(side = 'left', padx = 4)
button3.pack(side = 'left', padx = 4)

label2 = Label(root, text = '(여기에 울음소리가 나옵니다)')
label2.pack()

root.mainloop()