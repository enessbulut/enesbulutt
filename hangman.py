word="TÜRKİYE"
word1="-------"
list1=list(word)
list2=list(word1)
life=7
test=0
print("Enter capital letters \nYou will try to guess a 7 letter word.")
while test<7:
    result=input("enter a letter")
    if (result in word):
        test+=1
        result1=list1.index(result)
        list2[result1]=result
        print("correct letter")
    else:
        print("wrong letter")
        life-=1
        if life==0:
         break
if list2==["T","Ü","R","K","İ","Y","E"]:
    print("congratulations, you knew the word\ngoodbye")
else:
    print("you didn't guess correctly\ngoodbye")


