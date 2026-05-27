def main():
    exp = input("Expression: ").split(" ")
    print(f"{calculate(exp):.1f}")
 
def calculate(expression):
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    else:
        if z != 0:
            return x/z
        else:
            print("Can't divide by 0")

main()
