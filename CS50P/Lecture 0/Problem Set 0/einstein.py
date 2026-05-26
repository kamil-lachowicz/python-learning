def main():
    txt = einstein()
    print("E:", txt)

def einstein():
    mass = int(input("m: "))
    c = 300000000
    result = mass * (c*c)
    return result

main()
