import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, bg="black", fg ="white", font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text=1, command=lambda: add_to_calculation(1), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text=2, command=lambda: add_to_calculation(2), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text=3, command=lambda: add_to_calculation(3), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text=4, command=lambda: add_to_calculation(4), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text=5, command=lambda: add_to_calculation(5), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text=6, command=lambda: add_to_calculation(6), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text=7, command=lambda: add_to_calculation(7), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text=8, command=lambda: add_to_calculation(8), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text=9, command=lambda: add_to_calculation(9), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text=0, command=lambda: add_to_calculation(0), activeforeground="white", activebackground="brown", bg="black", fg ="white", width=5,
                  font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), activeforeground="white", activebackground="brown", bg="green", fg ="white", width=5,
                     font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), activeforeground="white", activebackground="brown", bg="green", fg ="white", width=5,
                      font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), activeforeground="white", activebackground="brown", bg="green", fg ="white", width=5,
                    font=("Arial", 14))
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), activeforeground="white", activebackground="brown", bg="green", fg ="white", width=5,
                    font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_open_par = tk.Button(root, text="(", command=lambda: add_to_calculation("("), activeforeground="white", activebackground="brown", bg="blue", fg ="white", width=5,
                         font=("Arial", 14))
btn_open_par.grid(row=5, column=1)

btn_close_par = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), activeforeground="white", activebackground="brown",bg="blue", fg ="white", width=5,
                          font=("Arial", 14))
btn_close_par.grid(row=5, column=3)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, bg="orange", activeforeground="white", activebackground="brown",fg ="white", width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)

btn_clear = tk.Button(root, text="C", command=clear_field, bg="grey", fg ="white", activeforeground="white", activebackground="brown",width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
