letter=input("Enter a String :").strip()
vowel="a","e","i","u","y"
for x in letter:
    if x in vowel:
        print(f"{x} is a vowel.")
    else:
        print(f"{x} is not a vowel.")
if not letter:
    print("String is empty.")