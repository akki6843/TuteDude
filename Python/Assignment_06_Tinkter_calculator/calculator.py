import tkinter as tk
from tkinter import font


class Calculator:
    '''
    A simple calculator application using Tkinter.
    Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
    Features:
    - Clear button to reset the calculator. 
    - Displays results with up to two decimal places.
    - Handles division by zero gracefully by showing an error message.
    '''
    def __init__(self):
        """Initialize the calculator application."""
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Display variables
        '''
        first_operand: Stores the first number entered by the user.  
        operation: Stores the current arithmetic operation selected by the user.
        second_operand: Stores the second number entered by the user after selecting an operation.
        result: Stores the result of the calculation after the user presses the equals button.
        '''
        self.first_operand = ""
        self.operation = ""
        self.second_operand = ""
        self.result = ""

        # Custom fonts
        self.display_font = font.Font(family="Helvetica", size=20)
        self.button_font = font.Font(family="Helvetica", size=14)

        # Display frame
        self.display_frame = tk.Frame(self.root, bg="white", relief="sunken", bd=2)
        self.display_frame.pack(fill="both", padx=10, pady=10)

        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.display_label = tk.Label(
            self.display_frame,
            textvariable=self.display_var,
            bg="white",
            fg="black",
            anchor="e",
            font=self.display_font,
            padx=10,
            pady=10,
        )
        self.display_label.pack(fill="both", expand=True)

        # Button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Button configuration
        buttons = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("/", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("*", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("-", 2, 3),
            ("0", 3, 0),
            (".", 3, 1),
            ("=", 3, 2),
            ("+", 3, 3),
        ]

        """
        Create buttons based on the configuration and place them in a grid layout.
        Each button is associated with a command that calls the on_button_click method with the button's text as an argument.
        The clear button is created separately and calls the clear method when clicked.
        """

        for (text, row, col) in buttons:
            btn = tk.Button(
                self.button_frame,
                text=text,
                font=self.button_font,
                width=4,
                height=2,
                command=lambda t=text: self.on_button_click(t),
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Clear button
        clear_btn = tk.Button(
            self.root,
            text="C",
            font=self.button_font,
            width=28,
            height=2,
            command=self.clear,
        )
        clear_btn.pack(pady=5)

    def on_button_click(self, char):
        """
        Handle button clicks and update the calculator state accordingly.
        - If the clear button is clicked, reset the calculator.
        - If the equals button is clicked, perform the calculation.
        - If an operation button is clicked, store the first operand and the operation.
        - If a digit or decimal point is clicked, update the current operand being entered.
        """
        if char == "C":
            self.clear()
            return

        if char == "=":
            self.calculate()
            return

        if char in ["+", "-", "*", "/"]:
            # Store first operand and set operation
            if not self.first_operand:
                self.first_operand = "0"
            self.operation = char
            self.update_display()
            return

        # Add digit or decimal point
        if self.operation:
            self.second_operand += char
        else:
            if self.first_operand == "0":
                self.first_operand = char
            else:
                self.first_operand += char

        self.update_display()

    def calculate(self):
        """
        Perform the calculation based on the stored operands and operation.
        - Convert the operands to floats and perform the appropriate arithmetic operation.
        - Handle division by zero by displaying an error message.
        - Format the result to display up to two decimal places if necessary.
        """
        if not self.first_operand or not self.operation or not self.second_operand:
            return

        try:
            num1 = float(self.first_operand)
            num2 = float(self.second_operand)
            result = 0

            if self.operation == "+":
                result = num1 + num2
            elif self.operation == "-":
                result = num1 - num2
            elif self.operation == "*":
                result = num1 * num2
            elif self.operation == "/":
                if num2 == 0:
                    self.display_var.set("Error")
                    return
                result = num1 / num2

            # Format result
            if result == int(result):
                self.result = str(int(result))
            else:
                self.result = f"{result:.2f}"

            self.first_operand = self.result
            self.second_operand = ""
            self.operation = ""
            self.update_display()
        except ValueError:
            self.display_var.set("Error")

    def clear(self):
        """
        Reset the calculator to its initial state.
        - Clear the first operand, second operand, operation, and result.
        - Update the display to show "0".
        """
        self.first_operand = ""
        self.operation = ""
        self.second_operand = ""
        self.result = ""
        self.display_var.set("0")

    def update_display(self):
        """
        Update the calculator display with the current state.
        - Construct the display text based on the first operand, operation, and second operand.
        - If no input is present, display "0".
        """
        display_text = ""
        if self.first_operand:
            display_text = self.first_operand
        if self.operation:
            display_text += self.operation
        if self.second_operand:
            display_text += self.second_operand
        if not display_text:
            display_text = "0"
        self.display_var.set(display_text)

    def run(self):
        """
        Start the Tkinter main loop to run the calculator application.
        """
        self.root.mainloop()


if __name__ == "__main__":
    """
    Create an instance of the Calculator class and run the application.
    - The Calculator class encapsulates all the functionality of the calculator application.
    - The run method starts the Tkinter main loop, allowing the user to interact with the calculator.
    """
    calc = Calculator()
    calc.run()
