prompt = input("Input: ").strip()
vowels = ["a","e","i","o","u","A","E","I","O","U"]
for char in prompt:
    if char not in vowels:
        print(f"{char}",end="")
    else:
        print(f"",end="")
print()

