# Calculator      
class Calculator:
    def addition(self, num1, num2):
        return num1+num2
            
    def subtraction(self, num1, num2):
        return num1-num2

    def multiplication(self, num1, num2):
        return num1*num2

    def division(self, num1, num2):
        return num1/num2

# Main
def Main():
    num1 = int(input("Enter a number: \n"))
    num2 = int(input("Enter a number \n"))
    
    calc = Calculator()
    
    print("Welcome to the calculator :) \n\n")
    print("***** Calculator Menu ***** \n")
    print (" 1) Addition\n 2) Subtraction\n 3) Multiplication\n 4) Division \n")
    calcType = input("What type of calculation do you want to do? \n")
    
    if calcType == "1":
        print("Answer:", calc.addition(num1, num2))
    
    elif calcType == "2":
        print("Answer:", calc.subtraction(num1, num2))
        
    elif calcType == "3":
        print("Answer:", calc.multiplication(num1, num2))
        
    elif calcType == "4":
        print("Answer:", calc.division(num1, num2))
    
    else:
        print("Please enter a valid option\n")
        
Main()
    