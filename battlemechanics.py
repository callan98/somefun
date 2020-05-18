#fight mechanics
from random import randint
def attack(weapon,difficulty):
    speed=0
    attack=0
    if weapon==1:
        speed=3
        attack=1
    elif weapon==2:
        speed=2
        attack=2
    elif weapon==3:
        speed=1
        attack=3
    else:
        print("you do not have a validwepon type")
    print("choose your attack")
    print("1.stab")
    print("2.slash")
    print("3.flourish")
    choice=input()
    if choice=="1":
        choice=1
    elif choice=="2":
        choice=2
    elif choice=="3":
        choice=3
    else:
        print("this is not a valid move, you pass")
        choice=4
    
    if choice==1:
        speed=speed+3
        attack=attack+1
    elif choice==2:
        speed=speed+2
        attack=attack+2
    elif choice==3:
        speed=speed+1
        attack=attack+3
    else:
        speed=0
        attack=0
    ran1=randint(1,3)
    chance=speed*ran1
    if difficulty==1:
        if chance>=5:
            hit=attack
        else:
            hit=0
    if difficulty==2:
        if chance>=7:
            hit=attack
        else:
            hit=0
    if difficulty==3:
        if chance>=9:
            hit=attack
        else:
            hit=0
    return hit
        
def opponentsturn(difficulty,danger):
    hit=0
    modifier=difficulty*danger
    if modifier%4 == 0:
        hit= modifier/4
    elif modifier%3==0:
        hit= modifier/3
    elif modifier%5==0:
        hit= modifier/5
    else:
        hit=5
    return hit
    
def fightstart(x,hp,difficulty,weapon,danger):
    hp2=danger*difficulty
    print("the", x, "faces you")
    while hp2>0 and hp> 0:
        hit=attack(weapon,difficulty)
        print("your attack does", hit, "damage")
        hp2=hp2-hit
        print("opponents hp is" ,hp2)
        hit2=opponentsturn(difficulty, danger)
        hp=hp-hit2
        print(x,"hits you for", hit2)
        print("your hp is", hp)
    if hp<=0:
        print("you have fallen to", x)
        print("please restart the game and try again")
    elif hp2<=0:
        print("you have defeated",x)

        
        
    
    
    
    
