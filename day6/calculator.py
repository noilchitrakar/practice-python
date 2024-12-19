#claculator

def addition(a,b):     #parameter   (recives the value)
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divison(a,b):
    return a/b
def modulas(a,b):
    return a%b
def floorDivison(a,b):
    return a//b
def exponent(a,b):
    return a**b


print("Use The calculator")    

while 1:
    print('''enter 1 to use the calculator \nenter 2 to quit the calculator
    ''')
    user_input=int(input("Enter the choice you want between 1 and 2 : "))
    if user_input==1:
        fist=int(input("enter the first number"))
        second=int(input("enter the second number"))
        print("which operation do you want to perform")
        operation=input('''enter the opeartion you want
        for addition(+)
        for subtraction(-)
        for multiplication(*)
        for divison(/)
        for modulas(%)
        for Floor divison(//)
        for exponent(**)
        ''')
        if operation=='+':
            print(addition(fist,second))#argument (sends the value to the function)
        elif operation=='-':
            print(subtraction(fist,second))#argument (sends the value to the function)
        elif operation=='*':
            print(multiplication(fist,second))#argument (sends the value to the function)
        elif operation=='/':
            print(divison(fist,second))#argument (sends the value to the function)
        elif operation=='%':
            print(modulas(fist,second))#argument (sends the value to the function)
        elif operation=='//':
            print(floorDivison(fist,second))#argument (sends the value to the function)
        elif operation=='**':
            print(exponent(fist,second))#argument (sends the value to the function)
        else:
            print("please enter a valid opeation")
    elif user_input==2:
        print("Thanks for using the calculator")
        break
    else:
        print("please enter a valid choice between 1 and 2")
        
