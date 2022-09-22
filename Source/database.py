import pymysql
from tkinter import messagebox
import webbrowser
from turtle_login_re import FloweringTree 
from send_mass import *

class Database:
    def __init__(self,database_name,user,password,host):
        self.database_name = database_name
        self.user = user
        self.password = password
        self.host = host
        self.cnn,self.cursor = self.connect_db()
    def connect_db(self):
        cnn = ''
        cursor='' 
        try: 
            cnn = pymysql.connect(host=self.host
                            ,user=self.user,password=self.password
                            ,db=self.database_name
                            )
            cursor = cnn.cursor()
        except:
            print("connection failed")
        finally:
            print("connection ok")
            return cnn , cursor

    def rest_pas(self,number,password):
        query=f"select * from manager_login where phone_number='{number}'"
        data=self.cursor.execute(query)
        if data == 1:
            query1=f"update manager_login set pass='{password}' where phone_number='{number}'"
            self.cursor.execute(query1)
            self.cnn.commit()    
            messagebox.showinfo('Information','Reset password successfully')
        else:
            messagebox.showerror('Unspecified Error', 'Error: This phone number not found in database!') 
            
    def insert_person(self,name,lname,pn,email,passw):
            query=f"INSERT INTO login_creat.manager_login (first_name,last_name,phone_number,email_address,pass) values {name,lname,pn,email,passw}"
            self.cursor.execute(query)        
            self.cnn.commit()
            messagebox.showinfo('Information','Registered successfully')

    def login_check(self,email,passw):
        query1=f"SELECT * FROM login_creat.manager_login where email_address='{email}'"
        query2=f"SELECT * FROM login_creat.manager_login where pass='{passw}'"
        data1=self.cursor.execute(query1)
        data2=self.cursor.execute(query2)
        fix = data1 + data2
        if fix == 0:
            messagebox.showerror('login problem', 'Error: Email or password not correct!') 
        else:
            a_website = "https://github.com/ariandexter"
            webbrowser.open_new(a_website)
            flowering_tree = FloweringTree()
            flowering_tree.draw()   
            messagebox.showinfo('Information','Login successfully')   

