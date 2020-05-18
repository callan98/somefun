#callan littlejohn
#basic tezt adventure
#16/05/2020

from random import randint
import eventloading
import battlemechanics


hp=100
def setdifficulty():
    print("welcome to this simple text adventur")
    print("please choosea difficulty")
    print("1. easy")
    print("2. normal")
    print("3.difficult")
    difficulty=input()
    if difficulty not in ("1","2","3"):
        print("this is not a valid difficulty")
    if difficulty=="1":
        difficulty=1
    if difficulty=="2":
        difficulty=2
    if difficulty=="3":
        difficulty=3
    
    return difficulty
 
def weaponselect():
    print("as a child you were abandoned, begging and stealing got you a long way,")
    print("but also got you in a lot of trouble")
    print("trying to escape the law you run to the woods")
    print("you happen across a dead merchant")
    print("it looks like he was attacked by a wild beast,")
    print("a weapon still hangs from his side, you lean down to grab it")
    print("from your thieving days you remember that merchants only carry three types of weapons")
    print("1. sword")
    print("2. axe")
    print("3. handcannon")
    print("what weapon does this merchant have?")
    weapon=input("please note for all options please only type the number")
    if weapon not in ("1","2","3"):
        print("this is not a valid weapon")
    if weapon=="1":
        weapon=1
    if weapon=="2":
        weapon=2
    if weapon=="3":
        weapon=3
    
    return weapon
    
def movement2 ():
    ran1=randint(1,4)
    tillevent=ran1
    while tillevent>=1:
        one= eventloading.movingrepository1()
        two= eventloading.movingrepository2()
        three= eventloading.movingrepository3()
        four= eventloading.movingrepository4()
        print("four paths lay ahead")
        print("1.",one)
        print("2.",two)
        print("3.",three)
        print("4.",four)
        choice= input("choose a path")
        tillevent=tillevent-1
    if tillevent==0:
        danger=movement(choice)
    return danger

def choicemechanic(choice,x):
    if choice=="1":
        print("you choose to fight the",x)
        battle=battlemechanics.fightstart(name,hp,difficulty, weapon, dangerlevel)
    if choice=="2":
        print("you attempt to trade with the",x)
    if choice=="3":
        print("you try to run away")
        ran1=randint(1,10)
        chance=difficulty*ran1
        if chance<=20:
            print("got away safe")
        else:
            print("no chance to run, time to fight")
            battle=battlemechanics.fightstart(name,hp,difficulty, weapon, dangerlevel)         


def movement(path):
    
    if firstpath=="1":
        danger=3
    elif firstpath=="2":
        danger=1

    elif firstpath=="3":
        danger=2

    elif firstpath=="4":
        danger=5
    return danger

difficulty=setdifficulty()
    
    

print("hi adventurer,what is your name?")
player= input("enter name")
print("hello", player)
weapon=weaponselect()

print("three roads appear before you, which will you choose")
print("1, the dark and dusty road")
print("2, the yellow brick road")
print("3, A dark cave")
print("4, fuck the roads")

firstpath= input("choose path,1,2,3,4")

danger=movement(firstpath)

name=eventloading.nameget(danger)


eventsetup=eventloading.eventset(name)

dangerlevel=eventloading.dangerlevel(name)

choice= eventloading.choice(dangerlevel,name)

action=choicemechanic(choice,name)

while hp>=1:
    danger=movement2()
    name=eventloading.nameget(danger)
    eventsetup=eventloading.eventset(name)
    dangerlevel=eventloading.dangerlevel(name)
    choice= eventloading.choice(dangerlevel,name)
    action=choicemechanic(choice,name)
    


