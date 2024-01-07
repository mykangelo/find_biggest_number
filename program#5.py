#Ask user for 3 numbers. Find and print the biggest number using only if statement

#for invalid input
def valid_input(prompt):
    while True:
        try: 
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Error: Please enter a valid number. ")
            

#ask user for 3 numbers
first_num = valid_input("Please enter the first number: ")
second_num = valid_input("Please enter the second number: ")
third_num = valid_input("Please enter the third number: ")

#using only the if statement, find the biggest number
if first_num >= second_num and first_num >= third_num:
    print("The biggest number is: ", first_num)
elif second_num >= first_num and second_num >= third_num:
    print("The biggest number is : ", second_num)
else:
    print("The biggest number is", third_num)




    
    
            