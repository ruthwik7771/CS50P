#new function get_number() to get only positive input from the user
def get_number():

    #this while loop will operate until we get positive value of n, if we get positive value we break
    while True:

        #takes n value input as integer
        n = int(input("What's n value? ")) 

        #if n is negative, it asks user for a positive value and goes for another loop
        if n < 0:
            print("n value must be positive")
            continue

        #if n is positive, then the loop breaks and takes that particular n value
        else:
            break
    
    #returns n value as an integer, n = get_number()
    return n

#new main() function to call other functions and give required output
def main():

    #n takes the value given by get_number
    n = get_number()

    #then applies the meow() with n
    meow(n)

#prints n number of meow's
def meow(n):

    #for loop to print meow n times
    for _ in range(n):

        #want meow and next meow side-by-side
        print("Meow", end=" ")

#calling the main() function at last
main()
