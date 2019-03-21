from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import smtplib

Sender = "senderemail@email.com"
pwd="password"
Reciver = "reciveremail@email.com"

#msg
info = "Hello World!!   "

#DES3
def des3():
    cipher = DES3.new(get_random_bytes(24))
    encryD3 = cipher.encrypt(info)
    return "DES3 Encryption ",encryD3

#DES
def des():
    cipher = DES.new(get_random_bytes(8))
    encryD = cipher.encrypt(info)
    return "new DES Encryption ",encryD

#AES
def aes():
    cipher = AES.new(get_random_bytes(32))
    encryA = cipher.encrypt(info)
    return "NEW AES Encryption ",encryA

#Combine Msg
z=aes()
print(z)
y=des()
print(y)
x=des3()
print(x)
x3=z+y+x
mylist = list(x3)
print(mylist)
# writing encrypted msg in file bcoz it is in byte fromat
with open("output2.txt","w") as f:
    f.write(" ".join(map(str,mylist)))
    f.write("\n")
#reading file and convert it in single string but still google identify it is byte
with open("output2.txt","r") as f:
    msg=f.readlines()
print(msg)
#convert string further string so it cannot detect as byte now google can not identify it is byte 
mymsg="My msg is ".join(msg)
print(mymsg)
# sending mail
try:

    smtpobj = smtplib.SMTP('smtp.gmail.com',587)    
    smtpobj.starttls()
    smtpobj.login(Sender,pwd)
    
    smtpobj.sendmail(Sender,Reciver,mymsg)
    print("Mail Send")
    smtpobj.quit()
except Exception as ex:
    print("Failed",ex)
    
