from tkinter import *

root = Tk()
root.title('중간고사 4번')
root.geometry('400x400')
choice = IntVar()

canvas = Canvas(root, width = 400, height = 300, fill = 'white')
canvas.pack()

def choose():
    if value ==1:
       canvas.delete('all')
       canvas.create_rectangle(50,25,50,25, fill = 'red')

    elif value == 2:
       canvas.delete('all')
       canvas.create_oval(10,10,100,100, fill = 'blue')

    elif value == 3:

        canvas.delete('all')
        canvas.create_text(200,100, text = 'Hello Duksung', fill = 'blue', font = ('Helvetica',20))

Radiobutton(root, text = '사각형', variable = choice, value = 1).pack()
Radiobutton(root, text = '원', variable = choice, value = 2).pack()
Radiobutton(root, text = '텍스트',variable = choice, value = 3).pack()

button = Button(root, text = '그리기', command =choose())