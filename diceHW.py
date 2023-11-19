import random

reroll = "y"

while reroll == "y":
    num = random.randint(1, 6)
    
    print(num)
    if num == 1:
        print("[   ]")
        print("[ * ]")
        print("[   ]")    
    elif num == 2:
        print("[*  ]")
        print("[   ]")
        print("[  *]") 
    elif num == 3:
        print("[*  ]")
        print("[ * ]")
        print("[  *]") 
    elif num == 4:
        print("[* *]")
        print("[   ]")
        print("[* *]") 
    elif num == 5:
        print("[* *]")
        print("[ * ]")
        print("[* *]")
    elif num == 6:
        print("[***]")
        print("[   ]")
        print("[***]")  
        
    reroll = input("Type y to play again and n to stop\n>>> ")
