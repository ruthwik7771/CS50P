#main() function to input, call twttr() and print output
def main():

    twitter = input("Input: ")
    output = twttr(twitter)
    print("Output: ", output, sep="")

#twttr() to remove vowels from the string
def twttr(twitter):

    new_str = "" #new string initiated to store final output string
    n = len(twitter) #string length
    for i in range(n): #for loop to go character by character
        if twitter[i].lower() not in "aeiou": #if after lowering that character, it is not there in the "aeiou", then add it to the new_str
            new_str += twitter[i]
    return new_str #return the new_str

main()

"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DRY RUN
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def twttr(twitter):

    new_twitter = twitter.replace("a", "").replace("e","").replace("i","").replace("o","").replace("u","").replace("A","").replace("E","").replace("I","").replace("O","").replace("U","")
    return new_twitter

twitter = input("Input: ")

print("Output: ", twttr(twitter), sep="")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
