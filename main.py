from tkinter import Label,Button,Frame,Tk,SOLID
import sqlite3
from register import createAccount
from login import Login
from tkinter import messagebox


def reg_window(): #register.py
   createAccount.account()

def login_window(): #login.py
#function to open login page
    Login.login_function()


    

def main():

    #tkinter window
    ws = Tk()
    ws.title('LOGIN')
    ws.geometry('700x700')
    ws.config(bg="#447c84")

   
    # frames
    frame = Frame(ws, padx=20, pady=20)
    frame.pack(expand=True)

    #labels
    Label(
        frame, 
        text="MAIN",
        font=("Times", "24", "bold")
        ).grid(row=0, columnspan=3, pady=10)


    # button 
    login_btn = Button(frame, text="Login", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=login_window)
    reg_btn = Button(frame, text="Register", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=reg_window)
    ext_btn = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:ws.destroy())

    login_btn.grid(row=6,column=0,pady=20)
    reg_btn.grid(row=6, column=1, pady=20)
    ext_btn.grid(row=6, column=2, pady=20)


    ws.mainloop()
main()


