from tkinter import *

root = Tk()
root.title("Prince Tkinter APP")


frame = LabelFrame(root, text="This is my frame", padx=5, pady=5)
frame.pack(padx=100, pady=100)

r = StringVar()
Radiobutton(frame, text="Domestic", variable="r", value=1).pack()
Radiobutton(frame, text="International", variable="r", value=2).pack()


button_quit = Button(frame, text="Exit Program", command=root.quit)
button_quit.pack()



root.mainloop()