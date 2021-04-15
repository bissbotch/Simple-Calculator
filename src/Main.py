from Calculator import addition
from Calculator import subtraction
from Calculator import multiplication
from Calculator import division

def getInputs():
    num1 = input("Enter a number: \n")
    num2 = input("Enter a number \n")
    
    return num1, num2

def CalcMenu():
    print("Welcome to the calculator :) \n\n")
    print("***** Calculator Menu ***** \n")
    print ("1) Addition\n 2) Subtraction\n 3) Multiplication\n 4) Division \n")
    calcType = input("What type of calculation do you want to do? \n")
    
    if calcType == 1:
        Calculator.addition()
    
    elif calcType == 2:
        Calculator.subtraction()
        
    elif calcType == 3:
        Calculator.multiplication()
        
    elif calcType == 4:
        Calculator.division()
    
    else:
        print("Please enter a valid option\n")

def Main():
    getInputs()
    CalcMenu()
    