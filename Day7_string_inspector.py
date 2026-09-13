def palindrome_checker(user_text):
    print("--->Palindrome Test<---")
    cleaned=""
    for char in user_text.lower():
        if char.isalnum():
            cleaned += char
    reversed_strg=cleaned[::-1]
    print("Original string: ",user_text)
    print("Cleaned string: ",cleaned)
    print("reversed string: "reversed_strg)

    if not cleaned:
        print("[!]The text doesn't contain any text or symbol")
    elif reversed_strg==user_text:
        print("[RESULT] It's a palindrome")
    else:
        print("[RESULT] It's not a palindrome")

def count_vowels(user_text):
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

    choose=int(input("Enter your choice[1,2,3,4,5]: "))
