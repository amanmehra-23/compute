x = int(input("enter number of rows: "))

for i in range(x): #if my input is 5 so the loop will run from 0 to x-1 that is 4

    for j in range(x-i-1): #from 0 to 5-i-1 matlab 0 to 4-i 
        print(" ", end="")

    for k in range(2 * i + 1): #+1 as when i =0 we need to print 1 star *2 as it gives the pyra pattern otheriwse its half pyramid 

        if k == 0 or k == 2 * i or i == x - 1: #when k =0 we have to print the first star when  i =x-1 we print the entire line of stars when k 2*i bsically every row we print 2 "*s"
                print("*", end="")
        else:
            print(" ", end="")

    print()
