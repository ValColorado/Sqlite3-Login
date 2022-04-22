from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib
from hashlib import blake2b
import tkinter


class createAccount:

    def account():

        #tkinter window
        ws = Tk()
        ws.title('Create New Account')
        ws.geometry('500x400')
        ws.config(bg="#447c84")

        #clear screen
        def clr():
            uname.delete(0, END)
            pwd.delete(0, END)
            addy.delete(0, END)

        #submit registration info
        def submit():

            #hash the password            
            plaintext = pwd.get().encode('utf-8')
            hash_password = hashlib.sha256(plaintext).hexdigest()
 
            #make sure fields aren't empty 
            uname_check = uname.get()
            pwd_check = pwd.get()
            addy_check = addy.get()
            check_count = 0

            if uname_check == "":
                messagebox.showerror('info', "Username can't be empty!")
            else:
                check_count += 1
            if pwd_check == "":
                messagebox.showerror('info', "Password can't be empty!")
            else:
                check_count += 1
            if addy_check == "":
                messagebox.showerror('info', "Address can't be empty!")
            else:
                check_count += 1
            


            # if username, password, and address aren't empty
            if check_count == 3:
                
                con = sqlite3.connect('{database.db}') #enter your sql database here to establish connection 
                c = con.cursor()
                
                con.execute('''create table if not exists table1(
                            username text not null,
                            password text not null);      
                ''')
                con.execute('''create table if not exists table2(
                            username text not null,
                            address text not null);
                                
                ''')

                if c.execute("SELECT * from table1 WHERE(username = :un);",{

                    'un': uname.get(),
                    }).fetchall():
                
                    messagebox.showerror('info','this username has been taken please try another one')
                else:
                    c.execute("insert into table1 VALUES (:username, :password);",{

                        'username': uname.get(),
                        'password': hash_password,
                        })
                    c.execute("insert into table2 VALUES (:username, :address);",{

                        'username': uname.get(),
                        'address': addy.get(),
                        })
                    messagebox.showerror('info','Account has been registed')

                con.commit()
                    
                ws.destroy()
                
        # frames
        frame = Frame(ws, padx=20, pady=20)
        frame.pack(expand=True)

        # labels
        Label(
            frame, 
            text="Create New Account",
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
        Label(
            frame, 
            text='Address:', 
            font=("Times", "14")
            ).grid(row=3, column=0, pady=5)


        # Entry
        uname = Entry(frame, width=30)
        pwd = Entry(frame, width=30,show="*")
        addy = Entry(frame, width=30)

        #placement for text
        uname.grid(row=1, column=1)
        pwd.grid(row=2, column=1)
        addy.grid(row=3, column=1)

        # button 
        clr_btn = Button(frame, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=clr)
        reg_btn = Button(frame, text="Register", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=submit)
        ext_btn = Button(frame, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=lambda:ws.destroy())
        
        #button placement 
        clr_btn.grid(row=6, column=0, pady=20)
        reg_btn.grid(row=6, column=1, pady=20)
        ext_btn.grid(row=6, column=2, pady=20)


        ws.mainloop()   
    