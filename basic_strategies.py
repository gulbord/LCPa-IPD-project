from random import random

class Player:
    def __init__(self, k):
        self.k=k
    
    def play(self, hist):
        return random()<k
    
class TftPlayer(Player):
    def play(self, hist):
        return hist[-1]
    
    
# so for example we can have

nice_guy=Player(1)  #always cooperates
bad_guy=Player(0)   #never cooperates
avg_guy=Player(0.5) #cooperates half the time
mn_guy=Player(0.75) #mostly cooperates
mb_guy=Player(0.25) #rarely cooperates
tt_guy=TftPlayer(0) #reacts with last opponent move


# basic mechanics for 1-on-1 game

def game(pl1, pl2, it):
    hist1=[True] #only for the correct initialization of tt_guy
    hist2=[True] #same
    points=[0,0]
    
    for i in range(it): 
        hist1.append(pl1.play(hist2))
        hist2.append(pl2.play(hist1))
        if hist1[-1] and hist2[-1]:
            points[0]+=2
            points[1]+=2
        else if hist1[-1] and not hist2[-1]:
            points[1]+=3
        else if not hist1[-1] and hist2[-1]:
            points[1]+=3
        else if not hist1[-1] and not hist2[-1]:
            points[0]+=1
            points[1]+=1
    
    return points