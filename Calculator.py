print("Simple Calculator for + - * /")

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mult(a,b):
    return(a*b)

def div(a,b):
    if b==0:
        return(-1)
    else:
        return(a/b)

print("Please select operation -\n"+
    "Press 1) Add\n"+
    "Press 2) Subtract\n"+
    "Press 3) Multiply\n"+
    "Press 4) Divide\n")

choice = int(input("Enter your choice : "))

a = float(input("Enter Number a : "))
b = float(input("Enter Number b : "))

if choice == 1:
    print(a, " + ", b, " = ",add(a, b))
  
elif choice == 2:
    print(a, " - ", b, " = ",sub(a, b))
  
elif choice == 3:
    print(a, " * ", b, " = ",mult(a, b))
  
elif choice == 4:
    if div(a,b)==-1:
        print(a," Cannot be divided by ",b)
    else:
        print(a, " / ", b, " = ",div(a, b))

else:
    print("Invalid input")

