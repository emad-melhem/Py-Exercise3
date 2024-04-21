import random

def _GetNewQuwstion():
    x=random.randint(1, 10)
    y=random.randint(1, 10)
    operator=random.choice(["*", "+","-"])
    result = False
    retresult = int(input(f"What is {x} {operator} {y}?"))
    
    if operator == "*":
        result = retresult == x * y
    elif operator == "+":
        result = retresult == x + y
    else:
        result = retresult == x - y
        
    if result:
        print("That is correct!")
    else:
        print("That is false, you failed the test.")
    return result


try:
    x=0
    while x < 3:
        if not _GetNewQuwstion():
            break
        x+=1
        if x == 3:
            print("All is correct! You passed the test!")
except ValueError:
    print("That's not a Number! \nThat is false, you failed the test.")