#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""

        self.equation = tk.StringVar()
        self.equation.set("")

        self.expression_field = tk.Entry(root, textvariable=self.equation)
        self.expression_field.grid(columnspan=4, ipadx=8, ipady=10)

        self.create_number_buttons()
        self.create_operator_buttons()

        equal_button = tk.Button(root, text="=", command=self.equalpress)
        equal_button.grid(row=5, column=2)

        clear_button = tk.Button(root, text="C", command=self.clear)
        clear_button.grid(row=5, column="1")

    def create_number_buttons(self):
        for num in range(10):
            button = tk.Button(self.root, text=str(num), command=lambda num=num: self.press(str(num)))
            row = (9 - num) // 3 + 2
            col = (num - 1) % 3
            button.grid(row=row, column=col)

    def create_operator_buttons(self):
        operators = ['+', '-', '*', '/']
        row = 2
        col = 3
        for op in operators:
            button = tk.Button(self.root, text=op, command=lambda op=op: self.press(op))
            button.grid(row=row, column=col)
            row += 1

    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            self.expression = str(eval(self.expression))
            self.equation.set(self.expression)
        except:
            self.equation.set(" Error ")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

