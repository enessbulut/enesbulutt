password=input("enter password.")
low=False  
long=False
up=False
num=False
special=False
while long==False:
   if (len(password)>=7):
        long=True
   else:
     password=input("enter a longer password")
while low==False:
    if password.islower():
        password=input("use capital letters")
    else:
        low=True
while up==False:
    if password.isupper():
        password=input("use lowercase letters")
    else:
        up=True
while num==False:
    if password.isnumeric():
        password=input("add letters")
    else:
        num=True
while special==False:
    if password.count("@")>0 or password.count("*")>0 or password.count("#")>0 or password.count("$")>0 or password.count("%")>0 or password.count("&")>0 or password.count(".")>0:
        special=True
    else:
        password=input("use special characters")
if (len(password)>=7) and password.islower()==False and password.isupper()==False and num==True and special==True:
   print("Congratulations, you have created a strong password")
else:
   password=input("try creating password again")

   
   
