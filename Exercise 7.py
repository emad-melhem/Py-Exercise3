import random

def _GetNewQuwstion():
    x=random.randint(1, 10)
    y=random.randint(1, 10)
    operator=random.choice(["*", "+","-"])
    retresult = int(input(f"What is {x} {operator} {y}?"))
    
    if operator == "*":
        result = retresult == x * y
    elif operator == "+":
        result = retresult == x + y
    else:
        result = retresult == x - y
        
    return result

try:
    x=0
    while x < 3:
        if not _GetNewQuwstion():
            print("That is false, you failed the test.")
            break
        elif x < 2:
            print("That is correct!")
        else:
            print("Correct! You passed the test!")
        x+=1
        
except ValueError:
    print("That's not a Number! \nThat is false, you failed the test.")