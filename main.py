import tkinter as tk

w_calculator=tk.Tk()
w_calculator.configure(bg='black')
w_calculator.geometry("500x550")
w_calculator.title("Calculator")
w_calculator.resizable(False, False)


formula = "0"
lbl_text = tk.Label(text=formula, font=("Courier New", 30, "bold"), bg="black", fg="white")
lbl_text.place(x=11, y=50)
    
buttons=[
        "C", "DEL", "*", "=",
        "1", "2", "3", "/",
        "4", "5", "6", "+",
        "7", "8", "9", "-",
        "(", "0", ")", "X^2"
        ]

x=18
y=140

for button in buttons:
        get_lbl=lambda x=button: scheme(x)
        tk.Button(text=button, bg="yellow",font=("Courier New", 20),command=get_lbl).place(x=x, y=y,width=115,height=79)
        x += 117
        if x > 400:
            x = 18
            y += 81

def scheme(operation):
    global formula

    if operation == "C":
            formula = ""
    elif operation == "DEL":
            formula = formula[0:-1]
    elif operation == "X^2":
            formula = str((eval(formula))**2)
    elif operation == "=":
            formula = str(eval(formula))
    else:
        if formula == "0":
            formula = ""
        formula += operation
    lbl_text.configure(text=formula)


w_calculator.mainloop()