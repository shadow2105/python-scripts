#!/usr/bin/python3

a=34
loe=[]
b=0
print("^^Guess the correct no.^^")
print()
while b<10:
    c=int(input())
    b+=1
    if 0<=c<=100:
        if c<a and c not in range(a-5,a):
            print ("!! Wrong No.","\n","The entered value is lesser than the expected value")
        elif c>a and c not in range(a+1,a+6):
            print ("!! Wrong No.","\n","The entered value is greater than the expected value")
        elif c==a:
            print ("||Entered value matched")
            loe.append(c)
            break
        elif c!=a and c in range(a-5,a+6):
            print ("!! Wrong No.","\n","The entered value is near the expected value")
    else:
        print ("!!!!Invalid Value!!!!")
    loe.append(c)
    print ("")
print("\n")
if c==a:
    print ("**GAME WON**")
else:
    print ("**GAME LOST**")
print ("List of Entries:","\n",loe)
