from tkinter import *

class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '...'

class Dog(Pet):
    def speak(self):
        return '멍멍!'

class Cat(Pet):
    def speak(self):
        return '야옹!'

class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet


root = Tk()
root.title('문제 5')
root.geometry('700x300')

person = Person('홍길동')

Label(root, text='반려동물 등록하기').pack(pady=8)

Label(root, text='반려동물 이름:').pack()
entry = Entry(root, width=30)
entry.pack(pady=3)

Label(root, text='종류 선택:').pack()
pet_type = StringVar(value='Dog')
Radiobutton(root, text='강아지', value='Dog', variable=pet_type).pack()
Radiobutton(root, text='고양이', value='Cat', variable=pet_type).pack()

Label(root, text='옵션 선택:').pack(pady=5)
vaccinated = IntVar(value=0)
neutered = IntVar(value=0)
Checkbutton(root, text='예방접종 완료', variable=vaccinated).pack()
Checkbutton(root, text='중성화 완료', variable=neutered).pack()

result = StringVar(value='등록 정보를 확인하세요.')
Label(root, textvariable=result, fg='blue', wraplength=500, justify='left').pack(pady=10)

def register():
    pet_name =entry.get() or '이름없음'
    kind = pet_type.get()

    if kind == 'Dog':
        pet = Dog(pet_name)
    else:
        pet = Cat(pet_name)

    person.pet = pet

    vac = 'O' if vaccinated.get() else 'X'
    neu = 'O' if neutered.get() else 'X'
    kind_kor = '강아지' if kind == 'Dog' else '고양이'

    msg = (f'{person.name}의 반려동물 등록 완료!\n'
           f'이름: {pet.name} ({kind_kor})\n'
           f'소리: {pet.speak()}\n'
           f'예방접종: {vac}, 중성화: {neu}')
    result.set(msg)

def reset():
    entry.delete(0, END)
    pet_type.set('Dog')
    vaccinated.set(0)
    neutered.set(0)
    person.pet = None
    result.set('등록 정보를 확인하세요.')

Button(root, text='등록하기', width=12, command=register).pack(pady=3)
Button(root, text='초기화', width=12, command=reset).pack(pady=3)

root.mainloop()
