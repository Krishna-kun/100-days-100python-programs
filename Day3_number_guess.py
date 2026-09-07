import random
def game():
    secret_num=random.randint(1,10)
    attempt=3
    print("="*35)
    print("SYSTEM HAS SELECTED A NUMBER!! beteween 1 to 10")
    print("TRY YOUR BEST TO GUESS IT...")
    input("Press Enter to continue...")
    while True:
        
        guess=int(input("Enter the number you guessed: "))
        if guess==secret_num:
            print("CONGOO you guessed it 0_0")
            break
        elif guess>secret_num:
            attempt=attempt-1
            print("guessed a bit higher...attempt left:",attempt)

        elif guess<secret_num:
            attempt=attempt-1
            print("guessed a bit lower...attempt left:",attempt)
        
        else:
            print("INVALID input")

        if attempt == 0:
            print("GAME OVER! You ran out of attempts.")
            print("The secret number was:", secret_num)
            break

        
while True:
    print("="*30)
    print("     GUESSING NUMBER     ")
    print("="*30)
    print("1) lets start the game")
    print("2) exit")
    print("="*30)
    choice=int(input("Choose 1 or 2: "))
    if choice==1:
        game()
        input("Press enter to get back to menu...")
    elif choice==2:
        print("byee have a good day...")
        break
    else:
        print("INVALID input")
        break