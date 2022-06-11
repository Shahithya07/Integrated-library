from tkinter import *
from tkinter import messagebox, Entry
import pymysql
global issueBtn, labelFrame, lb1, inf1, inf2, inf4, quitBtn, root, Canvas1, status, inf3, check

# please enter your own mysql host username and password
con = pymysql.connect(host="localhost", user="root", password="xxxxx", database="db")
cur = con.cursor()

allBid = []

def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, inf3, inf4, quitBtn, root, Canvas1, status,check

    bid = inf1.get()
    issue_to = inf2.get()
    issued_date = inf3.get()
    return_date = inf4.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    inf3.destroy()
    inf4.destroy()

    extractBid = "select bid from books"
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from books where bid = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "insert into books_issued values ('" + bid + "','" + issue_to + "','" + issued_date + "', '" + \
               return_date + "')"

    updateStatus = "update books set status = 'issued' where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")


    print(bid)
    print(issue_to)
    print(issued_date)
    print(return_date)

    allBid.clear()


def issueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, inf3, inf4, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#EBBED1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Student Name: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # date button
    lb3 = Label(labelFrame, text="Issued date : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.6)

    inf3 = Entry(labelFrame)
    inf3.place(relx=0.3, rely=0.6, relwidth=0.62)
    l = Label(labelFrame, text="*Please enter the date in YYYY/MM/DD Format", bg='black', fg='white')
    l.place(relx=0.3, rely=0.7)

    # return date
    lb4 = Label(labelFrame, text="Return date : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.8)

    inf4 = Entry(labelFrame)
    inf4.place(relx=0.3, rely=0.8, relwidth=0.62)
    l = Label(labelFrame, text="*Please enter the date in YYYY/MM/DD Format", bg='black', fg='white')
    l.place(relx=0.3, rely=0.9)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
