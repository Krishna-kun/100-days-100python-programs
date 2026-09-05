import random
import string

def all_char(len):
    letters=string.ascii_letters
    digits=string.digits
    symbols=string.punctuation

    all_char=letters+digits+symbols

    password=" "
    
    for i in range(len):
        random_char=random.choice(all_char)
        password=password+random_char

    return password

while True:
    print("="*30)
    print("     PASSWORD GENERATOR      ")
    print("="*30)
    print("1) Generate a password")
    print("2) Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        length=int(input("Enter length of password:"))
        if length<4:
            print("password can't be this short")
        else:
            new_pass=all_char(length)
            print("==> New Password is:",new_pass)

            input("Press enter to continue...")

    elif choice==2:
        print("bye bye twin!")
        input("Press enter to continue...")

    else:
        print("[!]INVALID INPUT")
