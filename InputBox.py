from tkinter import *
from tkinter.ttk import *
from models.Form import Form

def validate_days(text: str):
    return text.isdigit()

class InputBox:

    def __init__(self, sms, ts):
        self.sms = sms
        self.ts = ts
        self.root = Tk()
        self.root.geometry('300x220')
        style = Style()
        self.root.iconphoto(False, PhotoImage(file='icon.png'))
        self.root.configure(background='#1DA1F2')
        style.configure("TButton", foreground="white", background="#1DA1F2")
        style.configure('TLabel', foreground='white', background="#1DA1F2")
        style.configure('TEntry', foreground='1DA1F2', background="white")
        company_label = Label(self.root, text="Company's name")
        self.company_input = Entry(self.root, justify=CENTER)
        user_label = Label(self.root, text="Twitter user's name")
        self.user_input = Entry(self.root, justify=CENTER)
        days_label = Label(self.root, text="number of days")
        validate_days_command = self.root.register(validate_days)
        self.days_input = Entry(self.root, justify=CENTER, validate="key", validatecommand=(validate_days_command,'%S'))
        submit = Button(self.root, text="Submit", command=self.submit)
        self.error_label = Label(self.root, text="")
        company_label.pack()
        self.company_input.pack()
        user_label.pack()
        self.user_input.pack()
        days_label.pack()
        self.days_input.pack()
        self.error_label.pack()
        submit.pack(side=BOTTOM)
        self.root.mainloop()

    def submit(self):
        self.sms.index_name = self.company_input.get()
        self.ts.user_name = self.user_input.get()
        if self.sms.validate() and self.ts.validate() and len(self.days_input.get())>0:
            self.sms.days = int(self.days_input.get())
            self.ts.days = int(self.days_input.get())
            self.root.destroy()
        else:
            self.error_label['text'] = "Company name, user name or/and number of fays may be invalid"
        

