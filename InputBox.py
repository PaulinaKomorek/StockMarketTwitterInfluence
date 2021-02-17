import tkinter as tk
from tkinter import *

class InputBox:


    def __init__(self):  
        self.root = Tk()
        company_label = Label(self.root, text="Company's name")
        self.company_input = Entry(self.root, bd = 5)
        user_label = Label(self.root, text="Twitter user's name")
        self.user_input = Entry(self.root, bd = 5)
        days_label = Label(self.root, text="number of days")
        self.days_input = Entry(self.root, bd = 5)
        submit = Button(self.root, text ="Submit", command = self.submit)
        company_label.pack()
        self.company_input.pack()
        user_label.pack()
        self.user_input.pack()
        days_label.pack()
        self.days_input.pack()
        submit.pack(side =BOTTOM) 
        self.root.mainloop()

    def submit(self):
        self.company_name = self.company_input.get()
        self.user_name = self.user_input.get()
        self.days = self.days_input.get()
        self.root.destroy()

    def get_data(self):
        return (self.company_name, self.user_name, int(self.days))






