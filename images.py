from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning Tkinter')
root.iconbitmap('images/cloud_socialnetwork.ico')


my_img = ImageTk.PhotoImage(Image.open("images/bob2.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/bob-minion.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/minions-bob.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/minions2.png"))

image_list = [my_img, my_img2, my_img3, my_img4]

my_label = Label(image = my_img)
my_label.grid(row=0, column=0, columnspan=3)
 
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command= lambda: back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command= lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

#my_label.pack()



#button_quit = Button(root, text="Exit Progam", command=root.quit)
#button_quit.pack()



root.mainloop()