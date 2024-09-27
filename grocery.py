groceries = {}
while True:
    try:
        grocery = input().lower().strip()
        if grocery:
            if grocery in groceries:
                groceries[grocery] += 1
            else:
                groceries[grocery] = 1
        else:
            raise ValueError("Empty input")
    except EOFError:
        break
    except ValueError as e:
        print(e)

for key in sorted(groceries.keys()):
    print(groceries[key], key.upper())
