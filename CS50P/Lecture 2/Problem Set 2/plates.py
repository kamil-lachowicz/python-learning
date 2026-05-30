def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False
    if not are_numbers_at_end(s):
        return False
    return True

def are_numbers_at_end(s):
    i = 0
    for c in s:
        if c.isdigit():
            if not c == "0":
                return s[i:].isnumeric()
            else:
                return False
        i += 1
    return True

main()