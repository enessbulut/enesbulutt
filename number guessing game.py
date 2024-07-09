import random
test=3
number=random.randint(0,20)
result=int(input("You need to guess numbers between 1-20\nYou have 3 rights\nenter a number:"))
while test>0:
    if number == result:
        print("you guessed the number correctly.")
        break
    if number<result:
        result=int(input("Your guess is wrong. You should guess a smaller number"))
    if number>result:
        result=int(input("Your guess is wrong. You should guess a larger number."))
    test-=1
print("Goodbye!")