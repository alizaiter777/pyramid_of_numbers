
x = int(input("Enter x : "))
#start count from 1 to x which x is the input from user 
for i in range (1,x+1):
    #then take i and list all numbers before it presented by j
    for j in range(1,i+1):
        print(j,end=" ")
    print("")