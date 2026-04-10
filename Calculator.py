import tkinter as tk
import math

root = tk.Tk()
root.title("Calculator")
root.geometry("775x460")

number1 = ""
number2 = ""
znak = ""
new_number = False
number = 1 
otvet = ""

display = tk.Label(root, text=number1, font=("Arial", 24, "bold"))
display.grid(row = 0, column=0, columnspan=9)

root.config(bg="#242424")

#789
def click_7():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "7"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "7"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "7"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "7"
            display.config(text=number2)

button_7 = tk.Button(root, text=7, command=click_7, width=4, height=2, font=("Arial", 24, "bold"))
button_7.grid(row=1, column=0)

def click_8():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "8"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "8"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "8"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "8"
            display.config(text=number2)

button_8 = tk.Button(root, text=8, command=click_8, width=4, height=2, font=("Arial", 24, "bold"))
button_8.grid(row=1, column=1)

def click_9():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "9"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "9"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "9"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "9"
            display.config(text=number2)

button_9 = tk.Button(root, text=9, command=click_9, width=4, height=2, font=("Arial", 24, "bold"))
button_9.grid(row=1, column=2)

#456
def click_4():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "4"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "4"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "4"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "4"
            display.config(text=number2)

button_4 = tk.Button(root, text=4, command=click_4, width=4, height=2, font=("Arial", 24, "bold"))
button_4.grid(row=2, column=0)

def click_5():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "5"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "5"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "5"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "5"
            display.config(text=number2)

button_5 = tk.Button(root, text=5, command=click_5, width=4, height=2, font=("Arial", 24, "bold"))
button_5.grid(row=2, column=1)

def click_6():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "6"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "6"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "6"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "6"
            display.config(text=number2)

button_6 = tk.Button(root, text=6, command=click_6, width=4, height=2, font=("Arial", 24, "bold"))
button_6.grid(row=2, column=2)

#123
def click_1():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "1"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "1"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "1"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "1"
            display.config(text=number2)

button_1 = tk.Button(root, text=1, command=click_1, width=4, height=2, font=("Arial", 24, "bold"))
button_1.grid(row=3, column=0)

def click_2():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "2"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "2"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "2"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "2"
            display.config(text=number2)

button_2 = tk.Button(root, text=2, command=click_2, width=4, height=2, font=("Arial", 24, "bold"))
button_2.grid(row=3, column=1)

def click_3():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "3"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "3"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "3"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "3"
            display.config(text=number2)

button_3 = tk.Button(root, text=3, command=click_3, width=4, height=2, font=("Arial", 24, "bold"))
button_3.grid(row=3, column=2)

def click_0():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "0"
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "0"
            display.config(text=number1)
    else:
        if new_number:
            number2 = "0"
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "0"
            display.config(text=number2)

button_3 = tk.Button(root, text=0, command=click_0, width=4, height=2, font=("Arial", 24, "bold"))
button_3.grid(row=4, column=1)

def click_zapatay():
    global number
    global new_number
    global number1
    global number2
    if number == 1:
        if new_number:
            number1 = "0"+"."
            display.config(text=number1)
            new_number = False
        else:
            number1 = number1 + "."
            display.config(text=number1)
    else:
        if new_number:
            number2 = "."
            display.config(text=number2)
            new_number = False
        else:
            number2 = number2 + "."
            display.config(text=number2)

button_zapatay = tk.Button(root, text=".", command=click_zapatay, width=4, height=2, font=("Arial", 24, "bold"))
button_zapatay.grid(row=4, column=2)

def plus():
    global znak
    global new_number
    global number
    number = 2
    new_number = True
    znak = "+"

button_plus = tk.Button(root, text = "+", command=plus, width=4, height=2, font=("Arial", 24, "bold"))
button_plus.grid(row=3, column=3)

def minus():
    global znak
    global new_number
    global number
    number = 2
    new_number = True
    znak = "-"

button_minus = tk.Button(root, text = "-", command=minus, width=4, height=2, font=("Arial", 24, "bold"))
button_minus.grid(row=4, column=3)

def plus_minus():
    global number1
    global number2
    global znak
    global new_number
    global number
    if number == 1:
        if float(number1) > 0:
            number2 = "-" + number2
            display.config(text=number1)
        else:
            number1 = str(abs(float(number1)))
            display.config(text=number1)
    else:
        if float(number1) > 0:
            number2 = "-" + number2
            display.config(text=number2)
        else:
            number2 = str(abs(float(number2)))
            display.config(text=number2)
button_plus_minus = tk.Button(root, text = "±", command=plus_minus, width=4, height=2, font=("Arial", 24, "bold"))
button_plus_minus.grid(row=4, column=0)

def mult():
    global znak
    global new_number
    global number
    number = 2
    new_number = True
    znak = "*"
button_mult = tk.Button(root, text = "*", command=mult, width=4, height=2, font=("Arial", 24, "bold"))
button_mult.grid(row=2, column=3)

def div():
    global znak
    global new_number
    global number
    number = 2
    new_number = True
    znak = "/"
