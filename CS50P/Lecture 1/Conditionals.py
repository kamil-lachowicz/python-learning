"""
Lecture 1 of CS50P course. 
Reviewing conditionals.
"""

"""
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
"""

def main():
    x = int(input("What's x?\n"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n%2==0
    
    #Other ways to achive the result
    return True if n % 2 == 0 else False
    
    if n % 2 == 0:
        return True;
    else:
        return False



main()

name = input("What's your name?")

match name:
    case "Harry":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")