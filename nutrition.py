def main(): #main() function to call all other functions
    fruit = input("Item: ").lower().strip()

    calorie = calories(fruit) #calling calories() function once to optimise the code
    if calorie != None:
        print("Calories: ", calorie, sep = "")

def calories(fruit):
    calories = [ #calories is the list of objects
        {"apple": 130},
        {"avocado": 50},
        {"banana": 110},
        {"cantaloupe": 50},
        {"grapefruit": 60},
        {"grapes": 90},
        {"honeydew melon": 50},
        {"kiwifruit": 90},
        {"lemon": 15},
        {"lime": 20},
        {"nectarine": 60},
        {"orange": 80},
        {"peach": 60},
        {"pear": 100},
        {"pineapple": 50},
        {"plums": 70},
        {"strawberries": 50},
        {"sweet cherries": 100},
        {"tangerine": 50},
        {"water melon": 80}
    ]

    #object is a variable nothing but calories[i]
    #first we have to call list, then object in list, then that particular value
    for object in calories:
        if fruit in object: #if string fruit is there inside object dictionary
            return object[fruit] #then return object[fruit] or calories[i][fruit]

main()
