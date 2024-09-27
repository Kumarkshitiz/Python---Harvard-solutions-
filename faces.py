def convert(value):
    return value.replace(":)","🙂").replace(":(","🙁")
def main():
    prompt = input("Enter an input: ")
    print(convert(prompt))

if __name__ == "__main__":
    main()
