#simplecalulator

num1 = float(input("Enter number 1 :"))
num2 = float(input("Enter number 2 :"))

#Tothecalculations

print("1: Addition , 2 : substraction , 3 : division , 4 : multiplication ")
 
X = input("What action do want to perform with the entered numbers answer theough numbers ")

if X==1 :
    print("Sum of numbers is :",num1+num2)

if X==2 :
    if num1 >= num2 :
        print("Substraction of num1 by num2 is :",num1-num2)
    else :
        print("substraction of num2 by num1 is :",num2-num1)

if X==4 :
    print("Multiplication of both numbers is :",num1*num2)

if X==3 : 
    if num2==0 :
        print("Sorry invalid entry")
    else :
        print("division of num1 by num2 is :",num1/num2)
            