from tkinter import *
 
root = Tk()
photo = PhotoImage(file = 'dog2.gif.jpg')
label = Label(root, image = photo)
label.pack()
root.mainloop()