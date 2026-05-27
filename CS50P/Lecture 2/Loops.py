
"""
Lecture 2 of CS50P course.
Reviewing loops, lists and dictionaries.
"""
 
#While 
 
"""
i = 0
while i < 3:
    print("meow")
    i += 1
"""
 
#For
 
"""
#Worse
for i in [0, 1, 2]:
    print("meow")
 
#Better
for i in range(3):
    print("meow")
 
#Best - _ when variable is unused
for _ in range(3):
    print("meow")
 
# Alternative
print("meow\n" * 3, end="")
"""
 
#Input validation
 
def main():
    meow(get_number())
 
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
 
def meow(n):
    for _ in range(n):
        print("meow")
 
main()
 
#Lists
 
students = ["Hermione", "Harry", "Ron"]
 
for student in students:
    print(student)
 
#With index
for i in range(len(students)):
    print(i + 1, students[i])
 
#Dictionaries
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
 
for student in students:
    print(student, students[student], sep=", ")
 
#More data = List of dicts
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry",    "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron",      "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco",    "house": "Slytherin",  "patronus": None},
]
 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
 
#Nested loops (One inside the other)
 
def print_square(size):
    for _ in range(size):
        print("#" * size)
 
    #Nested alternative
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
 
print_square(3)