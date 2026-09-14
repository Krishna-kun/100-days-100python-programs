def palindrome_checker(user_text):
    print("\n--->Palindrome Test<---")
    cleaned=""
    for char in user_text.lower():
        if char.isalnum():
            cleaned += char
    reversed_strg=cleaned[::-1]
    print("\nOriginal string: ",user_text)
    print("Cleaned string: ",cleaned)
    print("reversed string: ",reversed_strg)

    if not cleaned:
        print("\n[!]The text doesn't contain any text or symbol\n")
    elif reversed_strg==user_text:
        print("\n[RESULT] It's a palindrome\n")
    else:
        print("\n[RESULT] It's not a palindrome\n")

    input("Press enter to continue...")

def count_vowels(user_text):
    print("\n--->Words Identfier<---")
    vowels=0
    consonents=0
    digits = 0
    spaces = 0
    specials = 0
    vowelLETTERS="aeiouAEIOU"
    for ch in user_text:
        if ch.isdigit():
            digits+=1
        elif ch.isalpha():
            if ch in vowelLETTERS:
                vowels+=1
            else:
                consonents+=1
        elif ch.isspace():
            spaces+=1
        else:
            specials+=1

    print("\nTotal characters :",len(user_text))
    print("Vowels           :",vowels)
    print("Consonents       :",consonents)
    print("Spaces           :",spaces)
    print("digits           :",digits)
    print("Specials         :",specials)

    input("\nPress enter to continue...")

def reverse_each_word(user_text):
    print("\n--->Reverse each word<---")
    words=user_text.split(" ")
    for word in words:
        reversed_word=words[::-1]
        result=" ".join(reversed_word)

    print("\nOriginal text    :",user_text)
    print("Reversed text     :",result)
    input("\nPress enter to continue...")

def slicing_formt(user_text):
    
    print("\n---> Slicing & Case Demo <---\n")
    print(f"Full Reverse (s[::-1])      : {user_text[::-1]}")
    print(f"Even Indices (s[::2])       : {user_text[::2]}")
    print(f"Odd Indices  (s[1::2])      : {user_text[1::2]}")
    print(f"Uppercase    (.upper())     : {user_text.upper()}")
    print(f"Lowercase    (.lower())     : {user_text.lower()}")
    print(f"Title Case   (.title())     : {user_text.title()}")
    print(f"Trim Edges   (.strip())     : {user_text.strip()}")

    input("\nPress enter to continue...")
#main loop 
while True:
    print("="*35)
    print("     STRING INSPECTOR       ")
    print("="*35)
    print("1) Palindrome Checker")
    print("2) Vowel, Consonant & Digit Counter")
    print("3) Reverse Each Word in Sentence")
    print("4) Slicing & Formatting Tricks")
    print("5) Exit") 

    try:
        choose=int(input("\nEnter your choice[1,2,3,4,5]: "))
    except ValueError:
        print("\n[!] Please enter a valid number.\n")
        continue
    
    user_text = input("Enter your text: ")

    if choose==1:
         palindrome_checker(user_text)
    elif choose==2:
        count_vowels(user_text)
    elif choose==3:
        reverse_each_word(user_text)
    elif choose==4:
        slicing_formt(user_text)

    elif choose==5:
        print("Have a nice day...")

    else:
        print("[!] Invalid input")