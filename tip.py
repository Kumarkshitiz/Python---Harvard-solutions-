def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    bill = d.replace("$","")
    return round(float(bill),1)


def percent_to_float(p):
    tip = p.replace("%","")
    tip_float = float(tip)
    return (tip_float/100)

main()
