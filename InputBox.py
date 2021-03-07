from tkinter import *
from tkinter.ttk import *
from models.Form import Form

def validate_days(text: str):
    return text.isdigit()

class InputBox:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('200x150')
        style = Style()
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
        company_label.pack()
        self.company_input.pack()
        user_label.pack()
        self.user_input.pack()
        days_label.pack()
        self.days_input.pack()
        submit.pack(side=BOTTOM)
        self.root.mainloop()

    def submit(self):
        self.company_name = self.company_input.get()
        self.user_name = self.user_input.get()
        self.days = self.days_input.get()
        self.root.destroy()

    def get_data(self):
        return Form(self.company_name, self.user_name, int(self.days))
