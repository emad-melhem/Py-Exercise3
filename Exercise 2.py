number= input("Enter your number to compare :").strip()
try:
    val = int(number)
    if val < 1000:
        print("This number is lower than 1000.")
    elif val > 2000:
        print("This number is higher than 2000.")
    else:
        print("This number is in between 1000 and 2000.")
except ValueError:
    print("That's not a Number!")