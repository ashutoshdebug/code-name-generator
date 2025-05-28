def codename():
    name = input("Enter your name:")
    code = []
    for char in name.lower():
        if char.isalpha():
            code.append(ord(char) - ord('a')+1)
        else:
            print("Invalid characters!")
    
    print(*code, sep='')
codename()
