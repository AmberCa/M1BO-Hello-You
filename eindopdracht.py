"# M1BO-Hello-You" 


from multiprocessing.resource_sharer import stop
from time import sleep

end = "The end"

#intro oorlog
def introoorlog():
    print ("Hello there.")
    print ("This is weird, you here...")
    sleep(2)
    print ("There is a war going on...")
    vraaga()
    
#vraag waar je bent en wat je gaat doen
def vraaga():
    print ("You can a: Hide  b: Walk around  c: Run around")
    anta = input().lower()
    if anta == ("a"):
        sleep(1)
        print ("You found a hut...")
        sleep(2)
        print ("In your hut there is no food and water")
        print ("You can't go anywhere. The door is broken.")
        sleep(3)
        print ("You died, because you don't have any food or water")
        print (end)
        opnieuw()
    elif anta == ("b"):
        sleep(1)
        print ("You look around and you see somthing in the distance.")
        sleep(3)
        vraagb()
    elif anta == ("c"):
        sleep(1)
        print ("You are tired...")
        print ("All that running and you came nowhere...")
        print ("You see nothing but the sun and sand.")
        sleep(2)
        print ("You have no food or water.")
        sleep(3)
        print ("You died, because you don't have food or water")
        print (end)
        opnieuw()
    else:
        print ("Not an option")
        sleep(3)
        vraaga()

#vraag bij muur
def vraagb():
    sleep(1)
    print ("Stop where you are now!")
    sleep(1)
    print ("There is someone on the wall do you a: Stop  b: Walk past")
    antb = input().lower()
    if antb ==("a"):
        sleep(2)
        print ("Who are you? What are you doing here? Who else is out there... The person said.")
        print ("Please help me there was a war in my homeland and I had to flee... You said.")
        uitlegfac()
    elif antb ==("b"):
        sleep(3)
        print ("The people on the wall don't like that, and saw you as a risk for their security")
        print ("You were shot to death")
        sleep(3)
        print (end)
        opnieuw()
    else:
        print ("Not a option")
        sleep(3)
        vraagb()

#uitleg groepen in de muur
def uitlegfac():
    print("We work in a system here in the walls. To keep order and happiness.")
    sleep(1)
    print ("The funtions are groups. We have 5 groups but if you don't belong in one of them you become Factionless.")
    sleep(2)
    print ("Abnegation")
    print ("Selfless, if you go to this group you need to put others before yourself. You live to help people. Your job is township of the town.")
    sleep(1)
    print ("Amity")
    print ("Peaceful, if you go to this group you become a farmer, your personality is to be kind to people. You show them kindness of people.")
    sleep(1)
    print ("Candor")
    print ("Honest, if you go to this group you have a very strong opinion about every thing. You become the jury in court.")
    sleep(1)
    print ("Dauntless")
    print ("Brave, if you go to this group you overcome your fear(s). You keep order in this town. That is what I am here. You will be the police.")
    sleep(1)
    print ("Erudite")
    print ("Intellectual, if you go to this group you can find important stuff and you can play with it. You are very smart and want to look for new possibilities.")
    vraagc()

#vraag wat bij jouw past
def vraagc():
    print ("What do you want to be in this world?")
    sleep(1)
    print ("a: Abnegation  b: Amity  c: Candor  d: Dauntless  e: Erudite")
    antc = input().lower()
    if antc ==("a"):
        sleep(2)
        print ("Good choice, we like others more than ourselves. We help the people, we help the world.")
        introab()
    elif antc ==("b"):
        sleep(2)
        print ("Good choice, we are friendly to people and animals. We will be helpful for everybody.")
        introam()
    elif antc ==("c"):
        sleep(2)
        print ("Good choice, everybody needs to be honest. In a society you have to speak the truth.")
        introca()
    elif antc ==("d"):
        sleep(2)
        print ("Good choice, we will see what you fear and you will overcome it. You are the hero here not the coward!")
        introda()
    elif antc ==("e"):
        sleep(2)
        print ("Good choice, lets find out where something comes from. Someone has to invent new stuf.")
        introer()
    else:
        print ("Not a option")
        sleep(3)
        vraagc()

#abnegation intro uitleg    
def introab():
    print ("There is a person on stage they say:")
    sleep(2)
    print ("Welcome folks, we are the group of Abonegation.We make sure that there is respect that allows us to live here. Our job is to arrange everything in this city, so we make decisions. We are a neutral group because we put others before ourselves.")
    print ("You need to come with us for your first decision. You walk with them.")
    keuzeabeinde()

#amity intro uitleg & einde
def introam():
    print ("You were send to the farmlands.")
    sleep(2)
    print ("The people here are kind and helpful.")
    print ("A couple years pass and you are still happy where you are.")
    sleep(2)
    print ("You are goning to die peacefully with lots of people that care about you when it is your time.")
    print ("For now you farm with the rest of the people that help you.")
    print (end)
    opnieuw()

#candor into uitleg
def introca():
    print ("So you always tell the truth?")
    sleep(2)
    print ("Then you belong to this group.")
    print ("Said a man on a podium.")
    sleep(1)
    print ("We are the jury/judges in this city.")
    print ("We bring justice to this city.")
    sleep(2)
    print ("You are about to make your first decision and make sure it is judged fairly, otherwise you will be kicked out of this group.")
    print ("Be aware because you are unable to pick a new faction.")
    carecht()

