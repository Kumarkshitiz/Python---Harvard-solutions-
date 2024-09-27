while True:
    fraction = input("Fraction: ")
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        percent = x/y
        if percent <= 1 :
            break
    except (ValueError, ZeroDivisionError):
        pass

percentage = round(percent * 100)
if percentage <= 1 :
    print("E",end ="")
elif percentage >= 99 :
    print("F",end ="")
else:
    print(f"{percentage}%", end= "")
