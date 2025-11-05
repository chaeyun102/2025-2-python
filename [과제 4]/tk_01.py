from tkinter import *

class Book:
    def __init__(self,title,author,borrowed =False):
        self.title = title
        self.author = author
        self.borrowed = borrowed

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return self.title+'이(가) 대출되었습니다.'

        else:
            return self.title+'은(는) 이미 대출 중입니다.'

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return self.title+'이(가) 반납되었습니다.'
        else: 
            return self.title+'은(는) 대출되지 않은 상태입니다.'
        
book = Book("", "")

def borrow_book():
    book.title = entry1.get()
    book.author = entry2.get()
    message = book.borrow()
    label.config(text=message, fg='blue')

def return_():
    book.title = entry1.get()
    book.author = entry2.get()
    message = book.return_book()
    label.config(text=message, fg='green')

root = Tk()
root.title('도서 대출 관리 프로그램')


Label(root, text = '도서 대출 관리 시스템',font = ('Helevetica',16,'bold')).pack()

Label(root, text = '제목: ').pack()
entry1 = Entry(root, width = 20)
entry1.pack()

Label(root, text = '저자').pack()
entry2 = Entry(root, width = 20)
entry2.pack()

frame = Frame(root)
frame.pack(pady=10)

button1 = Button(frame, text='대출', width=10, command=borrow_book)
button1.pack(side='left', padx=5)

button2 = Button(frame, text='반납', width=10, command=return_)
button2.pack(side='left', padx=5)

label = Label(root, text='', font=('Helvetica', 11, 'bold'))
label.pack(pady=10)

root.mainloop()



