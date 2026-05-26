def main():
    txt = replace_whitespaces()
    print_text(txt)

def replace_whitespaces():
    text = input("What text do you want to check?").replace(" ", "...")
    return text 

def print_text(text):
    print(text)

main()