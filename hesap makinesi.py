data=int(input("Select the operation you will perform: 1-Addition 2-Subtraction 3-Multiplication 4-Division")) 
number1=int(input("enter the 1st number:"))
number2=int(input("enter the 2st number:"))
if(data==1):
    result=number1+number2
elif(data==2):
    result=number1-number2
elif(data==3):
    result=number1*number2
else: 
    result=number1/number2
print(result)

