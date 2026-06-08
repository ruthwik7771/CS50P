#total price is 50 cents
price = 50

#due amount intial value is set to 50 cents
amount_due = 50

#while loop till amount_due is greter than or equal to zero, once the amount_due == 0 the loop breaks
while amount_due >= 0:
    print("Amount Due: ", amount_due, sep="")
    a = int(input("Insert Coin: ")) #input

    #accepted inputs are 25, 10 and 5 cents
    if a == 50 or a == 25 or a == 10 or a == 5:

        #in the order, first the amount_due will be positive, after paying it becomes zero and then negative
        #so, if and else considering both cases

        if amount_due - a >= 0: #remaining amount is non-negative
            amount_due = amount_due - a #there is still due left

            if amount_due == 0: #no due, so printing change owed == 0, and then equating amount_due == 0
                print("Change Owed: 0", sep = "")
                amount_due = 0
                break #amount_due = 0, so break

        elif amount_due - a < 0: #remaining amount is negative

            #change can only be in 5, 10, 25 cents
            if a - amount_due == 5 or a - amount_due == 10 or a - amount_due == 25 or a - amount_due == 50:

                #after giving the change, make amount_due becomes 0, and the loop breaks
                print("Change Owed: ", a - amount_due, sep="")
                amount_due = 0
                break

