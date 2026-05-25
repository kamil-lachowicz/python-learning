"""
Lecture 0 of CS50P course. 
Reviewing the absolute basics of programming in Python just to get into the course.
"""

# code . 
# python hello.py

# Ask user for their name
name = input("What's your name? ") #We can also strip().title() here, at lines end

#Remove whitespace from str and capitalize user's name
name = name.strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")


# Say hello to the user in different formating
print("Hello, \"respected\"", name, end="\n\n")
print(f"hello, {last}")

#Basic functions
def main():
    name = input("What's your name, (but in main)?")
    hello(name)

def hello(to="world"):
    print("Hello,", to)

main()