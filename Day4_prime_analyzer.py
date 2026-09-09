def findprime(n):
    if n<=1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def factors(n):
    fact=[]
    for i in range(1,num+1):
        if num%i==0:
            fact.append(i)

    return fact

def primes_in_range(start,end):
    plst=[]
    for i in range(start,end+1):
        if findprime(num):
            plst.append(num)

    return plst

#main loop
while True:
    print("="*35)
    print("     MATHS MACHINE       ")
    print("="*35)
    print("1)Check if a number is prime or not")
    print("2)Check how many factors a number have")
    print("3)Get list of all prime numbers in a specific range")
    print("4)exit")
    print("="*35)

    choice=int(input("Enter your choice[1,2,3,4]: "))

    

    if choice==1:
        num=int(input("Enter a number to check to prime or not: "))
        if findprime(num):
            print(f"==>the {num} is prime")
        else:
            print(f"==>the {num} is not prime") 
        input("\nPress Enter to continue...")
    elif choice==2:
        num=int(input("Enter the number to check how many factors it have: "))
        factor=factors(num)
        print(f"Factors of {num} is: {factor}")
        print(f"Number of factors of {num} is:{len(factor)}")
        input("\nPress Enter to continue...")

    elif choice==3:
        numS=int(input("Enter start of range: "))
        numE=int(input("Enter end of range: "))
        primelst=primes_in_range(numS,numE)
        print(f"Total prime numbers in the given range is{primelst}")
        print(f"Number of prime in the given range:{primelst}")

    elif choice==4:
        print("Have a nice day!!...")

    else:
        print("[!] invalid input")


