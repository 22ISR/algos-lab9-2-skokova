import tkinter as tk
import math

root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("800x600")
tk.Label(root, text="Калькулятор", font=("Arial", 18)).pack(padx=20, pady=20)
textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=20, pady=10, fill="x")
buttonFrame = tk.Frame(root)
buttonFrame.pack(fill="x", padx=20, pady=10)

for i in range(5):
    buttonFrame.columnconfigure(i, weight=1)

def on_button_click(value):
    if value == "=":
        calculate()
    elif value == "√":
        calculate_square_root()
    else:
        textbox.insert(tk.END, str(value))

def clear():
    textbox.delete('1.0', tk.END)

def calculate():
    expr = textbox.get('1.0', tk.END).strip()
    try:
        result = eval(expr)
        clear()
        textbox.insert(tk.END, str(result))
    except Exception as e:
        clear()
        textbox.insert(tk.END, "Error")

def calculate_square_root():
    expr = textbox.get('1.0', tk.END).strip()
    try:
        number = float(expr)
        if number < 0:
            raise ValueError("Нельзя найти корень из отрицательного числа")
        result = math.sqrt(number)
        clear()
        textbox.insert(tk.END, str(result))
    except Exception as e:
        clear()
        textbox.insert(tk.END, "Error")

# Верхний ряд: ( ) . √
btn_open = tk.Button(buttonFrame, text='(', font=("Arial", 18), command=lambda: on_button_click('('))
btn_open.grid(row=0, column=0, sticky="we", padx=5, pady=5)

btn_close = tk.Button(buttonFrame, text=')', font=("Arial", 18), command=lambda: on_button_click(')'))
btn_close.grid(row=0, column=1, sticky="we", padx=5, pady=5)

btn_dot = tk.Button(buttonFrame, text='.', font=("Arial", 18), command=lambda: on_button_click('.'))
btn_dot.grid(row=0, column=2, sticky="we", padx=5, pady=5)

btn_sqrt = tk.Button(buttonFrame, text='√', font=("Arial", 18), command=lambda: on_button_click('√'))
btn_sqrt.grid(row=0, column=3, sticky="we", padx=5, pady=5)

# Ряд 7 8 9 /
btn7 = tk.Button(buttonFrame, text='7', font=("Arial", 18), command=lambda: on_button_click('7'))
btn7.grid(row=1, column=0, sticky="we", padx=5, pady=5)

btn8 = tk.Button(buttonFrame, text='8', font=("Arial", 18), command=lambda: on_button_click('8'))
btn8.grid(row=1, column=1, sticky="we", padx=5, pady=5)

btn9 = tk.Button(buttonFrame, text='9', font=("Arial", 18), command=lambda: on_button_click('9'))
btn9.grid(row=1, column=2, sticky="we", padx=5, pady=5)

btn_div = tk.Button(buttonFrame, text='/', font=("Arial", 18), command=lambda: on_button_click('/'))
btn_div.grid(row=1, column=3, sticky="we", padx=5, pady=5)

# Ряд 4 5 6 *
btn4 = tk.Button(buttonFrame, text='4', font=("Arial", 18), command=lambda: on_button_click('4'))
btn4.grid(row=2, column=0, sticky="we", padx=5, pady=5)

btn5 = tk.Button(buttonFrame, text='5', font=("Arial", 18), command=lambda: on_button_click('5'))
btn5.grid(row=2, column=1, sticky="we", padx=5, pady=5)

btn6 = tk.Button(buttonFrame, text='6', font=("Arial", 18), command=lambda: on_button_click('6'))
btn6.grid(row=2, column=2, sticky="we", padx=5, pady=5)

btn_mul = tk.Button(buttonFrame, text='*', font=("Arial", 18), command=lambda: on_button_click('*'))
btn_mul.grid(row=2, column=3, sticky="we", padx=5, pady=5)

# Ряд 1 2 3 -
btn1 = tk.Button(buttonFrame, text='1', font=("Arial", 18), command=lambda: on_button_click('1'))
btn1.grid(row=3, column=0, sticky="we", padx=5, pady=5)

btn2 = tk.Button(buttonFrame, text='2', font=("Arial", 18), command=lambda: on_button_click('2'))
btn2.grid(row=3, column=1, sticky="we", padx=5, pady=5)

btn3 = tk.Button(buttonFrame, text='3', font=("Arial", 18), command=lambda: on_button_click('3'))
btn3.grid(row=3, column=2, sticky="we", padx=5, pady=5)

btn_sub = tk.Button(buttonFrame, text='-', font=("Arial", 18), command=lambda: on_button_click('-'))
btn_sub.grid(row=3, column=3, sticky="we", padx=5, pady=5)

# Ряд 0 C +
btn0 = tk.Button(buttonFrame, text='0', font=("Arial", 18), command=lambda: on_button_click('0'))
btn0.grid(row=4, column=0, sticky="we", padx=5, pady=5)

btn_clear = tk.Button(buttonFrame, text='C', font=("Arial", 18), command=clear)
btn_clear.grid(row=4, column=1, columnspan=2, sticky="we", padx=5, pady=5)

btn_add = tk.Button(buttonFrame, text='+', font=("Arial", 18), command=lambda: on_button_click('+'))
btn_add.grid(row=4, column=3, sticky="we", padx=5, pady=5)

# Ряд =
btn_equal = tk.Button(buttonFrame, text='=', font=("Arial", 18), command=lambda: on_button_click("="))
btn_equal.grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)

root.mainloop()
