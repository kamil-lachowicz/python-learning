def main():
    txt = replace_emojis()
    print_text(txt)

def replace_emojis():
    text = input("What text do you want to check?").replace(":)", "🙂").replace(":(", "🙁")
    return text 

def print_text(text):
    print(text)

main()