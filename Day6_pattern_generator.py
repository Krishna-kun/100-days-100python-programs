def Star_triangle(num):
    print("---> Right-Angled Star Triangle <---")
    for i in range(1,num+1):
        for j in range(i):
            print("*",end=" ")
        print()

def Number_triangle(num):
    print("---> Numbered Triangle <---")
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def Inverted_star_pattern(num):
    for i in range(num,0,-1):
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

    if choose==1:
        num=int(input("Enter the number of rows for pattern(eg.5): "))
        if num<=0:
            print("[!] Number of rows must be greatter than zero")
        elif num>0:
            result=Star_triangle(num)
            print(result)