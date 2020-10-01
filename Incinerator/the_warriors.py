#!/usr/bin/env checkio --domain=py run the-warriors

# 
# END_DESC

#NOTE: Python에서의 Class: https://wikidocs.net/28

class Warrior:
    def __init__(self):    
        self.health = 50
        self.attack = 5
        self.is_alive = True
    
    def check_life(self):
        self.is_alive = self.health > 0

class Knight(Warrior):
    def __init__(self):    
        self.health = 50
        self.attack = 7
        self.is_alive = True

def fight(unit_1, unit_2):
    r = 1
    while unit_2.is_alive:
        if unit_1.is_alive and r % 2 == 0: #it's time for unit_2 to attack
            unit_1.health -= unit_2.attack
            unit_1.check_life()
        elif r % 2 == 1:
            unit_2.health -= unit_1.attack
            unit_2.check_life()
        else:
            return False
        r += 1
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")