for row in range(5):
    for col in range(5):
        if(col==0 or col==4) or (row==2 and 0<col<4) or(row==col or col+row==4):
            print("*", end='')
        else:
            print(" ", end='')
    print()