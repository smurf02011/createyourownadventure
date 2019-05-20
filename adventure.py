# Create your own destiny

print("You are on a deserted island in a 2D world!")
print("Try to survive until rescue arrives!")
print("Available commands are in CAPITAL LETTERS")
print("Any other command exits the program")
print("First LOOK around....")

do = input(":: ")
if do == "LOOK":
    print('You are stuck in a sand ditch')
    print("Crawl out LEFT or RIGHT")
do = input(":: ")
if do == "LEFT":
        print("You see a STARFISH and a CRAB on the sand")
        print("And you're hungry! Which do you eat?")
        do = input("::")
        if do == "STARFISH":
            print("Oh no! You immediately don't feel well")
            print("You do not survive :()")
        elif do == "CRAB":
           print("Raw crab should be fine, right? YES OR NO.")
           do = input("::")
           if do == "YES":
                print("Ok, You eat it raw, fingers crossed")
                print("Food in your belly helps you see a TREE")
                do = input("::")
           if do == "TREE":
                print("Its a cocount tree! And you're thirsty!")
                print("Do you drink the coconut water? YES or NO.")
                do = input("::")
                if do == "YES":
                    print("Oh boy. Coconut water and raw crab don't mix.")
                    print("You do not survive:()")
                elif do == "NO":
                    print("Good choice")
                    print("Look! It's a rescue plane! You made it! o/")

elif do == "RIGHT":
        print("No can do. That side is very slippery.")
        print("You fell very far into some weird cavan.")
        print("You do not survive :()")
else:
        print("You can only do actions in CAPITAL LETTERS")
        print("Try Again")