button_div = tk.Button(root, text = "/", command=div, width=4, height=2, font=("Arial", 24, "bold"))
button_div.grid(row=1, column=3)

def digr():
    global znak
    global new_number
    global number
    number = 2
    new_number = True
    znak = "^"
button_digr = tk.Button(root, text = "^", command=digr, width=4, height=2, font=("Arial", 24, "bold"))
button_digr.grid(row=3, column=4)

def coren():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(float(number1)**0.5)
            display.config(text=number1)
            number = 1
        else:
            otvet = str(float(otvet)**(1/2))
            display.config(text=otvet)
    elif number == 2:
        if number2 != "":
            number2 = str(float(number2)**0.5)
            display.config(text=number2)
            number = 2
        else:
            otvet = str(float(otvet)**(1/2))
            display.config(text=otvet)
    

button_coren = tk.Button(root, text = "√", command=coren, width=4, height=2, font=("Arial", 24, "bold"))
button_coren.grid(row=2, column=4)

def coren3():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(float(number1)**(1/3))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(float(otvet)**(1/3))
            display.config(text=otvet)
    else:
        if number2 != "":
            number2 = str(float(number2)**(1/3))
            display.config(text=number2)
            number = 2
        else:
            otvet = str(float(otvet)**(1/3))
            display.config(text=otvet)

button_coren3 = tk.Button(root, text = "∛", command=coren3, width=4, height=2, font=("Arial", 24, "bold"))
button_coren3.grid(row=1, column=4)

def kvadrat():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(float(number1)**2)
            display.config(text=number1)
            number = 1
        else:
            otvet = str(float(otvet)**2)
            display.config(text=otvet)
    else:
        if number2 != "":
            number2 = str(float(number2)**2)
            display.config(text=number2)
            number = 2
        else:
            otvet = str(float(otvet)**2)
            display.config(text=otvet)

button_kvadrat = tk.Button(root, text = "x²", command=kvadrat, width=4, height=2, font=("Arial", 24, "bold"))
button_kvadrat.grid(row=2, column=5)

def cub():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(float(number1)**3)
            display.config(text=number1)
            number = 1
        else:
            otvet = str(float(otvet)**3)
            display.config(text=otvet)
    else:
        if number2 != "":
            number2 = str(float(number2)**3)
            display.config(text=number2)
            number = 2
        else:
            otvet = str(float(otvet)**3)
            display.config(text=otvet)

button_cub = tk.Button(root, text = "x³", command=cub, width=4, height=2, font=("Arial", 24, "bold"))
button_cub.grid(row=1, column=5)

def factorial():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(math.factorial(int(float(number1))))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(math.factorial(int(float(otvet))))
            display.config(text=otvet)

    elif number == 2:
        if number2 != "":
            number2 = str(math.factorial(int(float(number2))))
            display.config(text=number2)
            number = 2
        else:
            otvet = str(math.factorial(int(float(otvet))))
            display.config(text=otvet)

button_factorial = tk.Button(root, text = "x!", command=factorial, width=4, height=2, font=("Arial", 24, "bold"))
button_factorial.grid(row=3, column=6)

def subfact():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(round(math.factorial(int(float(number1)))/math.e))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(round(math.factorial(int(float(otvet)))/math.e))
            display.config(text=otvet)
    elif number == 2:
        if number2 != "":
            number2 = str(round(math.factorial(int(float(number2)))/math.e))
            display.config(text=number2)
            number = 2
        else:
            otvet = str(round(math.factorial(int(float(otvet)))/math.e))
            display.config(text=otvet)

button_subfact = tk.Button(root, text = "!x", command=subfact, width=4, height=2, font=("Arial", 24, "bold"))
button_subfact.grid(row=3, column=5)

def okr():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(round(float(number1)))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(round(float(otvet)))
            display.config(text=otvet)
    elif number == 2:
        if number2 != "":
            number2 = str(round(float(number2)))
            display.config(text=number2)
            number = 2
        else: 
            otvet = str(round(float(otvet)))
            display.config(text=otvet)

button_okr = tk.Button(root, text = "≈", command=okr, width=4, height=2, font=("Arial", 24, "bold"))
button_okr.grid(row=4, column=5)

def e():
    global number1
    global number2
    global number
    global new_number
    if number == 1:
        number1 = math.e
        display.config(text=number1)
    else:
        number2 = math.e
        display.config(text=number2)
    new_number = True

button_e = tk.Button(root, text = "e", command=e, width=4, height=2, font=("Arial", 24, "bold"))
button_e.grid(row=2, column=6)

def pi():
    global number1
    global number2
    global number
    global new_number
    if number == 1:
        number1 = math.pi
        display.config(text=number1)
    else:
        number2 = math.pi
        display.config(text=number2)
    new_number = True

button_pi = tk.Button(root, text = "π", command=pi, width=4, height=2, font=("Arial", 24, "bold"))
button_pi.grid(row=1, column=6)

def clear():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet

    znak = ""
    new_number = True
    number = 1
    number1 = ""
    number2 = ""
    otvet = ""
    display.config(text="")

