from tkinter import * 
from tkinter import messagebox
from send_mass import *

class GUI:
    def __init__(self,t1,db_connection):
        self.t1=t1
        self.db_connection =db_connection
    
    def delete(self):
        self.fname.delete(0, 'end')
        self.lname.delete(0, 'end')
        self.phn.delete(0, 'end')
        self.em.delete(0, 'end')
        self.passw.delete(0, 'end')

    def res_pass_num(self):
        ne=self.number_ent.get()
        number2(s=ne)

    def forgotpass(self):
        top = Toplevel()
        top.resizable(False, False)
        top.title('Reset Password')
        Label(top,text="      Reset Password ",font=("Times", "20", "bold")).grid(row=0,column=0, columnspan=3, pady=5)
        Label(top,text="Enter your number",font=("Times", "13")).grid(row=1,column=0, pady=5)
        Label(top,text='Enter OTP', font=("Times", "13")).grid(row=2, column=0, pady=5)
        self.number_ent = Entry(top, width=30)
        self.number_ent.grid(row=1, column=1)
        self.RES_ENT = Entry(top, width=30)
        self.RES_ENT.grid(row=2, column=1)
        bu_login = Button(top, text="Check", padx=15, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=lambda:self.OTP_check(a=2))
        bu_login.grid(row=6, column=2, pady=20)
        bu_forgotpass = Button(top, text="send OTP", padx=12, pady=1,command=lambda:self.res_pass_num())
        bu_forgotpass.grid(row=2, column=2, pady=20)
        bu_ext = Button(top, text="exit", padx=18, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=top.destroy)
        bu_ext.grid(row=6, column=0, pady=20)

    def rest_passw(self):
        top = Toplevel()
        top.resizable(False, False)
        top.title('Reset Password')
        Label(top,text="      Reset Password ",font=("Times", "20", "bold")).grid(row=0,column=0, columnspan=3, pady=5)
        Label(top,text="Enter the new password",font=("Times", "13")).grid(row=1,column=0, pady=5)
        Label(top,text='Enter again', font=("Times", "13")).grid(row=2, column=0, pady=5)
        self.ent_passw = Entry(top, width=30)
        self.ent_passw.grid(row=1, column=1)
        self.ent_passw_again = Entry(top, width=30)
        self.ent_passw_again.grid(row=2, column=1)
        bu_login = Button(top, text="Check", padx=15, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=lambda:self.res_passw_number())
        bu_login.grid(row=6, column=2, pady=20)
        bu_ext = Button(top, text="exit", padx=18, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=top.destroy)
        bu_ext.grid(row=6, column=0, pady=20)

    def OTP_check(self,a):
        if a == 1:
            x=self.OTP_ENT.get()
            if int(x) == int(c):
                self.check_confirm()
            if int(x) != int(c):
                messagebox.showerror('OTP error', 'Error: pleas inter correct OTP CODE!')
        if a == 2:
            n=self.RES_ENT.get()
            if int(n) == int(y):
                self.rest_passw()
            if int(n) != int(y):
                messagebox.showerror('OTP error', 'Error: pleas inter correct OTP CODE!')   
  
    def Confirm_number(self):
        self.nee = self.phn.get()        
        top = Toplevel()
        top.resizable(False,False)
        top.title('Confirmation number')
        Label(top,text="Confirmation number",font=("Times", "20", "bold")).grid(row=0, columnspan=3, pady=5)
        Label(top,text=f"OTP send to {int(self.nee)}",font=("Times", "18", "bold")).grid(row=1, columnspan=3, pady=10)
        Label(top,text='Enter OTP ', font=("Times", "14")).grid(row=2, column=0, pady=5)
        self.OTP_ENT = Entry(top, width=30)
        self.OTP_ENT.grid(row=2, column=1)
        bu_login = Button(top, text="Check", padx=15, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=lambda:self.OTP_check(a=1))
        bu_login.grid(row=6, column=2, pady=20)
        bu_forgotpass = Button(top, text="send OTP", padx=12, pady=1,command=lambda:number1(f=self.nee))
        bu_forgotpass.grid(row=2, column=2, pady=20)
        bu_ext = Button(top, text="exit", padx=18, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=top.destroy)
        bu_ext.grid(row=6, column=0, pady=20)


    def check_and_confirm(self):
        email=self.em.get()
        name=self.fname.get()
        password=self.passw.get()
        email_check = email.find("@gmail.com")
        print(email_check)
        if len(name) < 4:
            messagebox.showerror('NAME limit', 'Error: NAME words cannot be less than 3!')
            return
        if len(password) < 6:
            messagebox.showerror('PASSWORD limit', 'Error: PASSWORDcannot be less than 6!')
            return
        try:
            int(self.phn.get())        
        except ValueError:
                messagebox.showerror('Number fals', 'Error: pleas inter correct number!')
                return
        if email_check >= 10:
               self.Confirm_number()                            
        if email_check == -1:
            messagebox.showerror('login problem', 'Error: Email not correct!')
            
  
    def gui_creat(self):
        top = Toplevel()
        top.resizable(False, False)
        Label(top, text="Create New Accountl",font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(top, text='First Name', font=("Times", "14")).grid(row=1, column=0, pady=5)
        Label(top, text='Last Name', font=("Times", "14")).grid(row=2, column=0, pady=5)
        Label(top, text='Phone number', font=("Times", "14")).grid(row=3, column=0, pady=5)
        Label(top, text='Email Address', font=("Times", "14")).grid(row=4, column=0, pady=5)
        Label(top, text='Password', font=("Times", "14")).grid(row=5, column=0, pady=5)
        self.fname = Entry(top, width=30)
        self.lname = Entry(top, width=30)
        self.em = Entry(top, width=30)
        self.phn =Entry(top,width=30)
        self.passw = Entry(top, width=30,show="•")
        self.fname.grid(row=1, column=1)
        self.lname.grid(row=2, column=1)
        self.phn.grid(row=3,column=1)
        self.em.grid(row=4, column=1)
        self.passw.grid(row=5, column=1)
        clr = Button(top, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=self.delete)
        reg = Button(top, text="Register", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=self.check_and_confirm)
        ext = Button(top, text="Exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=top.destroy)
        clr.grid(row=6, column=0, pady=20)
        reg.grid(row=6, column=1, pady=20)
        ext.grid(row=6, column=2, pady=20)

    def gui_login(self):
        top = Toplevel()
        top.resizable(False, False)
        Label(top, text="Welcome Back",font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
        Label(top, text='Email Address', font=("Times", "14")).grid(row=1, column=0, pady=5)
        Label(top, text='Password', font=("Times", "14")).grid(row=2, column=0, pady=5)
        self.em1 = Entry(top, width=30)
        self.passw1 = Entry(top, width=30,show="•")
        self.em1.grid(row=1, column=1)
        self.passw1.grid(row=2, column=1)
        bu_login = Button(top, text="login", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=self.check_data)
        bu_login.grid(row=6, column=2, pady=20)
        bu_forgotpass = Button(top, text="forgot pass", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=self.forgotpass)
        bu_forgotpass.grid(row=6, column=1, pady=20)
        bu_ext = Button(top, text="exit", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"),command=top.destroy)
        bu_ext.grid(row=6, column=0, pady=20)

    def check_confirm(self):
        name = self.fname.get()
        lname = self.lname.get()
        pnn = self.phn.get()
        email = self.em.get()
        passw = self.passw.get()
        self.db_connection.insert_person(name,lname,pnn,email,passw)
    
    def res_passw_number(self):
        passw1=self.ent_passw.get()
        passw_again=self.ent_passw_again.get()
        if passw1 == passw_again:
            pass_1 = passw1
            number=self.number_ent.get()
            self.db_connection.rest_pas(number,pass_1)
        else:
            messagebox.showerror('Password error', 'Error: Enter same password in two Entry!')  


    def check_data(self):
        email = self.em1.get()
        passw = self.passw1.get()
        self.db_connection.login_check(email,passw)

      
