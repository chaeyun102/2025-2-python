from tkinter import *

def nemo():
    canvas.delete('all')
    canvas.create_rectangle(10,10,100,100, fill = 'red')

def circle():
    canvas.delete('all')
    canvas.create_oval(10,10,100,100, fill = 'blue')

def picture():
    canvas.delete('all')
    global img 
    img = PhotoImage(file ="DS_20251215\image1.png")
    canvas.create_image(10,10, anchor = NW, image = img)

def remove():
    canvas.delete('all')

root = Tk()
root.geometry('420x440')
root.title('중간고사 7번')

canvas = Canvas(root,width = 400, height = 320, bg = 'white')
canvas.pack()

frame = Frame(root, width = 40, height = 20)
frame.pack()

button1 = Button(frame, text = '사각형', command = nemo)
button1.pack(side = 'left')
button2 = Button(frame, text = '원', command = circle)
button2.pack(side = 'left')
button3 = Button(frame, text = '그림', command = picture)
button3.pack(side = 'left')
button4 = Button(frame, text = '지우기', command = remove)
button4.pack(side = 'left')

Label(root, text = '버튼을 눌러 도형을 선택하세요.').pack()

root.mainloop()