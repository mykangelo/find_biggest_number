#Ask user for 3 numbers. Find and print the biggest number using only if statement

import tkinter as tk

#for invalid input
def valid_input(entry_widget):
    while True:
        try:
            user_input = float(entry_widget.get())
            return user_input
        except ValueError:
            print("Error", "Please enter a valid number.")

def find_biggest_number():
    try:
        first_num = valid_input()
        second_num = valid_input()
        third_num = valid_input()

        if first_num >= second_num and first_num >= third_num:
            print(text="The biggest number is: {}".format(first_num))
        elif second_num >= first_num and second_num >= third_num:
            print(text="The biggest number is: {}".format(second_num))
        else:
            print(text="The biggest number is: {}".format(third_num))

    except ValueError:
        print("Error", "Please enter valid numbers.")

#for the GUI window
window = tk.Tk()
window.title("Find the Biggest Number")

label = tk.Label(window, text= " ")


button = tk.Button(window, text="result", command=valid_input)


label.grid(row=0, column=0, pady=10)
button.grid(row=1, column=0, pady=10)

window.mainloop()

    
    
            