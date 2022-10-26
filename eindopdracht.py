"# M1BO-Hello-You" 


#intro oorlog
from multiprocessing.resource_sharer import stop
from telnetlib import AUTHENTICATION


def introoorlog():
    print ("Hello there...")
    print ("This is weird, you here...")
    print ("There is a war going on...")
    vraaga()
    
#vraag waar je bent en wat je gaat doen
def vraaga():
    print ("You can a: Hide  b: Walk around  c: Run around")
    anta = input()
    if anta == ("a"):
        print ("You fount a hut...")
        print ("In your hut is no food and water")
        print ("You can't go anywere. The door is broken.")
        print ("You died, because you don't have food or water")
        print (end)
        
    if anta == ("b"):
        print ("You look around and you see somthing in the distance.")
        vraagb()
    if anta == ("c"):
        print ("You are tired...")
        print ("All that running and you came nowhere...")
        print ("You see nothing but the sun and sand.")
        print ("You have no food or water.")
        print ("You died, because you don't have food or water")
        print (end)
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
        print (end)
    else:
        print ("Not a option")
        vraagb()
#uitleg groepen in de muur
def uitlegfac():
    print("We work in a system here in the walls. To keep order and happiness.")
    print ("The funtions are groups. We have 5 groups but if you don't belong in one of them you become Factoinless.")
    print ("Abnegation")
    print ("Selfless, if you go to this group you need to put others before yourself. You live to help people. Your job is township of the town.")
    print ("Amity")
    print ("Paechful, if you go to this group you become a famer you need to be kind to people. You show them kindness of people. You become a farmer.")
    print ("Candor")
    print ("Honest, if you go to this group you have a very strong opinion about every thing. You become the jury in court.")
    print ("Dauntless")
    print ("Brave, if you go to this group you overcome your fear(s). You keep orther in this town. That is what I am here. You will be the police.")
    print ("Erudite")
    print ("Intellectual, if you go to this group you can find important stuff and you can play with it. You are very smart and whant to look for new possibilities.")
    vraagc()


#vraag wat bij jouw past
def vraagc():
    print ("What do you want to be in this world?")
    print ("a: Abnegation  b: Amity  c: Candor  d: Dauntless  e: Erudite")
    antc = input()
    if antc ==("a"):
        print ("Good choice, we like others more then ourself. We help the people we help the world.")
        introab()
    if antc ==("b"):
        print ("Good choice, we are friendly to people and animals. We will be helpful for everybody.")
        introam()
    if antc ==("c"):
        print ("Good choice, everybody needs to be honest. In a society you have to speak the truth.")
        introca()
    if antc ==("d"):
        print ("Good choice, we will see what you fear and you will overcome it. You are the hero here not the coward!")
        introda()
    if antc ==("e"):
        print ("Good choice, lets find out what were comes from. Someone has to invent new stuf.")
        introer()
    else:
        print ("Not a option")
        vraagc()

#abnegation intro uitleg    
def introab():
    print ("There is a person on stage they say:")
    print ("Welcome folks, we are the group of Abonegation.We make sure that there is respect that allows us to live here. Our job is to arrange everything in this city, so we make decisions. We are a neural group because we put others before ourselves.")
    print ("You need to come with us for your decision. You walk with them.")

#amity intro uitleg & einde
def introam():
    print ("You were sent to the farm lands.")
    print ("The people here are kind and helpful.")
    print ("A couple years pass and you are still happy were you are.")
    print ("You die peaceful with lots of people that care about you when it is your time.")
    print ("For now you farm with the rest of the people that help you.")
    print (end)
   


#candor into uitleg
def introca():
    print ("So you always tell the truth?")
    print ("Then you belong to this group.")
    print ("Said a man on a podium.")
    print ("We are the jury/judges in this city.")
    print ("We bring justice to this city.")
    print ("You are about to make your first decision and make sure it is judged fairly, otherwise you will be kicked out of this group.")
    print ("Be aware of unable to pick a new one.")
    carecht()



#Dauntless into uitleg
def introda():
    print ("")

#Erudite into uitleg
def introer():
    print ("")


#rechtbank keuze
def carecht():
    print ("Your first assignment in this city.")
    print ("There are a group of people are they guilty?")
    print ("a: Yes (kill them)  b: No (let them go)")
    antcar = input()
    if antcar ==("a"):
        print ("You made the right choice they were guilty.")
        print ("You live happily ever after.")
        print (end)
    if antcar ==("b"):
        print ("You were wrong")
        print ("We have too large a population in this town and we don't want any liars here!")
        print ("You yourself are condemned by your friends in Candor. You were killed by your friends...")
        print (end)
    else:
        print ("Not a option")
        carecht()


end = "The end"

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