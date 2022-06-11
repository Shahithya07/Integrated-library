from datetime import date
import smtplib
from email.message import EmailMessage

from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from Register import *
import pymysql

num = []
data = []
Ids = []
Num = []
IssuedDate = []
details =[]

# please enter your own mysql host username and password
con = pymysql.connect(host="localhost", user="root", password="xxxxx", database="db")
cur = con.cursor()

def check_reg_num(register_number,PassWord):
    num.clear()
    Pass=[]
    cur.execute("select register_number from student")
    for i in cur:
        num.append(i[0])
    if register_number in num:
        cur.execute("SELECT password FROM student")
        for i in cur:
            Pass.append(i[0])
        if PassWord in Pass:
            return True
        else:
            Tk().withdraw()
            messagebox.askretrycancel("ERROR", "WRONG PASSWORD")
            return False
    else:
        Tk().withdraw()
        messagebox.askokcancel("Error", "No register number found")


def check_id():
    if Info1.get() != "":
        register_number = int(Info1.get())
        PassWord = Info2.get()
        state = check_reg_num(register_number, PassWord)
        if state:
            library()
        else:
            messagebox.askretrycancel("ERROR", "No User found Please register")
    else:
        messagebox.showinfo("ERROR","please enter the register number")

def library():
    global headingFrame1, headingLabel, btn1, btn2

    root3 = Tk()
    root3.title("Library")
    root3.minsize(width=400, height=400)
    root3.geometry("600x500")

    Canvas4 = Canvas(root3)
    Canvas4.config(bg="#D5C790")
    Canvas4.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root3, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to the Library", bg='black', fg='white',font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(root3, text="Add Book Details", bg='black', fg='white', command=add_book)
    btn1.place(relx=0.10, rely=0.4, relwidth=0.35, relheight=0.1)

    btn2 = Button(root3, text="Delete Book", bg='black', fg='white', command=delete)
    btn2.place(relx=0.10, rely=0.5, relwidth=0.35, relheight=0.1)

    btn3 = Button(root3, text="View Book List", bg='black', fg='white', command=View)
    btn3.place(relx=0.10, rely=0.6, relwidth=0.35, relheight=0.1)

    btn4 = Button(root3, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
    btn4.place(relx=0.10, rely=0.7, relwidth=0.35, relheight=0.1)

    btn5 = Button(root3, text="Return Book", bg='black', fg='white', command=returnBook)
    btn5.place(relx=0.10, rely=0.8, relwidth=0.35, relheight=0.1)

    btn6 = Button(root3, text="Edit the Student's details", bg='black', fg='white', command=student_details)
    btn6.place(relx=0.55 , rely=0.4 , relwidth=0.35 ,relheight=0.1)

    root3.mainloop()

def update():
    reg_num = Info1.get()
    name = Info2.get()
    emailId = Info3.get()
    phoneNumber = Info4.get()

    try:
        cur.execute(
            "update student set register_number ='" + reg_num + "',name='" + name + "',emailId='" + emailId + "',PhoneNumber='" + phoneNumber + "' where register_number='" + reg_num + "'")
        con.commit()
        messagebox.showinfo('Success', "Updated Successfully")
    except:
        messagebox.showinfo('Error', "Can't add data into database")

    print(reg_num)
    print(name)
    print(emailId)
    print(phoneNumber)

def edit():
    global Info1, Info2, Info3, Info4
    root2 = Tk()
    root2.title("Library")
    root2.minsize(width=400, height=400)
    root2.geometry("600x500")

    Canvas3 = Canvas(root2)
    Canvas3.config(bg="#99BBD4")
    Canvas3.pack(expand=True, fill=BOTH)

    headingFrame = Frame(root2, bg="#FFBB00", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel2 = Label(headingFrame, text="Edit", bg='black', fg='white', font=('Courier', 15))
    headingLabel2.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelframe2 = Frame(root2, bg='black')
    labelframe2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    student = "select * from student where register_number=4077"
    cur.execute(student)
    for x in cur:
        for y in range(0, 4):
            details.append(x[y])

    l21 = Label(labelframe2, text="Register Number ", bg='black', fg='white')
    l21.place(relx=0.10, rely=0.2, relheight=0.08)

    Info1 = Entry(labelframe2, text=details[0], bg='white', fg='black')
    Info1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    l22 = Label(labelframe2, text="Name ", bg='black', fg='white')
    l22.place(relx=0.10, rely=0.35, relheight=0.08)

    Info2 = Entry(labelframe2, text=details[1], bg='white', fg='black')
    Info2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    l23 = Label(labelframe2, text="EmailId ", bg='black', fg='white')
    l23.place(relx=0.10, rely=0.50, relheight=0.08)

    Info3 = Entry(labelframe2, text=details[2], bg='white', fg='black')
    Info3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    l24 = Label(labelframe2, text="Phone Number  ", bg='black', fg='white')
    l24.place(relx=0.10, rely=0.65, relheight=0.08)

    Info4 = Entry(labelframe2, text=details[3], bg='white', fg='black')
    Info4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    EditBtn = Button(root2, text="Edit", bg='#f7f1e3', fg='black', command=update)
    EditBtn.place(relx=0.3, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_btn = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root2.mainloop()

def student_details():
    root1 = Tk()
    root1.title("Library")
    root1.minsize(width=400, height=400)
    root1.geometry("600x500")

    Canvas2 = Canvas(root1)
    Canvas2.config(bg="#A3D8D2")
    Canvas2.pack(expand=True, fill=BOTH)

    headingFrame2 = Frame(root1, bg="#FFBB00", bd=5)
    headingFrame2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel1 = Label(headingFrame2, text="Student Details", bg='black', fg='white', font=('Courier', 15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelframe1 = Frame(root1, bg='black')
    labelframe1.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    reg=Info1.get()
    student = "select * from student where register_number='" + reg +"'"
    cur.execute(student)
    for i in cur:
        for j in range(0, 4):
            details.append(i[j])

    l1 = Label(labelframe1, text="Register Number ", bg='black', fg='white')
    l1.place(relx=0.10, rely=0.2, relheight=0.08)

    stInfo1 = Label(labelframe1, text=details[0], bg='white', fg='black')
    stInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    l2 = Label(labelframe1, text="Name ", bg='black', fg='white')
    l2.place(relx=0.10, rely=0.35, relheight=0.08)

    stInfo2 = Label(labelframe1, text=details[1], bg='white', fg='black')
    stInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    l3 = Label(labelframe1, text="EmailId ", bg='black', fg='white')
    l3.place(relx=0.10, rely=0.50, relheight=0.08)

    stInfo3 = Label(labelframe1, text=details[2], bg='white', fg='black')
    stInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    l4 = Label(labelframe1, text="Phone Number  ", bg='black', fg='white')
    l4.place(relx=0.10, rely=0.65, relheight=0.08)

    stInfo4 = Label(labelframe1, text=details[3], bg='white', fg='black')
    stInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    EditBtn = Button(root1, text="Edit", bg='#f7f1e3', fg='black', command=edit)
    EditBtn.place(relx=0.3, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn1 = Button(root1, text="Quit", bg='#f7f1e3', fg='black', command=root1.destroy)
    quitBtn1.place(relx=0.5, rely=0.9, relwidth=0.18, relheight=0.08)

    root1.mainloop()

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

Canvas1 = Canvas(root)
Canvas1.config(bg="#808080")
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="LOGIN", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

labelframe = Frame(root, bg='black')
labelframe.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

lb1 = Label(labelframe, text="Register number ", bg='black', fg='white')
lb1.place(relx=0.05, rely=0.2, relheight=0.08)

Info1 = Entry(labelframe)
Info1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.10)

lb2 = Label(labelframe, text="Password",bg='black', fg='white')
lb2.place(relx=0.05, rely=0.4, relheight=0.08)

Info2 = Entry(labelframe)
Info2.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.10)

btn1 = Button(root, text="LOGIN", bg='white', fg='black', command=check_id)
btn1.place(relx=0.35, rely=0.50, relwidth=0.30, relheight=0.08)

labelframe = Frame(root, bg="black")
labelframe.place(relx=0.30, rely=0.65, relwidth=0.4, relheight=0.1)

lb2 = Label(labelframe, text="Don't have an account?", bg="black", fg="white")
lb2.place(relx=0.3, rely=0.3, relwidth=0.45,relheight=0.40)

btn2 = Button(root, text="REGISTER", bg='white', fg='black', command=register)
btn2.place(relx=0.35, rely=0.8, relwidth=0.30, relheight=0.08)

root.mainloop()

now = date.today()
query = "select name from books_issued where returnDate = '" + str(now) + "'"
cur.execute(query)
for i in cur:
    data.append(i[0])
if not data:
    print("No books to be returned in today's date")

for i in data:
    EmailId = "select emailId from student where name ='" + i + "'"
    cur.execute(EmailId)
    for j in cur:
        Ids.append(j[0])

for i in data:
    phone_number= "select PhoneNumber from student where name = '" + i + "'"
    cur.execute(phone_number)
    for j in cur:
        Num.append(j[0])

if not Ids == []:
    for i in data:
        msg = EmailMessage()
        msg.set_content("""
        
        This reminder is regarding the books you have borrowed in our library.
        We humbly request you to return those books any moment from the day you received this message. 
        
        Thank you.
        """)
        msg['subject'] = "Reminder"
        msg['to'] = Ids
        
        # enter your own emailId and password
        user = "xxxxxx@gmail.com"
        msg['from'] = user
        password = "aaaa"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        print("Email sent!!")
        server.quit()
else:
    print("EmailIds not found")
    
 if not Num == []:
    for i in Num:
        msg = EmailMessage()
        msg.set_content("""
        This reminder is regarding the books you have borrowed in our library.
        We humbly request you to return those books any moment from the day you received this message.

        Thank you.
                """)
        msg['subject'] = "Reminder"
        msg['to'] = i+"@sms.clicksend.com"

        #enter your own emailId and password
        user = "xxxxxxx@gmail.com"
        msg['from'] = user
        password = "aaaaa"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
    print("Messages Sent")
else:
    print("PhoneNumbers not found")
