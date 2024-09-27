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
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        if 0 < int(month) <= 12 and 0 < int(day) <= 31:
            break
    except:
        try:
            m, dy, year = date.split()
            for i in range(len(months)):
                if m == months[i]:
                    month = i + 1
            day = dy.rstrip(",")
            if 0 < int(month) <= 12 and 0 < int(day) <= 31:
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
