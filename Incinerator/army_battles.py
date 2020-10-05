#!/usr/bin/env checkio --domain=py run army-battles

# 
# END_DESC

# Taken from mission The Warriors

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

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, job, amount):
        self.units.extend([job() for i in range(amount)])

class Battle:
    def fight(self, army_1, army_2):
        if fight(army_1.units[0], army_2.units[0]):
            del army_2.units[0]
            if not army_2.units:
                return True
            else:
                return self.fight(army_1, army_2)
        else:
            del army_1.units[0]
            if not army_1.units:
                return False
            else:
                return self.fight(army_1, army_2)

def fight(unit_1, unit_2):
    r = 1
    while unit_2.is_alive:
        if unit_1.is_alive and r % 2 == 0: #it's time for unit_2 to attack
            unit_1.health -= unit_2.attack
            unit_1.check_life()
        elif unit_1.is_alive and r % 2 == 1:
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

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
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

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")