"# M1BO-Hello-You" 


#intro oorlog
from telnetlib import AUTHENTICATION


def introoorlog():
    print ("Hello there...")
    print ("This is weird, you here...")
    print ("There is a war going on...")
    vraaga()
    
#vraaga
def vraaga():
    print ("You can a: Hide  b: Walk around  c: Run around")
    anta = input()
    if anta == ("a"):
        print ("You fount a hut...")
        print ("In your hut is no food and water")
        print ("You can't go anywere. The door is broken.")
        print ("You died, because you don't have food or water")
    if anta == ("b"):
        print ("You look around and you see somthing in the distance.")
        vraagb()
    if anta == ("c"):
        print ("You are tired...")
        print ("All that running and you came nowhere...")
        print ("You see nothing but the sun and sand.")
        print ("You have no food or water.")
        print ("You died, because you don't have food or water")
    else:
        print ("Not a option")
        vraaga()

#vraag bij muur
def vraagb():
    print ("Stop were you are now!")
    print ("There is someone on the wall do you a: Stop  b: Walk past")
    antb = input()
    if antb ==("a"):
        print ("Who are you? Wat are you doing here? Who else is out there... The person said.")
        print ("Please help me there was a war in my home land and I had to flee... You said.")
        uitlegfac()
    if antb ==("b"):
        print ("The people on the wall don't like that and saw you as a risk for there security")
        print ("You were shoot till dead")
    else:
        print ("Not a option")
        vraagb()
#uitleg groepen in de muur
def uitlegfac():
    print("We work in a system here in the walls. To keep order and happiness.")
    print ("The funtions are groups. We have 5 groups but if you don't belong in one of them you become Factoinless.")
    print ("Abnegation")
    print ("Selfless, if you go to this group")
    print ("Amity")
    print ("Paechful, if you go to this group")
    print ("Candor")
    print ("Honest, if you go to this group")
    print ("Dauntless")
    print ("Brave, if you go to this group")
    print ("Erudite")
    print ("Intellectual, if you go to this group")
    vraagc()


#vraag wat bij jouw past
def vraagc():
    print ("What do you want to be in this world?")
    print ("a: Abnegation  b: Amity  c: Candor  d: Dauntless  e: Erudite")
    antc = input()
    if antc ==("a"):
        print ("")
    if antc ==("b"):
        print ("")
    if antc ==("c"):
        print ("")
    if antc ==("d"):
        print ("")
    if antc ==("e"):
        print ("")
    else:
        print ("Not a option")
        vraagc()
    



introoorlog()
def voorbeeldq():
    print ("")
    antq = input()
    if antq ==("a"):
        print ("")
    if antq ==("b"):
        print ("")
    if antq ==("c"):
        print ("")
    else:
        print ("Not a option")
        voorbeeldq()