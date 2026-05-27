def main():
    users_time = input("What time is it? ")
    result = convert(users_time)
    if result is not None:
        if 7 <= result <= 8:
            print("breakfast time")
        elif 12 <= result <= 13:
            print("lunch time")
        elif 18 <= result <= 19:
            print("dinner time")

#Added the challenge for AM and PM times, works on both 24h and 12h time formats.
def convert(time):
    hours, minutes_f = time.split(":")
    if len(minutes_f.split()) == 2:
        minutes, format = minutes_f.split()
        if format == "p.m.":
            if hours == "12":
                time = int(hours) + int(minutes)/60
            else:
                time = (int(hours)+12) + int(minutes)/60
        elif format == "a.m.":
            if hours == "12":
                time = 0
            else:
                time = int(hours) + int(minutes)/60
    else:
        time = int(hours) + int(minutes_f)/60

    return time
if __name__ == "__main__":
    main()
