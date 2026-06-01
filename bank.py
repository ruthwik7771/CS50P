#take the input and stripping and lowering at the same time
greeting = input("Greeting: ").strip().lower()

#reading each and every starting letters and not just checking for the same string
if greeting[0] == "h" and greeting[1] == "e" and greeting[2] == "l" and greeting[3] == "l" and greeting[4] == "o":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
