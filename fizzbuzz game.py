# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:17:49 2020

@author: callan
"""



first=3
second=5
score=1
player=1
truth=0

while player==1:
    if score%2==0:
        score2=input()
        if (score)%first==0 and (score)%second==0:
            truth="fizbuzz"
        elif (score)%first==0:
            truth="fizz"
        elif (score)%second==0:
            truth="buzz"
        else:
            truth=str(score)
        if score2!=truth:
            print("not quite.")
            print("your score was", score)
            player=0
        else:
            score=score+1
    else:
        if (score)%first==0 and (score)%second==0:
            print("fizbuzz")
        elif (score)%first==0:
            print("fizz")
        elif (score)%second==0:
            print("buzz")
        else:
            print(score)
        score=score+1