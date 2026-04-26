"""
Calculator class to handle all the computation logic.

I have  tried  to use dunder functions.
Idea is to use built-in methods, using the eval of self-expression,
where the expression will be dealt with as a string and then calculating the operation function directly.
This is something that I was learning parallely and I thought it can be
a good option to try instead of implementing each and every calculation
 button in between.
"""



class Calculator:
    def __init__(self):
        self.expression = "0"

    def append(self, value):
        if self.expression == "0" and value not in '+-*/.':
            self.expression = value
        else:
            self.expression += value

    def clear(self):
        self.expression = "0"

    def equals(self):
        try:
            # Safe eval: restrict globals to prevent code execution
            allowed = {"__builtins__": {}}
            result = eval(self.expression, allowed)
            self.expression = str(result) if result is not None else "0"
        except:
            self.expression = "Error"

    def get_display(self):
        return self.expression
