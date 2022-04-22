from tkinter import *
import sqlite3
from tkinter import messagebox
import hashlib


class Login:

    def login_function():
    
        #tkinter window
        ws = Tk()
        ws.title('Login')
        ws.geometry('500x400')
        ws.config(bg="#447c84")

        #clear screen
        def clr():
            uname.delete(0, END)
            pwd.delete(0, END)

        def submit():
            
             # Database 
            try:
                con = sqlite3.connect('database.db') #enter your sql database here to establish connection 
                c = con.cursor()
                
                c.execute("Select * from table1")
                for i in c.fetchall():
                    username_db = i[0]
                    password_db = i[1]
            except Exception as ep: 
                messagebox.showerror('',ep)

            u = uname.get()
            p = pwd.get()
            plaintext = p.encode('utf-8')
            hash_password = hashlib.sha256(plaintext).hexdigest()
 

            check_counter=0
            if u == "":
                messagebox.showerror('info', "Username can't be empty!")
            else:
                check_counter += 1
            if p == "":
                messagebox.showerror('info', "Password can't be empty!")
            else:
                check_counter += 1
            if check_counter == 2:
                if c.execute("SELECT * from table1 WHERE(username = :un) AND (password =:pwd);",{

                    'un': uname.get(),
                    'pwd':hash_password,
                    }).fetchall():
                    message = c.execute("Select * from table2 WHERE(username = :un)",{
                        'un': uname.get(),
                    }).fetchone()
                    messagebox.showerror('info',message)
                else:
                    messagebox.showerror('info','INVALID INFO TRY AGAIN')

                ws.destroy()
                
        # frames
        frame = Frame(ws, padx=20, pady=20)
        frame.pack(expand=True)

        # labels
        Label(
            frame, 
            text="Login Page",
            font=("Times", "24", "bold")
            ).grid(row=0, columnspan=3, pady=10)

        Label(
            frame, 
            text='Username:', 
            font=("Times", "14")
            ).grid(row=1, column=0, pady=5)
        Label(
            frame, 
            text='Password:', 
            font=("Times", "14")
            ).grid(row=2, column=0, pady=5)
      
        # Entry
        uname = Entry(frame, width=30)
        pwd = Entry(frame, width=30,show="*")
        


        uname.grid(row=1, column=1)
        pwd.grid(row=2, column=1)


        # button 
        clr_btn = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=clr)
        submit_btn = Button(frame, text="Submit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=submit)
        ext = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:ws.destroy())

        clr_btn.grid(row=6, column=0, pady=20)
        submit_btn.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)


        ws.mainloop()
    