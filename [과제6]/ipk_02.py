class Pet:
    def speak(self):
        return '...'

class Dog(Pet):
    def speak(self):
        return '멍멍!'
    
class Cat(Pet):
    def speak(self):
        return '야옹!'
    
class Person:
    def __init__(self, name, pet = None):
        self.name = name
        self.pet = pet

from tkinter import *

root = Tk()
root.title('문제2')
root.geometry('400x200')

person = Person('홍길동')

def dogchoice():
    person.pet = Dog()
    result.set('강아지를 선택했습니다.')

def catchoice():
    person.pet = Cat()
    result.set('고양이를 선택했습니다.')

def speaklouder():
    result.set(f'{person.name}의 반려동물 -> {person.pet.speak()}')

Label(root, text = '동물을 선택해 주세요.').pack()

frame = Frame(root)
frame.pack()
dogbutton = Button(frame, text = '강아지 선택', command = dogchoice)
catbutton = Button(frame, text = '고양이 선택', command = catchoice)
speakbutton = Button(root, text = '말하기', command = speaklouder)
dogbutton.pack(side = 'left', pady = 10)
catbutton.pack(side = 'left',pady = 10)
speakbutton.pack(pady = 10)

result = StringVar(value='')
label = Label(root, textvariable = result, fg = 'blue')
label.pack()

root.mainloop()