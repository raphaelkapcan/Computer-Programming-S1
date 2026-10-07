# You need to have at least 30 if statements and no direction can leave the user hanging without instructions.
first_direction = input("You walk into a house for some random reason. Your at the front door. Do you go left or right?")
if first_direction == "left":
    print("You've entered the persons house")
    print("You hear sounds, You see a hallway and there are stairs.")
    x = input("Pick which to follow:\nA. Follow the sounds\nB. Go down the hallway\nC. Go up the stairs")
    if x == "A":
        print("You follow the sounds and you see the tv is on with a man watching it. Do you \nspeak to him or \nleave?")
        y = input("A. Speak to him\nB. Leave")
        if y == "A":
            print("You speak to him and he threatens to call the cops. Do you \nrun or \nstay?")
            z = input("A. Run\nB. Stay")
            if z == "A":
                print("You run and the man calls the cops. Do you \nrun out of the house or \nrun upstairs?")
                a = input("A. Run out of the house\nB. Run upstairs")
                if a == "A":
                    print("You run out of the house and the man calls the cops. Luckily you get away and the cops never find you.")
                elif a == "B":
                    print("You run upstairs and the man calls the cops. You have three places you can go and hide. Do you hide in \nA. The closet\nB. The bathroom\nC. The bedroom") 
                    w = input("A. The closet\nB. The bathroom\nC. The bedroom")
                    if w == "A":
                        print("You hide in the closet and the cops arrive to the house, the man tell them you went upstairs. They search the house and find you in the closet. Do you \nA. Try to run\nB. Give up\nC. Fight the cops")
                        v = input("A. Try to run\nB. Give up\nC. Fight the cops")
                        if v == "A":
                            print("You try to run but the cops block your path. (was that really a good idea?) You are arrested for trespassing.")
                        elif v == "B":
                            print("You give up and the cops arrest you for trespassing.")
                        elif v == "C":
                            print("You throw a punch but the cop dodges it and tases you. You are arrested for trespassing and assult. (Talk about double trouble)")
                    elif w == "B":
                        print("You hide in the bathroom and the cops arrive to the house, the man tell them you went upstairs. They search the house and find you in the bathroom hiding behind the curtain. You are arrested for trespassing.")
                    elif w == "C":
                        print("You hide in the bedroom and the cops arrive to the house, the man tell them you went upstairs. They search the house and find you in the bedroom. You are arrested for trespassing.")   
            elif z == "B":
                print("You stay and the man keeps telling you to leave. Do you \nA. Leave\nB. Stay \nC. Fight the man \n D. Call the cops on him \n E. Laugh at him")
                if z == "A":
                    print("You say trick or treat and leave. You are safe.")
                elif z == "B":
                    print("You stay you ask the man for candy. He says he doesn't have any and tells you to leave.")
                elif z == "C":
                    print("You fight the man and he overpowers you. He calls the cops and you are arrested for trespassing and assult.")
                elif z == "D":
                    print("You call the cops on him for hurting your feelings and they arrive to the house. You tell the cops he is trespassing and the cops arrest him and now you have the hosue to yourself. You are safe and gain a house.")
                elif z == "E":
                    print("")
        elif y == "B":
            print("You leave the room.")
        
    elif x == "B":

    elif x == "C":