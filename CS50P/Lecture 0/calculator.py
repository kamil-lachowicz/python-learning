x = float(input("What's x? "))
y = float(input("What's y? "))

#We can also use round() instead of formating in print
z = x/y

print(f"{z:.2f}")

#Basic functions
def main():
    x = int(input("What's x?"))
    print("X squared is", square(x))

def square(n):
    return n*n

main()