def main():
    swap_date()

def swap_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                if not month.isnumeric() or not day.isnumeric() or not year.isnumeric():
                    continue
            else:
                if "," not in date:
                    continue
                month, day, year = date.split(" ")
                day = day.strip(",")
                try:
                    month = months.index(month)+1
                except ValueError:
                    continue

            if int(day) not in range(1,31):
                continue
            if int(month) not in range(1,12):
                continue
            print(f"{year}-{int(month):02d}-{int(day):02d}")
            return
        except EOFError:
            return

main()
