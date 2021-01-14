"""Creating a new window """
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning Tkinter')
root.iconbitmap('images/cloud_socialnetwork.ico')

def open():
    global my_img
    top = Toplevel()
    top.title("Meet Bob")
    top.iconbitmap('images/cloud_socialnetwork.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/bob2.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window Here", command=open).pack()

mainloop()