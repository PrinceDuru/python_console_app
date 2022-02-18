from re import T
from telnetlib import X3PAD
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import Font


from tkinter.ttk import Combobox


class SurveyApp(Frame):
    def __init__(self, App_Window):
        Frame.__init__(self, App_Window)

        self.radioBtnvalue = StringVar()
        self.comboBtnValue1 = StringVar()
        self.comboBtnValue2 = StringVar()
        self.comboBtnValue3 = StringVar()
        self.progNameValue = StringVar()
        self.userNameValue = StringVar()

        self.row_number = 0
        self.column_number = 1
        self.color = "#4EA004"
        self.font = Font(family='Helvetica', size=8)
        self.title_font = Font(family='Helvetica', size=18, weight="bold")   

        # create controls
        self.label_title = Label(self, text="ICET Student Survey", font=self.title_font, bg=self.color)
        self.label_full_name = Label(self, text="Full name:", font=self.font, bg=self.color)
        self.label_residency = Label(self, text="Residency: ", font=self.font, bg=self.color)
        self.label_program = Label(self, text="Programs ", font=self.font, bg=self.color)
        self.label_courses = Label(self, text="Courses", font=self.font, bg=self.color)

        self.radioBtn_domestic = Radiobutton(self, text="Domestic", value='dom', variable=self.radioBtnvalue, font=self.font, bg=self.color)
        self.radioBtn_international = Radiobutton(self, text="International", value='intl', variable=self.radioBtnvalue, bg=self.color)
        self.radioBtnvalue.set("dom")

        self.chkBx_programming = Checkbutton(self, text='Programming 1', onvalue='COMP100', offvalue='',  variable=self.comboBtnValue1, bg=self.color)
        self.chkBx_web = Checkbutton(self, text='Web Page Design', onvalue='COMP213', offvalue='', variable=self.comboBtnValue2, bg=self.color)
        self.chkBx_software = Checkbutton(self, text='Software Engineering', onvalue='COMP120', offvalue='',  variable=self.comboBtnValue3, bg=self.color)
        self.comboBtnValue1.set("COMP100")
        self.comboBtnValue2.set("COMP213")
        
        self.entry_name = Entry(self, textvariable = self.userNameValue, font=self.font)
        self.userNameValue.set("Prince Duru")

        self.cmbBx_programming = Combobox(self, textvariable=self.progNameValue)
        self.cmbBx_programming['values'] = ("AI", "Gaming", "Health", "Software")
        self.progNameValue.set("AI")

        self.reset_Button = Button(self, text="Reset", command=self.resetButton, font=self.font)
        self.ok_Button = Button(self, text="Ok", command=self.okButton, font=self.font)
        self.exit_Button = Button(self, text="Exit", command=self.exitButton, font=self.font)

        # add controls to gridview
        self.label_title.grid(row=0, column=0, padx=10, columnspan=3)
        self.label_full_name.grid(row=1, column=0, padx=10)
        self.label_residency.grid(row=2, column=0, padx=10)
        self.label_program.grid(row=4, column=0, padx=10)
        self.label_courses.grid(row=5, column=0, padx=10)
        self.radioBtn_domestic.grid(row=2, column=1,  padx=10, sticky="w") #sticky="w",
        self.radioBtn_international.grid(row=3, column=1, sticky="w", padx=10)
        self.chkBx_programming.grid(row=5, column=1, padx=10, sticky="w")
        self.chkBx_web.grid(row=6, column=1, padx=10, sticky="w")
        self.chkBx_software.grid(row=7, column=1, padx=10, sticky="w")

        self.cmbBx_programming.grid(row=4, column=1, padx=10, sticky="nsew")

        self.entry_name.grid(row=1, column=1, padx=10, sticky=E+W+N+S)
        self.entry_name.config(width=30)
        self.reset_Button.grid(row=8, column=0, padx=10, pady=10)
        self.reset_Button.config(height=1, width=12)
        self.ok_Button.grid(row=8, column=1, padx=10, pady=10)
        self.ok_Button.config(height=1, width=12)
        self.exit_Button.grid(row=8, column=2, padx=10, pady=10)
        self.exit_Button.config(height=1, width=12)

    def okButton(self):
        try:
            name = self.entry_name.get()
            residency = ""
            if self.radioBtnvalue.get() == 'intl':
                residency = "International"
            if self.radioBtnvalue.get() == 'dom':
                residency = "Domestic"

            program = self.cmbBx_programming.get()
            courses = ""
            if self.comboBtnValue1.get() == 'COMP100':
                courses += "Programming"
            if self.comboBtnValue2.get() == 'COMP213':
                courses += "\nWeb Design"
            if self.comboBtnValue3.get() == 'COMP120':
                courses += "\nSoftware Engineering"
            result = name + "\n" + program + "\n" + residency + "\n" + courses
            messagebox.showinfo(title="Information", message=result)
        
        except Exception:
            messagebox.showinfo(title="Error", message="Please enter valid value.")


    def resetButton(self):
        self.userNameValue.set("Prince Duru")
        self.comboBtnValue1.set("COMP100")
        self.comboBtnValue2.set("COMP213")
        self.comboBtnValue3.set(0)
        self.cmbBx_programming.set('AI')
      


    # exit button event
    def exitButton(self):
        App.destroy()

    
    def resizeApp(self):
        item_list = [self.label_title, self.label_full_name, self.label_residency, self.label_program, self.label_courses, \
        self.radioBtn_domestic, self.radioBtn_international, self.chkBx_programming, self.chkBx_web, self.chkBx_software, \
        self.cmbBx_programming, self.entry_name, self.reset_Button, self.ok_Button, self.exit_Button]
        
        Grid.columnconfigure(appFrame, self.column_number, weight=1)

        for item in item_list:
            Grid.rowconfigure(appFrame, self.row_number, weight=1)
            self.row_number += 1

App = Tk()
App.title("Centennial College")

appFrame = SurveyApp(App)
appFrame.pack(padx=8, pady=7,expand=YES, fill=BOTH)
appFrame.resizeApp()
appFrame["background"] = "#4EA004"

if __name__ == "__main__":

    # Create GUI
    App.mainloop()