button_clear = tk.Button(root, text = "C", command=clear, width=4, height=2, font=("Arial", 24, "bold"))
button_clear.grid(row=4, column=6)

def cl():
    global number1
    global number2
    global number
    global otvet
    if number == 1:
        number1 = str(number1)
        number1 = number1[:-1]
        if number1 == "":
            number1 = ""
        display.config(text=number1)
    elif number == 2:
        if number2:
            number2 = str(number2)
            number2 = number2[:-1]
            if number2 == "":
                number2 = ""
            display.config(text=number2)
        else:
            otvet = str(otvet)
            otvet = otvet[:-1]
            if otvet == "":
                otvet = ""
            display.config(text=otvet)

button_cl = tk.Button(root, text = "⌫", command=cl, width=4, height=2, font=("Arial", 24, "bold"))
button_cl.grid(row=4, column=7)

def sin1():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(math.sin((float(number1)*math.pi)/180))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(math.sin((float(otvet)*math.pi)/180))
            display.config(text=otvet)
    else:
        if number2 != "":
            number2 = str(math.sin((float(number2)*math.pi)/180))
            display.config(text=number2)
            number = 2
        else:
            otvet = str(math.sin((float(otvet)*math.pi)/180))
            display.config(text=otvet)

button_sin1 = tk.Button(root, text = "sin", command=sin1, width=4, height=2, font=("Arial", 24, "bold"))
button_sin1.grid(row=1, column=7)

def cos1():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(math.cos((float(number1)*math.pi)/180))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(math.cos((float(otvet)*math.pi)/180))
            display.config(text=otvet)
    else:
        if number2 != "":
            number2 = str(math.cos((float(number2)*math.pi)/180))
            display.config(text=number2)
            number = 2
        else:
            otvet = str(math.cos((float(otvet)*math.pi)/180))
            display.config(text=otvet)

button_cos1 = tk.Button(root, text = "cos", command=cos1, width=4, height=2, font=("Arial", 24, "bold"))
button_cos1.grid(row=2, column=7)

def tan1():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(math.tan((float(number1)*math.pi)/180))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(math.tan((float(otvet)*math.pi)/180))
            display.config(text=otvet)
    else:
        if number2 != "":
            number2 = str(math.tan((float(number2)*math.pi)/180))
            display.config(text=number2)
            number = 2
        else:
            otvet = str(math.tan((float(otvet)*math.pi)/180))
            display.config(text=otvet)

button_tan1 = tk.Button(root, text = "tan", command=tan1, width=4, height=2, font=("Arial", 24, "bold"))
button_tan1.grid(row=3, column=7)

def ln():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(math.log((float(number1)*math.pi)/180))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(math.log((float(otvet)*math.pi)/180))
            display.config(text=otvet)
    else:
        if number2 != "":
            number2 = str(math.log((float(number2)*math.pi)/180))
            display.config(text=number2)
            number = 2
        else:
            otvet = str(math.log((float(otvet)*math.pi)/180))
            display.config(text=otvet)

button_ln = tk.Button(root, text = "ln", command=ln, width=4, height=2, font=("Arial", 24, "bold"))
button_ln.grid(row=1, column=8)

def log1():
    global znak
    global new_number
    global number
    global number1
    global number2
    global otvet
    
    new_number = True
    if number == 1:
        if number1 != "":
            number1 = str(math.log(((float(number1)*math.pi)/180),10))
            display.config(text=number1)
            number = 1
        else:
            otvet = str(math.log(((float(otvet)*math.pi)/180),10))
            display.config(text=otvet)
    else:
        if number2 != "":
            number2 = str(math.log(((float(number2)*math.pi)/180),10))
            display.config(text=number2)
            number = 2
        else:
            otvet = str(math.log(((float(otvet)*math.pi)/180),10))
            display.config(text=otvet)

button_log1 = tk.Button(root, text = "log", command=log1, width=4, height=2, font=("Arial", 24, "bold"))
button_log1.grid(row=2, column=8)



def rovno():
    global number1
    global number2
    global znak
    global otvet
    global number
    global new_number
    if number == 2:
        if znak == "+":
            otvet = str(float(number1)+float(number2))
            display.config(text=otvet)
        elif znak == "-":
            otvet = str(float(number1)-float(number2))
            display.config(text=otvet)
        elif znak == "*":
            otvet = str(float(number1)*float(number2))
            display.config(text=otvet)
        elif znak == "/":
            otvet = str(float(number1)/float(number2))
            display.config(text=otvet)
        elif znak == "^":
            otvet = str(float(number1)**float(number2))
            display.config(text=otvet)

        number = 2
        new_number = True
        znak = ""
        number1 = str(otvet)
        number2 = ""

button_rovno = tk.Button(root, text = "=", command=rovno, width=4, height=2, font=("Arial", 24, "bold"))
button_rovno.grid(row=4, column=4)

def theme():
    BG_COLOR = "#2B2B2B" 
    FG_COLOR = "#FFFFFF" 
    
    for widget in root.winfo_children():
        try:
            widget.config(bg=BG_COLOR, fg=FG_COLOR)
        except:
            pass

theme()

root.mainloop()