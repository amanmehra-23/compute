x = int(input("ente number of rows: "))
c = "A"
n  = 1

for i in range(1,x+2):
    for j in range(1,i):
        if(i%2==0):
            print(f"{c} ", end="")
        else:
            print(f"{n} ", end="")
        c= chr(ord(c) +1)
        n = n +1
    print()
        