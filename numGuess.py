import random

x = random.randrange(10,500,113)

number = input("Enter a number:")
while(number != x):
    if number > x:
        print("your input is greater than actual number")
    else:
        print("your input is smaller than actual number")
    
    number = input("Enter your number Again:")
    if number == x:
        print("yehhh you entered right number")




