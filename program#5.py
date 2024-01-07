#Ask user for 3 numbers. Find and print the biggest number using only if statement

import tkinter as tk

def valid_input(entry_widget):
    try:
        user_input = float(entry_widget.get())
        return user_input
    except ValueError:
        show_error("Please enter a valid number.")
        entry_widget.delete(0, tk.END)  # to clear the entry widget
        window.after(2000, clear_error)  # to clear the error message
        return None

def show_error(message):
    error_label.config(text=message, fg="red")

def clear_error():
    error_label.config(text="")

def find_largest_number():
    clear_error()  # to clear any previous error messages
    try:
        first_num = valid_input(entry1)
        second_num = valid_input(entry2)
        third_num = valid_input(entry3)

        if first_num is not None and second_num is not None and third_num is not None:
            if first_num >= second_num and first_num >= third_num:
                result_label.config(text="The biggest number is: {}".format(first_num))
            elif second_num >= first_num and second_num >= third_num:
                result_label.config(text="The biggest number is: {}".format(second_num))
            else:
                result_label.config(text="The biggest number is: {}".format(third_num))

    except ValueError as e:
        show_error(str(e))

# for main window
window = tk.Tk()
window.title("Find the Biggest Number")

# for the input's widget
entry1 = tk.Entry(window, width=10)
entry2 = tk.Entry(window, width=10)
entry3 = tk.Entry(window, width=10)

# for labels
label1 = tk.Label(window, text="First Number:")
label2 = tk.Label(window, text="Second Number:")
label3 = tk.Label(window, text="Third Number:")
result_label = tk.Label(window, text="Result will be displayed here.")

# for the result botton
calculate_button = tk.Button(window, text="Calculate", command=find_largest_number)

# for error label
error_label = tk.Label(window, text="", fg="red")

# for widgets grid layout
label1.grid(row=0, column=0, pady=5)
label2.grid(row=1, column=0, pady=5)
label3.grid(row=2, column=0, pady=5)
entry1.grid(row=0, column=1, pady=5)
entry2.grid(row=1, column=1, pady=5)
entry3.grid(row=2, column=1, pady=5)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2, pady=10)
error_label.grid(row=5, column=0, columnspan=2, pady=10)

# initiate main event loop
window.mainloop()


    
    
            