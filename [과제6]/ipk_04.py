class Person:
    def __init__(self, name):
        self.name = name 

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes = []

    def enrollCourse(self, subject):
        self.classes.append(subject)

    def clearCourses(self):
        self.classes = []


from tkinter import *

root = Tk()
root.title('문제 4')
root.geometry('380x280')


def register_courses():
    student.clearCourses()

    if var_py.get(): student.enrollCourse('Python')
    if var_ai.get(): student.enrollCourse('AI')
    if var_ds.get(): student.enrollCourse('DataScience')

    if student.classes:
        result.set(f"등록된 과목: {', '.join(student.classes)}")
    else:
        result.set('선택된 과목이 없습니다.')

def reset_all():
    var_py.set(0)
    var_ai.set(0)
    var_ds.set(0)
    student.clearCourses()
    result.set('모든 선택을 해제했습니다.')

student = Student('홍길동') 

Label(root, text=f'학생 : {student.name}').pack()

var_py = IntVar(value=0)
var_ai = IntVar(value=0)
var_ds = IntVar(value=0)

button1 = Checkbutton(root, text='Python', variable=var_py)
button2 = Checkbutton(root, text='AI', variable=var_ai)
button3 = Checkbutton(root, text='DataScience', variable=var_ds)
button1.pack()
button2.pack()
button3.pack()

realbutton1 = Button(root, text='등록하기', command=register_courses)
realbutton2 = Button(root, text='초기화', command=reset_all)
realbutton1.pack()
realbutton2.pack()

result = StringVar(value='과목을 선택하고 [등록하기]를 누르세요.')
lb = Label(root, textvariable=result, wraplength=340, justify='left')
lb.pack(pady=8)

root.mainloop()
