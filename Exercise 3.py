number1= input("Enter your number1 :").strip()
number2= input("Enter your number2 :").strip()
number3= input("Enter your number3 :").strip()
try:
    val1 = int(number1)
    val2 = int(number2)
    val3 = int(number3)
    if val1 == val2 and val2 == val3:
        print(f"These numbers are the same!\nThe sum of these numbers is {3*val1}\nMultiplied by 4 this becomes {4*3*val1}")
    else:
        print(f"The sum of these numbers is {val1+val2+val3}")
except ValueError:
    print("That's not a Number!")