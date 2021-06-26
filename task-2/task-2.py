## 1.Import the math and tkinter libraries 
import math
import tkinter as tk
from tkinter import messagebox


## 2. Functions
## 2.1 Operational functions
def add_digit(digit):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)
    calc['state'] = tk.DISABLED


def add_operation(operation):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in '/*-+.':
        value = value[:-1]
    elif '/' in value or '*' in value or '-' in value or '+' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED


def calculate():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in '/*-+':
        operation = value[-1]
        value = value[:-1] + operation + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Attention!", "You must input numerics or operation!")
        calc.insert(0, "0")
    except ZeroDivisionError:
        messagebox.showinfo("Attention!", "Cannot be divided by zero!")
        calc.insert(0, "0")
    calc['state'] = tk.DISABLED


def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def trigonometry(operation):
    try:
        calc['state'] = tk.NORMAL
        value = float(calc.get())
        if operation == 'cos':
            value = str(math.cos(value))
        if operation == 'sin':
            value = str(math.sin(value))
        if operation == 'tan':
            value = str(math.tan(value))
        if operation == 'cot':
            value = str(math.cos(value) / math.sin(value))
        calc.delete(0, tk.END)
        calc.insert(0, value)
    except ValueError:
        messagebox.showinfo("Attention!", "Could not convert string to float!")
        calc.delete(0, tk.END)
        calc.insert(0, "0")
    calc['state'] = tk.DISABLED


def logarithms(operation):
    calc['state'] = tk.NORMAL
    try:
        value = float(calc.get())
        if operation == 'log2' and value != 0:
            value = str(math.log2(value))
            calc.delete(0, tk.END)
            calc.insert(0, value)
        elif value == 0:
            calc.delete(0, tk.END)
            calc.insert(0, "0")
        if operation == 'log10' and value != 0:
            value = str(math.log10(value))
            calc.delete(0, tk.END)
            calc.insert(0, value)
        elif value == 0:
            calc.delete(0, tk.END)
            calc.insert(0, "0")
        if operation == 'ln' and value != 0:
            value = str(math.log(value))
            calc.delete(0, tk.END)
            calc.insert(0, value)
        elif value == 0:
            calc.delete(0, tk.END)
            calc.insert(0, "0")
    except ValueError:
        messagebox.showinfo("Attention!", "Could not convert string to float!")
        calc.delete(0, tk.END)
        calc.insert(0, "0")
    calc['state'] = tk.DISABLED


def percent():
    try:
        calc['state'] = tk.NORMAL
        value = calc.get()
        if '/' in value:
            value_1 = float(value[:value.index('/')])
            value_2 = float(value[value.index('/') + 1:])
            value = value_1 / (value_2 / 100)
        elif '*' in value:
            value_1 = float(value[:value.index('*')])
            value_2 = float(value[value.index('*') + 1:])
            value = value_1 * (value_2 / 100)
        elif '-' in value:
            value_1 = float(value[:value.index('-')])
            value_2 = float(value[value.index('-') + 1:])
            value = value_1 - ((value_1 * value_2) / 100)
        elif '+' in value:
            value_1 = float(value[:value.index('+')])
            value_2 = float(value[value.index('+') + 1:])
            value = value_1 + ((value_1 * value_2) / 100)
        else:
            value = float(value)
            value = str(value / 100)
        calc.delete(0, tk.END)
        calc.insert(0, str(value))
    except ValueError:
        messagebox.showinfo("Attention!", "Could not convert string to float!")
        calc.delete(0, tk.END)
        calc.insert(0, "0")
    calc['state'] = tk.DISABLED


def do_bin():
    calc['state'] = tk.NORMAL
    try:
        value = int(calc.get())
        value = str(bin(value))
        calc.delete(0, tk.END)
        calc.insert(0, value[2:])
    except ValueError:
        messagebox.showinfo("Attention!", "An invalid literal for integer!")
        calc.delete(0, tk.END)
        calc.insert(0, "0")
    calc['state'] = tk.DISABLED


