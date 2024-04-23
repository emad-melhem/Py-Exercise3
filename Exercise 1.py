letter=input("Enter a String :").strip()
vowel="a","e","i","u","y"
for x in letter:
    if x.lower() in vowel:
        print(f"{x} is a vowel.")
    elif x.isalpha():
        print(f"{x} is not a vowel.")
    elif x == " ":
        print(f"{x} is empty.")
    else:
        print(f"{x} is not letter.")
if not letter:
    print("String is empty.")