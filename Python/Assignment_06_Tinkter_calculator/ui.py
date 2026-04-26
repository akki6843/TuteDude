"""
This is the UI part of the code.
Here if you will see, mostly the development has been
done around the TK inter library.
The idea is I have created the button layout and basic functionalities
like plus, minus, and clear.

My thought was I should be able to keep two separate code:
1. One is the functionality that is backend, where you have calculator main.py
2. The frontend that is ui.py

"""

import tkinter as tk
from calculator_main import Calculator


class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.calc = Calculator()  # Use calculator class here

        # Display
        self.display_var = tk.StringVar()
        self.display_var.set(self.calc.get_display())
        display = tk.Entry(root, textvariable=self.display_var, font=("Arial", 20),
                           justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        # Button layout
        buttons = [
            ("C", 1, 0, self.clear),
            ("±", 1, 1, self.negate),  # Optional: toggle sign
            ("%", 1, 2, lambda: self.calc.append("%")),
            ("/", 1, 3, lambda: self.calc.append("/")),
            ("7", 2, 0, lambda: self.calc.append("7")),
            ("8", 2, 1, lambda: self.calc.append("8")),
            ("9", 2, 2, lambda: self.calc.append("9")),
            ("*", 2, 3, lambda: self.calc.append("*")),
            ("4", 3, 0, lambda: self.calc.append("4")),
            ("5", 3, 1, lambda: self.calc.append("5")),
            ("6", 3, 2, lambda: self.calc.append("6")),
            ("-", 3, 3, lambda: self.calc.append("-")),
            ("1", 4, 0, lambda: self.calc.append("1")),
            ("2", 4, 1, lambda: self.calc.append("2")),
            ("3", 4, 2, lambda: self.calc.append("3")),
            ("+", 4, 3, lambda: self.calc.append("+")),
            ("0", 5, 0, lambda: self.calc.append("0"), 2),  # Span 2 columns
            (".", 5, 2, lambda: self.calc.append(".")),
            ("=", 5, 3, self.equals)
        ]

        for (text, row, col, command, *span) in buttons:
            colspan = span[0] if span else 1
            btn = tk.Button(root, text=text, font=("Arial", 18), width=5,
                            command=command, bg="lightgray")
            btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")

        # Configure grid weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def update_display(self):
        self.display_var.set(self.calc.get_display())

    def clear(self):
        self.calc.clear()
        self.update_display()

    def negate(self):
        expr = self.calc.get_display()
        if expr != "Error" and expr != "0":
            if expr.startswith("-"):
                self.calc.expression = expr[1:]
            else:
                self.calc.expression = "-" + expr
            self.update_display()

    def equals(self):
        self.calc.equals()
        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()