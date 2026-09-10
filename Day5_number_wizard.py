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
    

#main loop 

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

#elif choose==2:
