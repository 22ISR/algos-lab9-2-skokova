import tkinter as tk

root = tk.Tk()
root.title("Моя программа")
root.geometry("800x500")
tk.Label(root, text="Калькулятор", font=("Arial", 18)).pack(padx=20, pady=20)
textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=20, pady=10, fill="x")
buttonFrame = tk.Frame(root)
buttonFrame.pack(fill="x", padx=20, pady=10)
for i in range(4):
    buttonFrame.columnconfigure(i, weight=1)
def press(char):
    textbox.insert(tk.END, str(char))
def clear():
    textbox.delete('1.0', tk.END)
def calculate():
   expr = textbox.get('1.0', tk.END).strip()
   result = eval(expr)
   clear()
   textbox.insert(tk.END, str(result))
    

btn7 = tk.Button(buttonFrame, text='7', font=("Arial", 18), command=lambda: press('7'))
btn7.grid(row=0, column=0, sticky="we", padx=5, pady=5)

btn8 = tk.Button(buttonFrame, text='8', font=("Arial", 18), command=lambda: press('8'))
btn8.grid(row=0, column=1, sticky="we", padx=5, pady=5)

btn9 = tk.Button(buttonFrame, text='9', font=("Arial", 18), command=lambda: press('9'))
btn9.grid(row=0, column=2, sticky="we", padx=5, pady=5)

btn_div = tk.Button(buttonFrame, text='/', font=("Arial", 18), command=lambda: press('/'))
btn_div.grid(row=0, column=3, sticky="we", padx=5, pady=5)

btn4 = tk.Button(buttonFrame, text='4', font=("Arial", 18), command=lambda: press('4'))
btn4.grid(row=1, column=0, sticky="we", padx=5, pady=5)

btn5 = tk.Button(buttonFrame, text='5', font=("Arial", 18), command=lambda: press('5'))
btn5.grid(row=1, column=1, sticky="we", padx=5, pady=5)

btn6 = tk.Button(buttonFrame, text='6', font=("Arial", 18), command=lambda: press('6'))
btn6.grid(row=1, column=2, sticky="we", padx=5, pady=5)

btn_mul = tk.Button(buttonFrame, text='*', font=("Arial", 18), command=lambda: press('*'))
btn_mul.grid(row=1, column=3, sticky="we", padx=5, pady=5)

btn1 = tk.Button(buttonFrame, text='1', font=("Arial", 18), command=lambda: press('1'))
btn1.grid(row=2, column=0, sticky="we", padx=5, pady=5)

btn2 = tk.Button(buttonFrame, text='2', font=("Arial", 18), command=lambda: press('2'))
btn2.grid(row=2, column=1, sticky="we", padx=5, pady=5)

btn3 = tk.Button(buttonFrame, text='3', font=("Arial", 18), command=lambda: press('3'))
btn3.grid(row=2, column=2, sticky="we", padx=5, pady=5)

btn_sub = tk.Button(buttonFrame, text='-', font=("Arial", 18), command=lambda: press('-'))
btn_sub.grid(row=2, column=3, sticky="we", padx=5, pady=5)

btn0 = tk.Button(buttonFrame, text='0', font=("Arial", 18), command=lambda: press('0'))
btn0.grid(row=3, column=0, sticky="we", padx=5, pady=5)

btn_clear = tk.Button(buttonFrame, text='C', font=("Arial", 18), command=clear)
btn_clear.grid(row=3, column=1, columnspan=2,sticky="we", padx=5, pady=5)

btn_add = tk.Button(buttonFrame, text='+', font=("Arial", 18), command=lambda: press('+'))
btn_add.grid(row=3, column=3, sticky="we", padx=5, pady=5)

btn_equal = tk.Button(buttonFrame, text='=', font=("Arial", 18), command=calculate)
btn_equal.grid(row=4, column=0, columnspan=4, sticky="we", padx=5, pady=5)

root.mainloop()