def do_dot(operation):
    calc['state'] = tk.NORMAL
    try:
        value = calc.get()
        if '/' in value:
            if '.' in value[value.index('/'):] or '.' == value[value.index('/') + 1]:
                calc['state'] = tk.DISABLED
        elif '*' in value:
            if '.' in value[value.index('*'):] or '.' == value[value.index('*') + 1]:
                calc['state'] = tk.DISABLED
        elif '-' in value:
            if '.' in value[value.index('-'):] or '.' == value[value.index('-') + 1]:
                calc['state'] = tk.DISABLED
        elif '+' in value:
            if '.' in value[value.index('+'):] or '.' == value[value.index('+') + 1]:
                calc['state'] = tk.DISABLED
        elif '.' in value:
            calc['state'] = tk.DISABLED
        calc.delete(0, tk.END)
        calc.insert(0, value + operation)
    except IndexError:
        messagebox.showinfo("Attention!", "Cannot input a dot after operation!")
    calc['state'] = tk.DISABLED


def do_del(operation):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if len(value) == 1:
        calc.delete(0, tk.END)
        calc.insert(0, '0')
        calc['state'] = tk.DISABLED
        return
    calc.delete(0, tk.END)
    calc.insert(0, value[:-1])
    calc['state'] = tk.DISABLED


## 2.2 Button functions
def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13),
                     command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=clear)


def make_cos_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: trigonometry(operation))


def make_sin_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: trigonometry(operation))


def make_tan_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: trigonometry(operation))


def make_cot_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: trigonometry(operation))


def make_log2_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: logarithms(operation))


def make_log10_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: logarithms(operation))


def make_ln_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: logarithms(operation))


def make_percent_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=percent)


def make_bin_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=do_bin)


def make_dot_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: do_dot(operation))


def make_del_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13),
                     command=lambda: do_del(operation))


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '/*-+':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '%':
        percent()
    elif event.char == '\x08':
        do_del('del')
    elif event.char == '.':
        do_dot('.')
    elif event.char == 'b':
        do_bin()


## 3. Window
win = tk.Tk()
win.geometry(f"365x335")
win['bg'] = 'grey'
win.title('Calculator')
win.minsize(365, 335)
win.maxsize(365, 335)

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=6, stick='we', padx=5, pady=2)

for i in range(0, 6):
    win.grid_columnconfigure(i, minsize=60)
    win.grid_rowconfigure(i + 1, minsize=60)

## 4. Make button
## 4.1 Digits
make_digit_button('7').grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button('8').grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button('9').grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button('4').grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button('5').grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button('6').grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button('1').grid(row=4, column=0, stick="wens", padx=5, pady=5)
make_digit_button('2').grid(row=4, column=1, stick="wens", padx=5, pady=5)
make_digit_button('3').grid(row=4, column=2, stick="wens", padx=5, pady=5)
make_digit_button('0').grid(row=5, column=0, columnspan=2, stick="wens", padx=5, pady=5)

## 4.2 Operations
make_operation_button('/').grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation_button('-').grid(row=4, column=3, stick="wens", padx=5, pady=5)
make_operation_button('+').grid(row=5, column=3, stick="wens", padx=5, pady=5)

make_calc_button('=').grid(row=5, column=2, stick="wens", padx=5, pady=5)
make_clear_button('c').grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_dot_button('.').grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_del_button('del').grid(row=1, column=1, stick="wens", padx=5, pady=5)

make_cos_button('cos').grid(row=2, column=4, stick="wens", padx=5, pady=5)
make_sin_button('sin').grid(row=3, column=4, stick="wens", padx=5, pady=5)
make_tan_button('tan').grid(row=4, column=4, stick="wens", padx=5, pady=5)
make_cot_button('cot').grid(row=5, column=4, stick="wens", padx=5, pady=5)

make_log2_button('log2').grid(row=2, column=5, stick="wens", padx=5, pady=5)
make_log10_button('log10').grid(row=3, column=5, stick="wens", padx=5, pady=5)
make_ln_button('ln').grid(row=4, column=5, stick="wens", padx=5, pady=5)
make_percent_button('%').grid(row=5, column=5, stick="wens", padx=5, pady=5)

## 4.3 To binary
make_bin_button('bin').grid(row=1, column=3, columnspan=3, stick="wens", padx=5, pady=5)

win.mainloop()
