def get_fibonacci(num):
    series=[]
    if num<=0:
        return []

    a=0
    b=1
    for i in range(num):
        series.append(a)
        next_term=a+b
        a=b
        b=next_term
    return series

def check_armstrong(num):
    if num<=0:
        return False
    power=len(str(num))
    total=0
    temp=num
    while temp>0:
        digit=temp%10
        total=total+(digit**power)
        temp=temp//10
    return total==num

def check_armstrong_range(strt,end):
    armstrong_found=[]
    for num in range(strt,end+1):
        if check_armstrong(num):
            armstrong_found.append(num)
    return armstrong_found 

#main loop 

while True:
    print("="*35)
    print("     NUMBER WIZARD       ")
    print("="*35)
    print("1) Generate Fibonacci sequence")
    print("2) check if a number is Armstrong")
    print("3) Find all armstrong number in a range")
    print("4) exit")

    choose=int(input("Choose number [1,2,3,4]: "))

    if choose==1:
        num=int(input("how many terms do you want: "))
        if num<=0:
            print("[!]Invalid, please enter positive integer")
        else:
            Result=get_fibonacci(num)
            print("Here is the Fibonacci sequence:",Result)
            input("Press enter to continue...")

    elif choose==2:
        num=int(input("Enter an Integer: "))
        if check_armstrong(num):
            print(f"{num} is an armstrong number!!")
        else:
            print(f"{num} is not an armstrong number!!")

        input("Press enter to continue...")

    elif choose==3:
        strt=int(input("Enter starting number:"))
        end=int(input("Enter ending number:"))
        if strt>end:
            print("[!] Starting number cant be smaller than ending number")
        else:
            Result=check_armstrong_range(strt,end)
            print(f"Armstrong number between {strt} and {end} is: ",Result)

        input("Press enter to continue...")

    elif choose==4:
        print("Have a nice day!!!")

        break

    else:
        print("[!] Enter number between [1,2,3,4]")