from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import Font

from tkinter.ttk import Combobox


def ok_button_click():
    try:
        name = entry_name.get()
        residency = ""
        if rdb_value.get() == 'intl':
            residency = "International"
        if rdb_value.get() == 'dom':
            residency = "Domestic"

        program = cmb_programming.get()
        courses = ""
        if cb.get() == 'COMP100':
            courses += "Programming"
        if cb1.get() == 'COMP213':
            courses += "\nWeb Design"
        if cb2.get() == 'COMP120':
            courses += "\nSoftware Engineering"
        result = name + "\n" + program + "\n" + residency + "\n" + courses
        messagebox.showinfo(title="Information", message=result)
    
    except Exception:
        messagebox.showinfo(title="Error", message="Please enter valid value.")


def reset_button_click():
    entry_name.delete(0, 'end')
    cb.set(0)
    cb1.set(0)
    cb2.set(0)
    cmb_programming.set('')


# exit button event
def exit_button_click():
    frame.destroy()


# create GUI
frame = Tk()
# set title of root frame
frame.title("Centennial College")
frame["background"] = "#DAF7A6"
color = "#DAF7A6"
# font style for controls
font = Font(family='Helvetica', size=8)
title_font = Font(family='Helvetica', size=18, weight="bold")

# create controls
lbl_title = Label(frame, text="ICET Student Survey", font=title_font)
lbl_title['background'] = color
lbl_full_name = Label(frame, text="Full name:", font=font)
lbl_full_name['background'] = color
lbl_residency = Label(frame, text="Residency: ", font=font)
lbl_residency['background'] = color
lbl_programs = Label(frame, text="Programs ", font=font)
lbl_programs['background'] = color
lbl_courses = Label(frame, text="Courses", font=font)
lbl_courses['background'] = color

rdb_value = StringVar()
rdb_domestic = Radiobutton(frame, text="Domestic", value='dom', font=font, variable=rdb_value)
rdb_domestic['background'] = color
rdb_international = Radiobutton(frame, text="International", value='intl', font=font, variable=rdb_value)
rdb_international['background'] = color
rdb_value.set(None)

cb = StringVar()
chk_programming = Checkbutton(text='Programming', onvalue='COMP100', offvalue='', font=font, variable=cb)
chk_programming['background'] = color
cb1 = StringVar()
chk_web = Checkbutton(text='Web Page Design', onvalue='COMP213', offvalue='', font=font, variable=cb1)
chk_web['background'] = color
cb2 = StringVar()
chk_software = Checkbutton(text='Software Engineering', onvalue='COMP120', offvalue='', font=font, variable=cb2)
chk_software['background'] = color
entry_name = Entry(frame, font=font)
n = StringVar()
cmb_programming = Combobox(frame, textvariable=n)
cmb_programming['values'] = ("AI", "Gaming", "Health", "Software")

btn_reset = Button(frame, text="Reset", command=reset_button_click, font=font)
btn_ok = Button(frame, text="Ok", command=ok_button_click, font=font)
btn_exit = Button(frame, text="exit", command=exit_button_click, font=font)

# add controls to gridview
lbl_title.grid(row=0, column=0, padx=10, columnspan=3)
lbl_full_name.grid(row=1, column=0, padx=10)
lbl_residency.grid(row=2, column=0, padx=10)
lbl_programs.grid(row=4, column=0, padx=10)
lbl_courses.grid(row=5, column=0, padx=10)
rdb_domestic.grid(row=2, column=1, sticky="w", padx=10)
rdb_international.grid(row=3, column=1, sticky="w", padx=10)
chk_programming.grid(row=5, column=1, padx=10, sticky="w")
chk_web.grid(row=6, column=1, padx=10, sticky="w")
chk_software.grid(row=7, column=1, padx=10, sticky="w")

cmb_programming.grid(row=4, column=1, padx=10, sticky='w')

entry_name.grid(row=1, column=1, padx=10)
entry_name.config(width=30)
btn_reset.grid(row=8, column=0, padx=10, pady=10)
btn_reset.config(height=1, width=12)
btn_ok.grid(row=8, column=1, padx=10, pady=10)
btn_ok.config(height=1, width=12)
btn_exit.grid(row=8, column=2, padx=10, pady=10)
btn_exit.config(height=1, width=12)


if __name__ == "__main__":

    # Create GUI
    frame.mainloop()

