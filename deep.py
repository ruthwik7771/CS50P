#taking input and striping and lowering all at the same time
response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

#writing if else for responses
if response == "42" or response == "forty-two" or response == "forty two":
    print("Yes")
else:
    print("No")
