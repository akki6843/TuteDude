import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

num1 = ""
num2 = ""
op = ""

screen = tk.StringVar()
screen.set("0")

label = tk.Label(window, textvariable=screen, bg="white", fg="black", anchor="e", padx=5, pady=10, relief="sunken")
label.pack(fill="both", padx=10, pady=10)

frame = tk.Frame(window)
frame.pack()

def click(val):
    global num1, num2, op

    if val == "C":
        num1 = ""
        num2 = ""
        op = ""
        screen.set("0")
        return

    if val == "=":
        if num1 == "" or op == "" or num2 == "":
            return
        n1 = float(num1)
        n2 = float(num2)
        ans = 0
        if op == "+":
            ans = n1 + n2
        elif op == "-":
            ans = n1 - n2
        elif op == "*":
            ans = n1 * n2
        elif op == "/":
            if n2 == 0:
                screen.set("cant divide by 0")
                return
            ans = n1 / n2
        if ans == int(ans):
            ans = int(ans)
        num1 = str(ans)
        num2 = ""
        op = ""
        screen.set(num1)
        return

    if val in ["+", "-", "*", "/"]:
        if num1 == "":
            num1 = "0"
        op = val
        screen.set(num1 + op)
        return

    if op == "":
        num1 = num1 + val
        screen.set(num1)
    else:
        num2 = num2 + val
        screen.set(num1 + op + num2)


btn7 = tk.Button(frame, text="7", width=4, height=2, command=lambda: click("7"))
btn7.grid(row=0, column=0, padx=4, pady=4)
btn8 = tk.Button(frame, text="8", width=4, height=2, command=lambda: click("8"))
btn8.grid(row=0, column=1, padx=4, pady=4)
btn9 = tk.Button(frame, text="9", width=4, height=2, command=lambda: click("9"))
btn9.grid(row=0, column=2, padx=4, pady=4)
btnd = tk.Button(frame, text="/", width=4, height=2, command=lambda: click("/"))
btnd.grid(row=0, column=3, padx=4, pady=4)

btn4 = tk.Button(frame, text="4", width=4, height=2, command=lambda: click("4"))
btn4.grid(row=1, column=0, padx=4, pady=4)
btn5 = tk.Button(frame, text="5", width=4, height=2, command=lambda: click("5"))
btn5.grid(row=1, column=1, padx=4, pady=4)
btn6 = tk.Button(frame, text="6", width=4, height=2, command=lambda: click("6"))
btn6.grid(row=1, column=2, padx=4, pady=4)
btnm = tk.Button(frame, text="*", width=4, height=2, command=lambda: click("*"))
btnm.grid(row=1, column=3, padx=4, pady=4)

btn1 = tk.Button(frame, text="1", width=4, height=2, command=lambda: click("1"))
btn1.grid(row=2, column=0, padx=4, pady=4)
btn2 = tk.Button(frame, text="2", width=4, height=2, command=lambda: click("2"))
btn2.grid(row=2, column=1, padx=4, pady=4)
btn3 = tk.Button(frame, text="3", width=4, height=2, command=lambda: click("3"))
btn3.grid(row=2, column=2, padx=4, pady=4)
btns = tk.Button(frame, text="-", width=4, height=2, command=lambda: click("-"))
btns.grid(row=2, column=3, padx=4, pady=4)

btn0 = tk.Button(frame, text="0", width=4, height=2, command=lambda: click("0"))
btn0.grid(row=3, column=0, padx=4, pady=4)
btndot = tk.Button(frame, text=".", width=4, height=2, command=lambda: click("."))
btndot.grid(row=3, column=1, padx=4, pady=4)
btneq = tk.Button(frame, text="=", width=4, height=2, command=lambda: click("="))
btneq.grid(row=3, column=2, padx=4, pady=4)
btnp = tk.Button(frame, text="+", width=4, height=2, command=lambda: click("+"))
btnp.grid(row=3, column=3, padx=4, pady=4)

btnc = tk.Button(window, text="C", width=20, height=2, command=lambda: click("C"))
btnc.pack(pady=5)

window.mainloop()