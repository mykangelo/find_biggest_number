#Ask user for 3 numbers. Find and print the biggest number using only if statement

#ask user for 3 numbers
first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))
third_num = int(input("Please enter the third number: "))

#using only the if statement, find the biggest number
if first_num >= second_num and first_num >= third_num:
    print("The biggest number is: ", first_num)
elif second_num >= first_num and second_num >= third_num:
    print("The biggest number is : ", second_num)
else:
    print("The biggest number is", third_num)


    
    
            