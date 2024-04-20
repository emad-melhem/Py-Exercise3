number1= input("Enter your number1 :").strip()
number2= input("Enter your number2 :").strip()
number3= input("Enter your number3 :").strip()
number4= input("Enter your number4 :").strip()
try:
    val1 = int(number1)
    val2 = int(number2)
    val3 = int(number3)
    val4 = int(number4)
    x= max(val1, val2, val3, val4)
    print(f"The largest number is {x}")
    
except ValueError:
    print("That's not a Number!")