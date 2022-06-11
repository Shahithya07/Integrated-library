from tkinter import *
from tkinter import messagebox
import pymysql
global inf1, inf2, inf3, inf4, inf5, Canvas1, root, con, cur, table

def registerId():
    register_number = inf1.get()
    name = inf2.get()
    emailId = inf3.get()
    PhoneNumber = inf4.get()
    password = inf5.get()

    insert = "INSERT INTO student VALUES ('" + register_number + "','" + name + "','" + emailId + "','" + PhoneNumber + "','" + password + "')"
    if not(register_number == "" or name == "" or emailId == "" or PhoneNumber == "" or password == ""):
        cur.execute(insert)
        con.commit()
        messagebox.showinfo('Success', "Registered successfully")
    else:
        messagebox.askretrycancel('Error', "Fill all the details")


def register():
    global root, Canvas1, inf1, inf2, inf3, inf4, inf5, table, con, cur

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # please enter your own mysql host username and password
    con = pymysql.connect(host="localhost", user="root", password="xxxx", database="db")
    cur = con.cursor()

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame2 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame2, text="REGISTER", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb1 = Label(labelFrame, text="Register number", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame, text="Name", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.35, relwidth=0.62)

    lb3 = Label(labelFrame, text="Email ID", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.53)

    inf3 = Entry(labelFrame)
    inf3.place(relx=0.3, rely=0.53, relwidth=0.62)

    lb4 = Label(labelFrame, text="Phone Number", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.7)

    inf4 = Entry(labelFrame)
    inf4.place(relx=0.3, rely=0.7, relwidth=0.62)

    lb5 = Label(labelFrame, text="Password", bg='black',fg='white')
    lb5.place(relx=0.05,rely=0.85)

    inf5 = Entry(labelFrame)
    inf5.place(relx=0.3,rely=0.85,relwidth=0.62)

    subBtn = Button(root, text="Submit", bg='#d1ccc0', fg='black', command=registerId)
    subBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
