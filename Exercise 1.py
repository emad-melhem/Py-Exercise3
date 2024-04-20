letter=input("Enter a String :").strip()
vowel="a","e","i","u","y"
for x in letter:
    if x.lower() in vowel:
        print(f"{x} is a vowel.")
    elif x.strip():
        print(f"{x} is not a vowel.")
    else:
        print(f"{x} is empty.")
if not letter:
    print("String is empty.")