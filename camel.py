#taking camel string input from the user
camel = input("cameCase: ")

#length of the string
n = len(camel)

#initiating i = last str character i = n - 1
i = n - 1

#initiating new empty string to store final snake_case string
new = ""

#while loop from last character to first character in reverse order
while i >= 0:

    #if the character is capital
    if 65 <= ord(camel[i]) <= 90:

        #then before the capital character add undeerscore + lower of capital
        #also everything is added before new because we are coming in reverse
        new = "_" + camel[i].lower() + new
        i = i - 1

    #if the character is not capital, then add directly to the new string
    elif 97 <= ord(camel[i]) <= 122:
        new = camel[i] + new
        i = i - 1

#printing final output string
print(new)


"""
DRY RUN:
-----------------------------------------------------------
camelcase = input("camelCase: ")

n = len(camelcase)

x = 0
for i in range(n):
    if 65 <= ord(camelcase[i]) <= 90:
        x += 1

if x == 0:
    print(camelcase)

elif x == 1:
    for i in range(n):
        if 65 <= ord(camelcase[i]) <= 90:
            y = i
            break
        else:
            continue
    first, second = camelcase.split(camelcase[y])
    print(first + "_" + camelcase[y].lower() + second)

new = ""
elif x == 2:
    for i in range(n):
        if 65 <= ord(camelcase[i]) <= 90:
            y = i
            break
        else:
            continue
    i = y + 1
    while i < n:
        if 65 <= ord(camelcase[i]) <= 90:
            z = i
            break
        else:
            i += 1
            continue
    first, second = camelcase.split(camelcase[y])
    new = first + "_" + camelcase[y].lower() + second

    second_one, second_two = second.split()

-----------------------------------------------------------
"""
