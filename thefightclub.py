#dict of characters and their details of Fight Club(1999) movie
characters = [
    {"Character Name": "The Narrator", "Name": "Edward Norton", "Place": "Condominium"},
    {"Character Name": "Tyler Durden", "Name": "Brad Pitt", "Place": "Derelict House"},
    {"Character Name": "Marla Singer", "Name": "Helena Carter", "Place": None}
]

#for loop to iterate between all the characters
for character in characters:
    
    #character["Character Name"] means what is "character name" mapped to in the particular character row
    print(character["Character Name"], character["Name"], character["Place"], sep = ", ")


"""
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
"""

