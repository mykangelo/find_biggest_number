#Ask user for 3 numbers. Find and print the biggest number using only if statement

#ask user for 3 numbers
firstNum = int(input("Please enter the first number: "))
secondNum = int(input("Please enter the second number: "))
thirdNum = int(input("Please enter the third number: "))

#using only the if statement, find the biggest number
if firstNum >= secondNum and firstNum >= thirdNum:
    print("The biggest number is: ", firstNum)
elif secondNum >= firstNum and secondNum >= thirdNum:
    print("The biggest number is : ", secondNum)
else:
    print("The biggest number is", thirdNum)


    
    
            