#Dauntless into uitleg
def introda():
    print ("We are like the police of this city.")
    sleep(1)
    print ("So act like it, no more mistakes, we need to keep people in check!")
    print ("Said the man on stage.")
    sleep(2)
    print ("You all are wall protectors for now! So move it!")
    sleep(3)
    print ("You walk to the wall and you see far in the desserd that there is a group of wild hunting animals is coming towards you.")
    keuzedawall()

#Erudite into uitleg
def introer():
    print ("Welcome to Erudite. You have the qualities of a researcher.")
    print ("In this city you are now a researcher.")
    sleep(2)
    print ("If you have a research question, make sure you answer it correctly.")
    edvraagonderzoek()

#rechtbank keuze
def carecht():
    print ("Your first assignment in this city.")
    sleep(1)
    print ("There are a group of people are they guilty?")
    print ("a: Yes (kill them)  b: No (let them go)")
    antcar = input().lower()
    if antcar ==("a"):
        print ("You made the right choice they were guilty.")
        sleep(2)
        print ("You live happily ever after.")
        print (end)
        opnieuw()
    elif antcar ==("b"):
        print ("You were wrong")
        sleep(1)
        print ("We have a too large population in this town and we don't want any liars here!")
        sleep(2)
        print ("You are condemned by your friends in Candor. You were convicted/ killed by your friends...")
        print (end)
        opnieuw()
    else:
        print ("Not a option")
        sleep(2)
        carecht()

#keuze ab met eindes
def keuzeabeinde():
    sleep(2)
    print ("You get to make your first choice about our government. Since you are part of it, you must make a decision for the city.")
    print ("a: give more space to your place of residence b: give more space to build a new lab for erudite")
    antab = input().lower()
    if antab ==("a"):
        print ("So you think more about yourself than the rest? That is not possible in this group.")
        sleep(1)
        print ("You will be dragged to court yourself... You were punished. Your punishment is death.")
        print (end)
        opnieuw()
    elif antab ==("b"):
        print ("You made the right choice and live happily ever after.")
        sleep(2)
        print (end)
        opnieuw()
    else:
        print ("Not a option")
        sleep(2)
        keuzeabeinde()

#keuze 1 da 
def keuzedawall():
    print ("You look around and find a few weapons.")
    sleep(1)
    print ("What do you get?")
    print ("a: sword  b: bow and arrow  c: bat  d: hide")
    antda1 = input().lower()
    if antda1 ==("c") or antda1 ==("a"):
        print ("Oh no, they come closer and you can't defend yourself anymore... They took your weapon. You run away.")
        sleep(2)
        print ("You fall and the animals are over you. They rip you apart.")
        sleep(2)
        print ("You are dead.")
        print (end)
        opnieuw()
    elif antda1 ==("b"):
        print ("You made it to a safer place but you are out of arrows!")
        sleep(2)
        vraagda2()
    elif antda1 == ("d"):
        print ("You found shelter but they can smell you.")
        sleep(2)
        print("They found you, you try to fight.")
        print ("You fall and the animals are over you. They rip you apart.")
        sleep(2)
        print ("You are dead.")
        print (end)
        opnieuw()
    else:
        print ("Not a option")
        sleep(2)
        keuzedawall()

#keuze 2 da
def vraagda2():
    print ("The animals are still comming! What do you do?")
    print ("a: get a other weapon  b: run away  c: walk away")
    antda2 = input().lower()
    if antda2 ==("a"):
        wapen2()
    elif antda2 ==("b"):
        print ("You run and run...")
        sleep(2)
        introoorlog()
    elif antda2 ==("c"):
        print ("The animals are faster and find you!")
        sleep(2)
        print ("They jump on you and you fall and the animals are over you. They rip you apart.")
        sleep(2)
        print ("You are dead.")
        print (end)
        opnieuw()
    else:
        print ("Not a option")
        sleep(2)
        vraagda2()

#wapen2 eind... da
def wapen2():
    print ("a: knive  b: a toilet seat  c: bat  d: sword")
    antda3 = input().lower()
    if antda3 ==("a") or antda3 ==("b") or antda3 ==("c") or antda3 ==("d"):
        sleep(1)
        print ("Oh no, they come closer and you can't defend yourself anymore... They took your weapon.")
        sleep(2)
        print ("You fall and the animals are over you. They rip you apart.")
        print ("You are dead.")
        sleep(2)
        print (end)
        opnieuw()
    else:
        print ("Not a option")
        sleep(2)
        wapen2()

#ed vraag onderzoek
def edvraagonderzoek():
    print ("How can dust form in the air?") 
    sleep(2)
    print ("a: it isn't always there. When it is there it forms a substance on the ground.")
    print ("b: it automatically forms a larger particle so that you can see it in the air.")
    anted = input().lower()
    if anted == ("a"):
        print ("Wrong!")
        sleep(1)
        print ("You will be dragged to court... You were punished your punishment is death.")
        sleep(2)
        print (end)
        opnieuw()
    elif anted == ("b"):
        print ("Good job you are a true researcher.")
        sleep(1)
        print ("You live happily ever after.")
        print (end)
        opnieuw()
    else: 
        print ("Not a option")
        sleep(2)
        edvraagonderzoek()

#opnieuw?
def opnieuw():
    sleep(2)
    print ("Do you want to play again?")
    print ("y/n")
    antopnieuw = input().lower()
    if antopnieuw ==("y"):
        print ("Oke here you go.")
        sleep(2)
        introoorlog()
    elif antopnieuw ==("n"):
        print ("Oke have a nice day/ night.") 
    else:
        print ("Not a option")
        sleep(2)
        opnieuw()

introoorlog()