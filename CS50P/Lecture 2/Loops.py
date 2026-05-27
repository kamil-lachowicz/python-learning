"""
Lecture 2 of CS50P course.
Reviewing loops, lists, and dictionaries.
"""
 
# --- WHILE LOOP ---
# Najlepsze podejście - liczymy od 0, używamy +=
i = 0
while i < 3:
    print("meow")
    i += 1
 
# --- FOR LOOP ---
# Coraz lepsze podejścia do tego samego problemu:
 
# 1. Lista ręczna
for i in [0, 1, 2]:
    print("meow")
 
# 2. range() - czystsze
for i in range(3):
    print("meow")
 
# 3. _ zamiast i, gdy zmienna nieużywana
for _ in range(3):
    print("meow")
 
# 4. Jeszcze krótsze - ale daje "meowmeowmeow" w jednej linii
print("meow\n" * 3, end="")
 
# --- WALIDACJA INPUT UŻYTKOWNIKA ---
# Pętla while True + break to klasyczny wzorzec walidacji
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n  # return od razu zamiast break + osobny return
 
def meow(n):
    for _ in range(n):
        print("meow")
 
def main():
    meow(get_number())
 
main()
 
# --- LISTY ---
students = ["Hermione", "Harry", "Ron"]
 
# Iterowanie po liście
for student in students:
    print(student)
 
# Iterowanie z indeksem (len + range)
for i in range(len(students)):
    print(i + 1, students[i])
 
# --- SŁOWNIKI (dict) ---
# Zamiast dwóch list (students[], houses[]) lepiej użyć dict:
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
 
for student in students:
    print(student, students[student], sep=", ")
 
# Gdy potrzeba więcej danych na studenta - lista słowników:
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry",    "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron",      "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco",    "house": "Slytherin",  "patronus": None},
]
 
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
 
# --- MARIO (zagnieżdżone pętle) ---
# Kolumna:
def print_column(height):
    for _ in range(height):
        print("#")
 
# Wiersz:
def print_row(width):
    print("#" * width)
 
# Kwadrat - zewnętrzna pętla = wiersze, wewnętrzna = kolumny
def print_square(size):
    for _ in range(size):
        print_row(size)
 
print_square(3)