def main():
    print(get_change())

def insert_coin():
    coin = int(input("Insert Coin: "))
    return coin

def get_change():
    cost = 50
    while cost > 0:
        print(f"Amount Due: {cost}")
        coin = insert_coin()
        if coin in (5, 10, 25):
            cost -= coin

    return "Change Owed: " + str(-cost)

main()
