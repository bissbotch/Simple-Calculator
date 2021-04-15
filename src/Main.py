def getInputs():
    num1 = input("Enter a number: \n")
    num2 = input("Enter a number \n")
    
    return num1, num2

def CalcMenu(self, num1, num2):
    print("Welcome to the calculator :) \n\n")
    print("***** Calculator Menu ***** \n")
    print ("1) Addition\n 2) Subtraction\n 3) Multiplication\n 4) Division \n")
    calcType = input("What type of calculation do you want to do? \n")
    
    if calcType == 1:
        Calculator.addition(self, num1, num2)
    
    elif calcType == 2:
        Calculator.subtraction(self, num1, num2)
        
    elif calcType == 3:
        Calculator.multiplication(self, num1, num2)
        
    elif calcType == 4:
        Calculator.division(self, num1, num2)
    
    else:
        print("Please enter a valid option\n")

class Calculator:

    def addition(self, num1, num2):
        answer = num1 + num2
        return answer
        
    def subtraction(self, num1, num2):
        answer = num1 - num2
        return answer

    def multiplication(self, num1, num2):
        answer = num1 * num2
        return answer

    def division(self, num1, num2):
        answer = num1 / num2
        return answer
    
    
def Main(self, num1, num2, answer):
    getInputs()
    CalcMenu(self, num1, num2)
    
    print("Answer: ", answer)
    