print("****************  CALCULATOR  ****************")

num1 = float(input("Enter the first number:")) 
num2 = float(input("Enter the second number:")) 

print("Enter 1 for 'Addition'\nEnter 2 for 'Subtraction'\nEnter 3 for 'Multiplication'\nEnter 4 for 'Division'\nEnter 5 for 'Modulus'\nEnter 6 for 'Exponential'\nEnter 7 for 'Floor Division'")

Entered_number = int(input("choose a number from 1 to 7:"))

if Entered_number == 1:
    print("Addition of your first & second number is: ", num1 + num2)
    
elif Entered_number == 2:
    print("Subtraction of your first & second number is: ", num1 - num2)
    
elif Entered_number == 3:
    print("Multiplication of your first & second number is: ", num1 * num2)
    
elif Entered_number == 4:
    print("Division of your first & second number is:", num1 / num2)
    
elif Entered_number == 5:
    print("Modulus of your first & second number is:", num1 % num2)

elif Entered_number == 6:
    print("Exponential of your first & second number is:", num1 ** num2)

elif Entered_number == 7:
    print("Floor Division of your first & second number is:", num1 // num2)

else:
    print("Invalid Input")