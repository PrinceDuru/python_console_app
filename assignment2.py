from re import T
from telnetlib import X3PAD
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import Font

from tkinter.ttk import Combobox


class HelloCentennial(Frame):
    def __init__(self, my_window):
        Frame.__init__(self, my_window)

        self.rdb_value = StringVar()
        self.cb = StringVar()
        self.cb1 = StringVar()
        self.cb2 = StringVar()
        self.n = StringVar()

        self.color = "#DAF7A6"
        self.font = Font(family='Helvetica', size=8)
        self.title_font = Font(family='Helvetica', size=18, weight="bold")   

        # create controls
        self.lbl_title = Label(self, text="ICET Student Survey", font=self.title_font, bg=self.color)
        self.lbl_full_name = Label(self, text="Full name:", font=self.font, bg=self.color)
        self.lbl_residency = Label(self, text="Residency: ", font=self.font, bg=self.color)
        self.lbl_programs = Label(self, text="Programs ", font=self.font, bg=self.color)
        self.lbl_courses = Label(self, text="Courses", font=self.font, bg=self.color)

        self.rdb_domestic = Radiobutton(self, text="Domestic", value='dom', variable=self.rdb_value, font=self.font, bg=self.color)
        self.rdb_international = Radiobutton(self, text="International", value='intl', variable=self.rdb_value, bg=self.color)
        self.rdb_value.set(None)

        self.chk_programming = Checkbutton(self, text='Programming', onvalue='COMP100', offvalue='',  variable=self.cb, bg=self.color)
        self.chk_web = Checkbutton(self, text='Web Page Design', onvalue='COMP213', offvalue='', variable=self.cb1, bg=self.color)
        self.chk_software = Checkbutton(self, text='Software Engineering', onvalue='COMP120', offvalue='',  variable=self.cb2, bg=self.color)
        
        self.entry_name = Entry(self, font=self.font)
        self.cmb_programming = Combobox(self, textvariable=self.n)
        self.cmb_programming['values'] = ("AI", "Gaming", "Health", "Software")

        self.btn_reset = Button(self, text="Reset", command=self.reset_button_click, font=self.font)
        self.btn_ok = Button(self, text="Ok", command=self.ok_button_click, font=self.font)
        self.btn_exit = Button(self, text="exit", command=self.exit_button_click, font=self.font)

        # add controls to gridview
        self.lbl_title.grid(row=0, column=0, padx=10, columnspan=3)
        self.lbl_full_name.grid(row=1, column=0, padx=10)
        self.lbl_residency.grid(row=2, column=0, padx=10)
        self.lbl_programs.grid(row=4, column=0, padx=10)
        self.lbl_courses.grid(row=5, column=0, padx=10)
        self.rdb_domestic.grid(row=2, column=1, sticky="w", padx=10)
        self.rdb_international.grid(row=3, column=1, sticky="w", padx=10)
        self.chk_programming.grid(row=5, column=1, padx=10, sticky="w")
        self.chk_web.grid(row=6, column=1, padx=10, sticky="w")
        self.chk_software.grid(row=7, column=1, padx=10, sticky="w")

        self.cmb_programming.grid(row=4, column=1, padx=10, sticky='w')

        self.entry_name.grid(row=1, column=1, padx=10)
        self.entry_name.config(width=30)
        self.btn_reset.grid(row=8, column=0, padx=10, pady=10)
        self.btn_reset.config(height=1, width=12)
        self.btn_ok.grid(row=8, column=1, padx=10, pady=10)
        self.btn_ok.config(height=1, width=12)
        self.btn_exit.grid(row=8, column=2, padx=10, pady=10)
        self.btn_exit.config(height=1, width=12)


    def ok_button_click(self):
        try:
            name = self.entry_name.get()
            residency = ""
            if self.rdb_value.get() == 'intl':
                residency = "International"
            if self.rdb_value.get() == 'dom':
                residency = "Domestic"

            program = self.cmb_programming.get()
            courses = ""
            if self.cb.get() == 'COMP100':
                courses += "Programming"
            if self.cb1.get() == 'COMP213':
                courses += "\nWeb Design"
            if self.cb2.get() == 'COMP120':
                courses += "\nSoftware Engineering"
            result = name + "\n" + program + "\n" + residency + "\n" + courses
            messagebox.showinfo(title="Information", message=result)
        
        except Exception:
            messagebox.showinfo(title="Error", message="Please enter valid value.")


    def reset_button_click(self):
        self.entry_name.delete(0, 'end')
        self.cb.set(0)
        self.cb1.set(0)
        self.cb2.set(0)
        self.cmb_programming.set('')


    # exit button event
    def exit_button_click(self):
        the_window.destroy()


# create GUI
# frame = Tk()

the_window = Tk()


# set title of root frame
frameA = HelloCentennial(the_window)
frameA.grid(row=0, column=0, padx=10, pady=10)

# Grid.rowconfigure(frameA, 0, weight=1)
# Grid.columnconfigure(frameA, 0, weight=1)
# frameA["resizeable"] = (True, True)


the_window.title("Centennial College")
frameA["background"] = "#DAF7A6"








if __name__ == "__main__":

    # Create GUI
    the_window.mainloop()

