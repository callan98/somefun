#event loading
from random import randint
def nameget(x):
    danger=x*randint(1,3)
    name=0
    if x==1:
        name="wizard"
    elif x==2:
        name="donkey"
    elif x==3:
        name="trader"
    elif x==4:
        name="knight"
    elif x==5:
        name="elf"
    elif x==6:
        name="alien"
    elif x==7:
        name="lizard"
    elif x==8:
        name="skeleton"
    elif x==9:
        name="wolf"
    elif x==10:
        name= "bounty hunter"
    elif x==11:
        name= "sorcerer"
    elif x==12:
        name="dragon"
    else:
        return 0
    return name


def eventset(x):
    eventypenum=randint(1,3)
    eventsetup=0
    if eventypenum==1:
       eventsetup= print("you come across a friendly",x)
    elif eventypenum==2:
        eventsetup=print("you see a",x,"in the distance")
    elif eventypenum==3:
        eventsetup=print("a wiley", x, "jumps towards you")


def dangerlevel(x):
    danger=0
    if x=="wizard":
        danger=1
    elif x=="donkey":
        danger=2
    elif x=="trader":
        danger=3
    elif x=="knight":
        danger=4
    elif x=="elf":
        danger=5
    elif x=="alien":
        danger=6
    elif x=="lizard":
        danger=7
    elif x=="skeleton":
        danger=8
    elif x=="wolf":
        danger=9
    elif x=="bounty hunter":
        danger=10
    elif x=="sorcerer":
        danger=11
    elif x=="dragon":
        danger=12
    danger=danger*randint(1,5)
    return danger

def choice (danger,x):
    if danger<=10:
        print("the", x, "is friendly")
        print("you can")
        print("1. fight")
        print("2. trade")
        print("3. move on")
        choice=input("what do you want to do?")
        if choice not in ("1","2","3"):
            print("that wasnt an option, you run away instead")
            choice=3
    elif danger>=11 and danger<=20:
        print("the",x,"says hello")
        print("you can")
        print("1. fight")
        print("2. trade")
        print("3. move on")
        choice=input("what do you want to do?")
        if choice not in ("1","2","3"):
            print("that wasnt an option, you run away instead")
            choice=3
    elif danger>=21 and danger<=30:
        print("the",x,"doesnt notice you")
        print("you can")
        print("1. fight")
        print("2. trade")
        print("3. move on")
        choice=input("what do you want to do?")
        if choice not in ("1","2","3"):
            print("that wasnt an option, you run away instead")
            choice=3
    elif danger>=31 and danger<=40:
        print("the",x,"stares at you")
        print("you can")
        print("1. fight")
        print("3. move on")
        choice=input("what do you want to do?")
        if choice=="2":
           print("you cannot trade now")
           print("you run away instead")
           choice="3"
        if choice not in ("1","2","3"):
            print("that wasnt an option, you run away instead")
            choice=3
    elif danger>=41 and danger<=50:
        print("the",x,"walks towards you")
        print("you can")
        print("1. fight")
        print("3. run away")
        choice=input("what do you want to do?")
        if choice==2:
           print("you cannot trade now")
           print("you run away instead")
           choice=3
        if choice not in ("1","2","3"):
            print("that wasnt an option, you run away instead")
            choice=3
    elif danger>=51 and danger<=60:
        print("the",x,"charges")
        print("get ready to fight")
        choice=3
    
    return choice

def movingrepository1():
    x=randint(1,10)
    if x==1:
        name="long dusky road"
    elif x==2:
        name="dark forrest"
    elif x==3:
        name="craggy mountain pass"
    elif x==4:
        name="mysterious plateau"
    elif x==5:
        name="strange house"
    elif x==6:
        name="dark cave"
    elif x==7:
        name="swamp"
    elif x==8:
        name="abandoned farm"
    elif x==9:
        name="abandoned fair"
    elif x==10:
        name="scrapyard"
    return name

def movingrepository2():
    x=randint(1,10)
    if x==1:
        name="fairy plains"
    elif x==2:
        name="cosy cottage"
    elif x==3:
        name="rolling fields"
    elif x==4:
        name="daisy meadows"
    elif x==5:
        name="blinding light"
    elif x==6:
        name="quaint village"
    elif x==7:
        name="beach"
    elif x==8:
        name="patrolled forrest"
    elif x==9:
        name="lively fairgrounds"
    elif x==10:
        name="babbling brook"
    return name
    
def movingrepository3():
    x=randint(1,10)
    if x==1:
        name="roman road"
    elif x==2:
        name="old forrest"
    elif x==3:
        name="hilly trail"
    elif x==4:
        name="rocky plateau"
    elif x==5:
        name="old house"
    elif x==6:
        name="snow covered fields"
    elif x==7:
        name="swamp village"
    elif x==8:
        name="farm"
    elif x==9:
        name="dodgy fair"
    elif x==10:
        name="dim alley"
    return name

def movingrepository4():
    x=randint(1,10)
    if x==1:
        name="raiders camp"
    elif x==2:
        name="old fort"
    elif x==3:
        name="pirate ship"
    elif x==4:
        name="thunderous mountains"
    elif x==5:
        name="banit hideout"
    elif x==6:
        name="lions den"
    elif x==7:
        name="underground lair"
    elif x==8:
        name="military camp"
    elif x==9:
        name="sharp rocks"
    elif x==10:
        name="no mans land"
    return name
