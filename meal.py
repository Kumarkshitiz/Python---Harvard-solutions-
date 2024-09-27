def main():
    Time = input("What time is it? ")
    timing = convert(Time)
    if 7<= timing <=8 :
        print("breakfast time")
    elif 12<= timing <=13 :
        print("lunch time")
    elif 18<= timing <=19 :
        print("dinner time")

def convert(time):
    hrs, minutes = time.split(":")
    min_decimal = int(minutes)/60
    time_decimal = int(hrs) + min_decimal
    return time_decimal

if __name__ == "__main__":
    main()
