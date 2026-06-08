#main() to call all functions
def main():
    plate = input("Plate: ")
    if is_valid(plate): #is_valid() is a function for overall checks
        print("Valid")
    else:
        print("Invalid")


def is_valid(s): #checking all conditions, if they are all true, then overall true
    if first(s) == "True" and second(s) == "True" and third_i(s) == "True" and third_ii(s) == "True" and fourth(s) == "True":
        return True
    else:
        return False


def first(s): #checking if first two characters are alphabets
    if len(s) == 1: #only if one character is there in the string
        if 97 <= ord(s[0].lower()) <= 122:
            return True
        else:
            return False

    elif len(s) >= 2: #if more than one characters are present in string
        if 97 <= ord(s[0].lower()) <= 122 and 97 <= ord(s[1].lower()) <= 122:
            return True
        else:
            return False

def second(s): #second to check if there are min 2 and max 6 characters in the string
    if 2 <= len(s) <= 6:
        return True

def third_i(s): #third_i to verify if there are no alphabets after numbers
    for i in range(len(s) - 1):
        if 48 <= ord(s[i]) <= 57 and 97 <= ord(s[i+1]) <= 122:
            return False
        else:
            return True

def third_ii(s): #third_ii to verify if first number is not 0
    x = 0
    for i in range(len(s)):
        if 48 <= ord(s[i]) <= 57:
            x = i
            break

    if s[x] == 0:
        return False
    else:
        return True

def fourth(s): #fourth to verify if all characters are only alphabets and numbers only
    a = 1
    for i in range(len(s)):
        if 48 <= ord(s[i]) <= 57 or 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
            a = 1
        else:
            a = 0
            break
    if a == 0:
        return False
    elif a == 1:
        return True

main() #finally, executing the main() function
