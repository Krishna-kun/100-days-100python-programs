def Star_triangle(num):
    print("\n---> Right-Angled Star Triangle <---")
    for i in range(1,num+1):
        for j in range(i):
            print("*",end=" ")
        print()

def Number_triangle(num):
    print("\n---> Numbered Triangle <---")
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def Inverted_star_pattern(num):
    print("\n--- Inverted Star Triangle ---")
    for i in range(num,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

def centered_pyramid(num):
    print("\n--->Centered pyramid<---")
    for i in range(1,num+1):
        for s in range(num-1):
            print(" ",end="")
        for j in range(i):
            print("*",end=" ")
        print()
        

# main loop
# while True:
    print("="*35)
    print("     PATTERN GENERATOR       ")
    print("="*35)
    print("1) Right-Angles star triangle")
    print("2) Number traingle (1,1 2,1 2 3...)")
    print("3) Inverted star triangle")
    print("4) Centered star pattern")
    print("5) Exit")

    choose=int(input("Enter you choice [1,2,3,4,]= "))

    if choose in [1,2,3,4,5]:
        if choose<0:
            print("[!] Number of rows should be gretter than zero")
        else:
            if choose==1:
                Star_triangle(choose)
            elif choose==2:
                Number_triangle(choose)
            elif choose==3:
                Inverted_star_pattern(choose)
            elif choose==4:
                centered_pyramid(choose)
            elif choose==5:
                print("Have a nice day...")
    else:
        print("[!] invalid input...")
