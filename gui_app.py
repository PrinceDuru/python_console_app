from tkinter import *

root = Tk()
root.title("Prince Tkinter APP")

def myClick():
    myLabel = Label(root, text=txt.get())
    myLabel.pack()

myButton = Button(root, text="Prince button", command=myClick, fg="blue", bg="black")

myButton.pack()

txt = Entry(width = 60, bg="red", fg="green")
txt.pack()

root.mainloop()