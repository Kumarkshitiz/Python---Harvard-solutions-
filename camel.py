def main():

    prompt = input("camelCase: ")
    for char in prompt:
        if char.isupper():
            print(f"_{char.lower()}", end="")
        else:
            print(f"{char}", end="")
    print()
main()



#if found append_ and make small
#print output
#


