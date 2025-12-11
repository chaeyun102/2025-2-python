from tkinter import *

class Person:
    def __init__(self,name):
        self.name = name
class HobbyPerson(Person):
    def __init__(self,name:str):
        super().__init__(name)
        self.hobbies = []

    def add_hobby(self,hobby):
        self.hobbies.append(hobby)

    def clear_hobbies(self):
        self.hobbies=[]
    
root = Tk()
root.title('문제 2')
root.geometry('380x260')

per = HobbyPerson('김덕성')


selected_hobby = IntVar()    


Radiobutton(root, text = '게임', value=1, variable= selected_hobby).pack()
Radiobutton(root, text = '독서', value=2, variable=selected_hobby).pack()
Radiobutton(root, text = '운동', value=3, variable=selected_hobby).pack()

result = StringVar(value="취미를 선택하고 [등록하기]를 누르세요.")
lb = Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=8)

# 동작 함수들
def register_courses():# 현재 체크 상태를 기준으로 과목 리스트 갱신
    per.clear_hobbies()
    if selected_hobby.get() ==1 :
        per.add_hobby('게임')
    if selected_hobby.get() ==2 :
        per.add_hobby('독서')
    if selected_hobby.get() ==3 :
        per.add_hobby('운동')
    if per.hobbies:
        result.set(f"현재 선택된 취미: {', '.join(per.hobbies)}")
    else:
        result.set("선택된 취미가 없습니다.")

def reset_all():
    per.clear_hobbies
    result.set("모든 선택을 해제했습니다.")

Button(root, text = '등록하기' , command = register_courses).pack()
Button(root, text = '초기화' , command = reset_all).pack()
root.mainloop()