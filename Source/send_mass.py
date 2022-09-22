import requests
import random
code_maker = random.randint(1000,1000000)
reset_pa = random.randint(1000,1000000)
c = code_maker
y = reset_pa
#in default code print OTP in terminal 
#if you want code send your number you need a access 
#if you have access enter your url access in url_enter
def number1(f):
    num1 = f
    start_send_code(num1=num1)

def number2(s):
    num2 = s
    reset_pass(num2=num2)

def start_send_code(num1):
    c
    print(c)
    #url_enter = ''
    #paramss= { 'receptor': num1, 'message' :f'Code:{c} .برای ورود کد زیر را وارد کنید '} 
    #jav = requests.post(url_enter,data=paramss)
    #print(jav)
def reset_pass(num2):
    y
    print(y)
    #url_enter = ''
    #paramss= { 'receptor': num2, 'message' :f'Code:{y} .برای ورود کد زیر را وارد کنید '} 
    #jav = requests.post(url_enter,data=paramss)
    #print(jav)

