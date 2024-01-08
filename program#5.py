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

# for main window GUI
window = tk.Tk()
window.geometry("451x280")
window.title("Find the Biggest Number") 
window.configure(bg="lightblue1")  

# for fonts
courier_bold = ("Courier", 16)
courier = ("Courier", 14)
title_header = ("OpenSymbol", 18, "bold", ) 

# for title header
title_label = tk.Label(window, text ="BIGGEST NUMBER IDENTIFIER", font=title_header, fg="white", bg="lightskyblue", bd=1, relief=tk.RIDGE)
title_label.grid(row=0, column=0, columnspan=10, pady=0, padx=0, sticky="nsew")

# for input widgets
entry1 = tk.Entry(window, width=20, font=courier)
entry2 = tk.Entry(window, width=20, font=courier)
entry3 = tk.Entry(window, width=20, font=courier)

# for labels
label1 = tk.Label(window, text="First Number :", font=courier_bold, bg="lightblue1")
label2 = tk.Label(window, text="Second Number :", font=courier_bold, bg="lightblue1")
label3 = tk.Label(window, text="Third Number :", font=courier_bold, bg="lightblue1")
result_label = tk.Label(window, text=" ", font=courier, bg="gray87", fg="green", bd=1, relief=tk.SUNKEN)

# for calculate button
find_button = tk.Button(window, text="Find", command=find_largest_number, font=courier_bold, bg="mintcream", padx=0, pady=0)

# for error label
error_label = tk.Label(window, text="", fg="red", bg="lightblue1")

# for widgets grid layout
label1.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
label2.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
label3.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")
entry1.grid(row=1, column=1, pady=5, padx=10, sticky="nsew")
entry2.grid(row=2, column=1, pady=5, padx=10, sticky="nsew")
entry3.grid(row=3, column=1, pady=5, padx=10, sticky="nsew")
find_button.grid(row=4, column=0, columnspan=2, pady=10,)
result_label.grid(row=5, column=0, columnspan=2, pady=0)
error_label.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")


for i in range(7):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.eval('tk::PlaceWindow . center')


window.mainloop()


    
    
            