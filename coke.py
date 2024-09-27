due = 50
paid = 0

while due > 0 :
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
      due = due - coin

change = due
print(f"Change Owed: {abs(change)}")

