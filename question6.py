numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

choice = input("Select which list to check \n1] X  \n2] Y \n")
if(choice == "X"):
    if numbers_x[0] == numbers_x[len(numbers_x) - 1 ]:
       print("YES")
    else:
        print("No")
elif(choice == "Y"):
     if numbers_y[0] == numbers_y[len(numbers_y) - 1 ]:
       print("YES")
     else:
        print("No")