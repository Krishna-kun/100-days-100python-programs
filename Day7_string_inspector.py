def palindrome_checker(text):
    print("\n---> Palindrome Test <---")
    # Clean string: lowercase and keep alphanumeric characters only
    cleaned = ""
    for ch in text.lower():
        if ch.isalnum():
            cleaned += ch