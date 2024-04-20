letter= input("Enter a string with a maximum size of 5 :").strip()
try :
    if len(letter) < 1 and len(letter) > 5:
        raise ValueError("The number of letters out of rang!")
    if len(letter) == 1:
        print(f"{letter} = {letter*6}.")
    elif len(letter) == 2:
        print(f"{letter[1]}{letter[0]}.")
    elif len(letter) == 3:
        print(f"{letter[2]}{letter[0]}{letter[1]}.")
    elif len(letter) == 4:
        list=letter[::-1]
        print(f"{list}.")
    else:
        print(letter[0],letter[1],letter[2], letter[3], letter[4], sep="t")
        #other way
        """
        newletter=""
        for x in letter:
            newletter+= x+"t"
        newletter=newletter+"\b."
        print(newletter)
        """

except ValueError:
    print("That's not a Number!")