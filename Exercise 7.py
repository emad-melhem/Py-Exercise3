import random

resCountTest=0

def _GetNewQuwstion():
    x=random.randint(1, 10)
    y=random.randint(1, 10)
    operator=random.choice(["*", "+"])
    result = False
    if operator == "*":
        retresult = int(input(f"What is {x} * {y}?"))
        if retresult == x * y:
            print("That is correct!")
            result = True
    else:
        retresult = int(input(f"What is {x} + {y}?"))
        if retresult == x + y:
            print("That is correct!")
            result = True
    return result

x=0
while x < 3:
    if not _GetNewQuwstion():
        print("That is false, you failed the test.")
        break
    else:
        resCountTest +=1
    x+=1

if resCountTest == 3:
    print("All is correct! You passed the test!")