def main():

    #taking time input and removing all empty spaces
    time = input("What time is it? ").replace(" ", "")

    #the value from convert() is assigned to new variable score
    score = convert (time)

    """print(score)"""

    #to estimate the value and print time according to it
    if 7.0 <= score <= 8.0:
        print("breakfast time")
    elif 12.0 <= score <= 13.0:
        print("lunch time")
    elif 18.0 <= score <= 19.0:
        print("dinner time")


#new function convert to convert 24-hour format to a particular score value
def convert(time):

    #split time into hour and minute
    hour, minute = time.split(":")

    #calculating score for example 7:30's score is 7.50
    score = float(hour) + ( float(minute) / 60 )

    #rounding off score to two decimal places
    return round(float(score), 2)

if __name__ == "__main__":
    main()
