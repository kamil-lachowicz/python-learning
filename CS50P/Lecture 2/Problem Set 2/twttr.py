def main():
    text = input("Input: ")
    print("Output: " + omit_vowels(text))

def omit_vowels(sentence):
    result = ""
    for char in sentence:
        if char not in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
            result += char
    return result 
            
main()
