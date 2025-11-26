import math
from tkinter import *

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        pass
    def perimeter(self):
        pass
    def draw(self, canvas):
        pass


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill='tomato')


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r,
                           fill='skyblue')


def picture():
    canvas.delete("all")

    if var.get() == 1:
        s = Rectangle(50, 50, 100, 100)
    else:
        s = Circle(200, 150, 60)

    s.draw(canvas)
    label.config(text=f"면적 = {s.area():.2f}, 둘레 = {s.perimeter():.2f}")


root = Tk()
root.title("문제3")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

label = Label(root, text="도형을 선택하고 그리기를 누르세요.")
label.pack()

var = IntVar(value=1)

Radiobutton(root, text="사각형", value=1, variable=var).pack()
Radiobutton(root, text="원", value=2, variable=var).pack()

Button(root, text="그리기", command=picture).pack()

root.mainloop()
