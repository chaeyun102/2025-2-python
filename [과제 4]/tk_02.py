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


borrowed_books: list[Book] = []


def update_borrowed_list():
    if borrowed_books:
        info = "대출 현황: "
        for b in borrowed_books:
            info += f"{b.title}({b.author}), "
        info = info[:-2]
    else:
        info = "대출 현황: 없음"
    borrowed_label.config(text=info)


def borrow_book():
    title = entry_title.get().strip()
    author = entry_author.get().strip()

    if not title or not author:
        message_label.config(text="제목과 저자를 모두 입력하세요.", fg="red")
        return

    for b in borrowed_books:
        if b.title == title and b.author == author:
            message_label.config(text=f"『{title}』은(는) 이미 대출 중입니다.", fg="red")
            return

    new_book = Book(title, author)
    borrowed_books.append(new_book)
    message_label.config(text=new_book.borrow(), fg="blue")
    update_borrowed_list()


def return_book():
    title = entry_title.get().strip()
    author = entry_author.get().strip()

    if not title or not author:
        message_label.config(text="제목과 저자를 모두 입력하세요.", fg="red")
        return

    for b in borrowed_books:
        if b.title == title and b.author == author:
            borrowed_books.remove(b)
            message_label.config(text=b.return_book(), fg="green")
            update_borrowed_list()
            return

    message_label.config(text=f"『{title}』은(는) 대출 목록에 없습니다.", fg="red")


root = Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("430x280")

Label(root, text = "도서 대출 관리 시스템", font =('Helvetica', 16, 'bold')).pack(pady=10)
Label(root, text = "제목:").pack()
entry_title = Entry(root, width=25)
entry_title.pack()

Label(root, text="저자:").pack()
entry_author = Entry(root, width=25)
entry_author.pack()

frame = Frame(root)
frame.pack(pady=10)

Button(frame, text = "대출", width = 10, command =borrow_book).pack(side='left', padx=5)
Button(frame, text = "반납", width = 10, command = return_book).pack(side='left', padx=5)

message_label = Label(root, text = "", font =('Helvetica', 11, 'bold'))
message_label.pack(pady =5)

borrowed_label = Label(root, text="대출 현황: 없음", font=('Helvetica', 10))
borrowed_label.pack(pady =5)

root.mainloop()
