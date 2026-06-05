#fuction thefightclub() just to list out the characters and print them directly
def thefightclub():

    #character input list
    characters = ["Tyler Durden", "The Narrator", "Marla Singer", "The  Bob"]

    print("Characters of The Fight Club (1999): ")

    #a for loop to print each and every character name in sequence
    for i in range(len(characters)):
        print(i + 1, characters[i])

#calling thefightclub() function
thefightclub()
