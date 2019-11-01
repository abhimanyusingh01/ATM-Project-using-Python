
# coding: utf-8

# In[5]:


from tkinter import *
from tkinter import messagebox
import sqlite3


ARIAL = ("arial",10,"bold")

class ATM:
    
    def __init__(self,root):
        self.conn = sqlite3.connect("atm_databse.db", timeout=100)
        self.login = False
        self.root = root
        self.header = Label(self.root,text="ATM Interface",bg="#FF7F24",fg="white",font=("arial",20,"bold"))
        self.header.pack(fill=X)
        self.frame = Frame(self.root,bg="#FFFFE0",width=800,height=420)
        
        
        self.ulabel =Label(self.frame,text="Account Number",bg="#FF7F24",fg="white",font=ARIAL)
        self.uentry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.plabel = Label(self.frame, text="Password",bg="#FF7F24",fg="white",font=ARIAL)
        self.pentry = Entry(self.frame,bg="honeydew",show="*",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.button = Button(self.frame,text="LOGIN",bg="#FF7F24",fg="white",font=ARIAL,command=self.verify)
        self.q = Button(self.frame,text="Exit",bg="#FF7F24",fg="white",font=ARIAL,command = self.root.destroy)
        self.ulabel.place(x=145,y=100,width=120,height=20)
        self.uentry.place(x=153,y=130,width=200,height=20)
        self.plabel.place(x=145,y=160,width=120,height=20)
        self.pentry.place(x=153,y=190,width=200,height=20)
        self.button.place(x=195,y=230,width=120,height=20)
        self.q.place(x=480,y=360,width=120,height=20)
        self.frame.pack()
    
    def database_fetch(self):
        self.acc_list = []
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ",(self.ac,))
        for i in self.temp:
            self.acc_list.append("Name = {}".format(i[0]))
            self.acc_list.append("Account No. = {}".format(i[2]))
            self.acc_list.append("Account Type = {}".format(i[3]))
            self.ac = i[2]
            self.acc_list.append("Balance = {}".format(i[4]))

    def verify(self):
        ac = False
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ", (int(self.uentry.get()),))
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.uentry.get():
                ac = True
            elif i[1] == self.pentry.get():
                ac = True
                m = "Welcome {} ".format(i[0])
                self.database_fetch()
                messagebox._show("Login Info", m)
                self.frame.destroy()
                self.MainMenu()
            else:
                ac = True
                m = " Incorrect Pin! Please Enter Valid Pin"
                messagebox._show("Login Info!", m)

        if not ac:
            m = "Incorrect Account Number !"
            messagebox._show("Login Info!", m)


    def MainMenu(self):
        self.frame = Frame(self.root,bg="#FFFFE0",width=800,height=420)
        root.geometry("800x440")
        self.detail = Button(self.frame,text="Account Details",bg="#FF7F24",fg="white",font=ARIAL,command=self.account_detail)
        self.enquiry = Button(self.frame, text="Balance Enquiry",bg="#FF7F24",fg="white",font=ARIAL,command= self.Balance)
        self.deposit = Button(self.frame, text="Deposit Money",bg="#FF7F24",fg="white",font=ARIAL,command=self.deposit_money)
        self.withdrawl = Button(self.frame, text="Withdrawl Money",bg="#FF7F24",fg="white",font=ARIAL,command=self.withdrawl_money)
        self.pinchange = Button(self.frame, text="Change PIN",bg="#FF7F24",fg="white",font=ARIAL,command=self.changepin)
        self.q = Button(self.frame, text="Exit", bg="#FF7F24", fg="white", font=ARIAL, command=self.root.destroy)
        self.detail.place(x=0,y=10,width=180,height=50)
        self.enquiry.place(x=0, y=350, width=180, height=50)
        self.deposit.place(x=620, y=10, width=180, height=50)
        self.withdrawl.place(x=620, y=350, width=180, height=50)
        self.pinchange.place(x=0, y=160, width=180, height=50)
        self.q.place(x=340, y=370, width=120, height=30)
        self.frame.pack()

    def account_detail(self):
        self.database_fetch()
        text = self.acc_list[0]+"\n"+self.acc_list[1]+"\n"+self.acc_list[2]
        self.label = Label(self.frame,text=text,bg="#FF7F24", fg="white",font=ARIAL)
        self.label.place(x=260,y=100,width=300,height=100)
        

    def Balance(self):
        self.database_fetch()
        self.label = Label(self.frame, text=self.acc_list[3],bg="#FF7F24", fg="white",font=ARIAL)
        self.label.place(x=260, y=100, width=300, height=100)
        
    def deposit_money(self):
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#FF6103", fg="white",font=ARIAL)
        self.money_box.place(x=260,y=100,width=200,height=20)
        self.submitButton.place(x=505,y=100,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.deposit_trans)
        
    def deposit_trans(self,flag):
        self.conn.execute("update atm set bal = bal + ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()
        self.label = Label(self.frame, text="Transaction Completed !", bg="#FF7F24", fg="white",font=ARIAL)
        self.label.place(x=260, y=100, width=300, height=100)

    def withdrawl_money(self):
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#FF6103", fg="white",font=ARIAL)
        self.money_box.place(x=260,y=100,width=200,height=20)
        self.submitButton.place(x=505,y=100,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.withdrawl_trans)
        
       
       
    def withdrawl_trans(self,flag):
        self.conn.execute("update atm set bal = bal - ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()
        self.label = Label(self.frame, text="Transaction Completed !", bg="#FF7F24", fg="white",font=ARIAL)
        self.label.place(x=260, y=100, width=300, height=100)
        

        
    
    def changepin(self):
        self.f1 = Frame(self.frame,bg="#FFFFE0",width=800,height=420)
        self.l1=Label(self.f1,text="New Pin",bg="#FF7F24",fg="white",font=ARIAL) 
        self.l1.place(x=350,y=170,width=120,height=20)
        self.o=StringVar()
        self.e2 = Entry(self.f1,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable=self.o)
        self.e2.place(x=310,y=200,width=200,height=20)
        self.l2=Label(self.f1,text="Confirm New Pin",bg="#FF7F24",fg="white",font=ARIAL)
        self.l2.place(x=350,y=240,width=120,height=20)
        self.p=StringVar()
        self.e3 = Entry(self.f1,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white",textvariable=self.p)
        self.e3.place(x=310,y=270,width=200,height=20)
        self.b=Button(self.f1,text="Submit",bg="#FF7F24",fg="white",font=ARIAL)
        self.b.place(x=350,y=320,width=120,height=20)
        self.b.bind("<Button-1>",self.click)
        self.f1.pack()
    
    def click(self,flag):
        
        if self.o.get()!=self.p.get():
            messagebox.showinfo("Output","PIN Do not match. please try again")
        else:
            self.conn.execute("update atm set pass = ? where acc_no = ?",(self.e2.get(),self.ac))
            self.conn.commit()
            messagebox.showinfo("Output","Your Pin has been changed successfully")
            self.f1.destroy()
            self.MainMenu()
        
root = Tk()
root.title("Sign In")
root.geometry("600x420")
obj = ATM(root)
root.mainloop()


