#main() function to call print square with side length 3
def main():
    print_square(3)

#print_square(side) function to print square with side length "side"
def print_square(side):

    #for loop to iterate columns
    for _ in range(side):

        #for loop to iterate over row
        for _ in range(side):
            
            #printing # along with tab space for perfect square
            print("#    ", end="")

        #printing \n so that once a row is finished, it goes to the new row
        print("\n")

#calling main() function
main()
