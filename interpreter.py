#new function called interpreter for reading and direct calculation and printing
def interpreter(p):
    if "+" in p:
        first, second = p.split("+")
        print(float(first) + int(second))
    elif "-" in p:
        first, second = p.split("-")
        print(float(first) - int(second))
    elif "*" in p:
        first, second = p.split("*")
        print(float(first) * int(second))
    elif "/" in p:
        first, second = p.split("/")
        print(float(first) / int(second))

#taking expression input from the user
expression = input("Expression: ").strip().replace(" ","")

#calling the interpreter function
interpreter(expression)
