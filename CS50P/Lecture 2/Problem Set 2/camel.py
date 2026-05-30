def main():
    camel = input("camelCase: ")
    print(camelCase_to_snake(camel))

def camelCase_to_snake(text):
    snake = ""
    for c in text:
        if c.isupper():
            c = "_" + c.lower()
        snake += c
    return snake
main()
