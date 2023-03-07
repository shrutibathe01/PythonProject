def Addition(a, b):
    result=a + b
    return result

def Substraction(a, b):
    result=a - b
    return result

def Multiplication(a, b):
    result=a * b
    return result

def Division(a, b):
    result=a / b
    return result

def Power(a,b):
    result=a**b
    return result

print("Select Operation That you want to Perform")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Power")

while True:
    choice = input("Enter ypur operation choice:")
    if choice in ('1', '2', '3', '4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            result=Addition(num1,num2)
            print("Addition: {} + {} = {}".format(num1,num2,result))

        elif choice == '2':
            result=Substraction(num1,num2)
            print("Substraction: {} - {} = {}".format(num1,num2,result))

        elif choice == '3':
            result=Multiplication(num1,num2)
            print("Multiplication: {} * {} = {}".format(num1,num2,result))

        elif choice == '4':
            if num2 == 0:
                print("Division by 0 not possible")
            else:
                result=Division(num1,num2)
                print("Division: {} / {} = {}".format(num1,num2,result))
                
        elif choice == '5':
            result=Power(num1,num2)
            print("Multiplication: {} ^ {} = {}".format(num1,num2,result))

        
        Continue=input("Want to continue Y/N: ")
        if Continue.upper()=="N":
            break
    else:
        print("Invalid Input")