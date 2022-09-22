from tkinter import *
from GUI_login import GUI
from database import Database
#1 - first of all enter database name
#2 - secondly enter your username of login in database 
#3 - thiedly enter your password of login  in database
#4 - enter your ip localhost (defult = 127.0.0.1 )  
db_connection= Database("", "", "", "127.0.0.1")
root = Tk()
gui = GUI(root,db_connection)
def find_gui(item):
    if item == "creat":
        gui.gui_creat()
    if item == "login":
        gui.gui_login()

root.title('confirm')
root.resizable(False, False)
root.geometry("500x400")
root.attributes('-fullscreen',False)
root.config(bg="#447c84")
frame = Frame(root, padx=20, pady=20)
frame.pack(expand=True)

def show():
    
        la_Creat_new_acc=Label(frame,text="Creat new account",font=("Times", "24", "bold"))
        bu_Creat_new_acc = Button(frame,text="start", padx=10, pady=10, relief=SOLID,command=lambda:find_gui("creat") ,font=("Times", "14", "bold"))
        la_login_form=Label(frame,text="login in account",font=("Times", "24", "bold"))
        bu_login_form=Button(frame,text="start", padx=10, pady=10, relief=SOLID,command=lambda:find_gui("login"), font=("Times", "14", "bold"))
        la_Creat_new_acc.grid(row=1,column=0,padx=50,pady=10)
        bu_Creat_new_acc.grid(row=1,column=1)
        la_login_form.grid(row=2,column=0,padx=50,pady=10)
        bu_login_form.grid(row=2,column=1)

show()
root.mainloop()

