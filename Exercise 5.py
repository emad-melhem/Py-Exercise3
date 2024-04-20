earning= input("Enter your number1 :").strip()
try:
    val1 = float(earning)
    if val1 < 0:
        raise IndexError("Number is less than null!") 
    elif val1 <= 67000:
        print(f"Your income after taxes is {val1 - val1*24/100} euro’s")
    elif val1 <= 97000:
        print(f"Your income after taxes is {val1 - val1*31/100} euro’s")
    else:
        print(f"Your income after taxes is {val1 - val1*34/100} euro’s")
    
except ValueError:
    print("That's not a Number!")
except IndexError as indexerror:
    print(indexerror.args)