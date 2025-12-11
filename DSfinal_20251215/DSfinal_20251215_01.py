from tkinter import *
import random 

class DrawableShape:
    def __init__(self):
        self.canvas = canvas

    def draw(self):
        pass

class Square(DrawableShape):
    def __init__(self, canvas,x,y,size):
        super().__init__(canvas)
        self.x = x 
        self.y = y 
        self.size = size

    def draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x +self.size,self.y +self.size , outline="black")


class Circle(DrawableShape):
    def __init__(self, canvas,x,y,radius):
        super().__init__(canvas)
        self.x = x 
        self.y = y 
        self.radius = radius

    def draw(self):
        self.canvas.create_oval(self.x, self.y, self.x+self.radius, self.y+self.radius, outline="black")

root = Tk()
canvas = Canvas(root, width=400, height=300, bg="white")

shapes = []

def squares():
    sqr = Square(canvas,random.randiant(0,400), random.randiant(0,300), random.randiant(0,100))
    shapes.append(sqr)

def circles():
    cir = Circle(canvas,random.randiant(0,400), random.randiant(0,300), random.randiant(0,100))
    shapes.append(cir)
def everything():
    sqr = Square(canvas,random.randiant(0,400), random.randiant(0,300), random.randiant(0,100))
    cir = Circle(canvas,random.randiant(0,400), random.randiant(0,300), random.randiant(0,100))
    shapes.append(sqr)
    shapes.append(cir)
Button(root, text = '사각형 추가',command = squares)
Button(root, text = '원 추가', command = circles)
Button(root, text = '모두 그리기', command = everything)