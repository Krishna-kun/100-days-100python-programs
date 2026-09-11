def Star_tri(num):
    print("---> Right-Angled Star Triangle <---")
    for i in range(1,num+1):
        for j in range(i):
            print("*",end=" ")
        print()

def Number_triangle(num):
    print("---> Numbered Triangle <---")
    for i in range(1,num+1):
        for j in range(i):
            print(f"{i}",end=" ")
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

    # if