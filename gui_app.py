from re import T
from telnetlib import X3PAD
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import Font


from tkinter.ttk import Combobox


class HelloCentennial(Frame):
    def __init__(self, my_window):
        Frame.__init__(self, my_window)

        self.radioBtnvalue = StringVar()
        self.combobtnValue = StringVar()
        self.cb1 = StringVar()
        self.cb2 = StringVar()
        self.progNameValue = StringVar()
        self.userNameValue = StringVar()

        self.row_number = 0
        self.column_number = 1
        self.color = "#4EA004"
        self.font = Font(family='Helvetica', size=8)
        self.title_font = Font(family='Helvetica', size=18, weight="bold")   

        # create controls
        self.lbl_title = Label(self, text="ICET Student Survey", font=self.title_font, bg=self.color)
        self.lbl_full_name = Label(self, text="Full name:", font=self.font, bg=self.color)
        self.lbl_residency = Label(self, text="Residency: ", font=self.font, bg=self.color)
        self.lbl_program = Label(self, text="Programs ", font=self.font, bg=self.color)
        self.lbl_courses = Label(self, text="Courses", font=self.font, bg=self.color)

        self.rdb_domestic = Radiobutton(self, text="Domestic", value='dom', variable=self.radioBtnvalue, font=self.font, bg=self.color)
        self.rdb_international = Radiobutton(self, text="International", value='intl', variable=self.radioBtnvalue, bg=self.color)
        self.radioBtnvalue.set("dom")

        self.chk_programming = Checkbutton(self, text='Programming 1', onvalue='COMP100', offvalue='',  variable=self.cb, bg=self.color)
        self.chk_web = Checkbutton(self, text='Web Page Design', onvalue='COMP213', offvalue='', variable=self.cb1, bg=self.color)
        self.chk_software = Checkbutton(self, text='Software Engineering', onvalue='COMP120', offvalue='',  variable=self.cb2, bg=self.color)
        self.cb.set("COMP100")
        self.cb1.set("COMP213")
        
        self.entry_name = Entry(self, textvariable = self.userNameValue, font=self.font)
        self.userNameValue.set("Prince Duru")

        self.cmb_programming = Combobox(self, textvariable=self.progNameValue)
        self.cmb_programming['values'] = ("AI", "Gaming", "Health", "Software")
        self.progNameValue.set("AI")

        self.btn_reset = Button(self, text="Reset", command=self.reset_button_click, font=self.font)
        self.btn_ok = Button(self, text="Ok", command=self.ok_button_click, font=self.font)
        self.btn_exit = Button(self, text="Exit", command=self.exit_button_click, font=self.font)

        # add controls to gridview
        self.lbl_title.grid(row=0, column=0, padx=10, columnspan=3)
        self.lbl_full_name.grid(row=1, column=0, padx=10)
        self.lbl_residency.grid(row=2, column=0, padx=10)
        self.lbl_program.grid(row=4, column=0, padx=10)
        self.lbl_courses.grid(row=5, column=0, padx=10)
        self.rdb_domestic.grid(row=2, column=1,  padx=10, sticky="w") #sticky="w",
        self.rdb_international.grid(row=3, column=1, sticky="w", padx=10)
        self.chk_programming.grid(row=5, column=1, padx=10, sticky="w")
        self.chk_web.grid(row=6, column=1, padx=10, sticky="w")
        self.chk_software.grid(row=7, column=1, padx=10, sticky="w")

        self.cmb_programming.grid(row=4, column=1, padx=10, sticky="nsew")

        self.entry_name.grid(row=1, column=1, padx=10, sticky=E+W+N+S)
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
            if self.radioBtnvalue.get() == 'intl':
                residency = "International"
            if self.radioBtnvalue.get() == 'dom':
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
        self.userNameValue.set('')
        self.cb.set(0)
        self.cb1.set(0)
        self.cb2.set(0)
        self.cmb_programming.set('')
      


    # exit button event
    def exit_button_click(self):
        the_window.destroy()

    

    def resizeRow(self):
        item_list = [self.lbl_title, self.lbl_full_name, self.lbl_residency, self.lbl_program, self.lbl_courses, \
        self.rdb_domestic, self.rdb_international, self.chk_programming, self.chk_web, self.chk_software, \
        self.cmb_programming, self.entry_name, self.btn_reset, self.btn_ok, self.btn_exit]
        
        Grid.columnconfigure(frameA, self.column_number, weight=1)

        for item in item_list:
            Grid.rowconfigure(frameA, self.row_number, weight=1)
            # Grid.columnconfigure(frameA, self.column_number, weight=1)
            self.row_number += 1
            # self.column_number += 1

the_window = Tk()

# set title of root frame
frameA = HelloCentennial(the_window)
# frameA.grid(row=0, column=0, padx=10, pady=10)
frameA.pack(padx=8, pady=7,expand=YES, fill=BOTH)

frameA.resizeRow()

the_window.title("Centennial College")
frameA["background"] = "#4EA004"

if __name__ == "__main__":

    # Create GUI
    the_window.mainloop()

