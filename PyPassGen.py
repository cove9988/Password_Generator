#!/usr/bin/python
# Programmed by P.B.Surya.Subhash
#Random program to test my skills ! :D
#This will generate Random strong passwords for you ! :)

import random

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []

length = input("Hey, Welcome. Just say me how many characters do you want in your password ?")
length = int(length)

#randomly select ascii character classes and individual characters

while count < length:
    rand = random.randint (0,3)
    if rand == 0:
        lower += 1
        b = int(random.randint (97,122))
        password.append(b)
    elif rand == 1:
        upper += 1
        b = random.randint (65,90)
        password.append(b)
    elif rand == 2:
        number += 1
        b = random.randint (48,57)
        password.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            b = random.randint (33,47)
            password.append(b)
        elif r == 1:
            b = random.randint (91,96)
            password.append(b)
        elif r == 2:
            b = random.randint (123,125)
            password.append(b)
    count += 1

#convert ascii code to characters
word = "".join([chr(c) for c in password])

#print the result
print ("Random",length,"character password =      ",word,"")
print ("It contains",lower,"lowercase,",upper,"uppercase,",number,"numbers and",symbol,"symbol characters")
