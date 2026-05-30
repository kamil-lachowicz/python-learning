"""
Lecture 3 of CS50P course.
Reviewing exceptions.
"""
 
#Try/except
 
"""
#Trying too many lines at once
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
"""
 
#Try as few lines as possible + else for success
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
 
#Loop until valid input
 
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
 
print(f"x is {x}")
 
#Get_int
 
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
 
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")
        else:
            return x
 
        #Other ways to return:
        #return inside try - fewer lines
        #try:
        #    return int(input(prompt))
        #except ValueError:
        #    print("x is not an integer")
 
        #pass - silently re-ask without warning the user
        #try:
        #    return int(input(prompt))
        #except ValueError:
        #    pass
 
main()