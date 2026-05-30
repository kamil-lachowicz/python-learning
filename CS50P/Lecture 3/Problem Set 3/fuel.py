def main():
    print(fraction_to_percent())

def fraction_to_percent():
    while True:
        fract = input("Fraction: ")
        try:
            x, y = fract.split("/")
        except ValueError:
            continue
        if not x.isdigit() or not y.isdigit():
            continue
        if  int(x) > int(y):
            continue
        try:
            fraction = (int(x)/int(y))
            if fraction >= 0.99:
                return "F"
            if fraction <= 0.01:
                return "E"
            result = f"{round((int(x)/int(y))*100)}%"
            return result
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
