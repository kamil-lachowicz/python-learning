def main():
    total_groceries()

def total_groceries():
    while True:
        list = [{"name": "", "count": "" }]
        try:
            item = input()
            list.append(f'{item}')
        except EOFError:
            print("bwal")
            for key in list:
                print(key["name"], key["count"])
            return

main()
