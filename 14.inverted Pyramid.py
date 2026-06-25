row=int(input("ENTER THE NUMBER OF ROWS : "))
for i in range (1 , row + 1):
    
    for j in range (1 , i ):
        print(" " , end=" ")

    for j in range (1 , row - i + 2):
        print("*  " , end=" ")

    print()