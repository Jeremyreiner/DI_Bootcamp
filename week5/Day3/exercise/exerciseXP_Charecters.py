# Description
# Create a class called Character with the following attributes and methods:
# name
# life – starts with a default value of 20
# attack – the base attack of a character (integer) will be a default of 10
# basic_attack() - accepts another character as a parameter 
# and will <attack> the character and the characters <life> points should drop.
# ---------------------------------------------------------------------------------

class Character():
    def __init__(self, name, life = 200, attack = 10):
        self.name = name
        self.life = life
        self.attack = attack
    
    def basic_attack(self, other):
        print(f"{self.name.title()} is Attacking {other.name.title()}")

class Druid(Character):

    def meditate(self):
        life_bonus = 10
        attack_points = 2
        self.life += life_bonus
        self.attack -= attack_points
        print(f"{self.name} is meditating. {self.name}'s life power has increased by {life_bonus}.")
        print(f"{self.name}'s attack has fallen by {attack_points}.")
        print(f"{self.name}'s life points is now: {self.life}, and attack power is: {self.attack}.")
        return  self. life and self.attack
    
    def animal_help(self):
        attack_power = 5
        self.attack += attack_power
        print(f"{self.name} is using animal assistance!!")
        print(f"{self.name} has increased his attack power by {attack_power}!")
        print(f"{self.name} now has an attack power of {self.attack}!")
        return self.attack

    def fight(self, other):
        damage_dealt = other.life - ((.75 * other.life) - (.75 * self.attack))
        other.life -= damage_dealt
        print(f"{self.name} is fighting {other.name}!")
        print(f"{self.name} has dealt {damage_dealt} damage to {other.name}!")
        print(f"{other.name} now has a total health of {other.life}.")
        return  other.life


class Warrier(Character):
    def brawl(self, other):
        damage_dealt = (.25*other.life) 
        health_gained = (.5 * self.attack) 
        other.life -= damage_dealt
        self.life += health_gained
        print(f"{other.name}'s been dealt {damage_dealt} damage. {other.name}'s health is now: {other.life}.")
        print(f"{self.name} did {damage_dealt} to {other.name}. {self.name} health has increased to: {self.life}.")
        return other.life and self.life

    def train(self):
        self.attack += 2
        self.life  += 2
        return self.attack and self.life

    def roar(self, other):
        damage_dealt = other.attack - 3
        other.attack = damage_dealt
        print(f"{self.name} used Roar on {other.name}!")
        print(f"{other.name}'s attack power has fallen. {other.name}'s attack power is now {other.attack}.")
        return other.attack



class Mage(Character):
    def curse(self, other):
        damage_dealt = other.attack - 2
        other.attack -= damage_dealt
        print(f"{self.name} used Curse on {other.name}!")
        print(f"{other.name}'s attack has decreased by {damage_dealt}!")
        print(f"{other.name}'s attack is now {other.attack}.")
        return other.attack

    def summon(self):
        self.attack += 3
        print(f"{self.name}'s attack has increased by 3, {self.name} overall attack is now {self.attack}.")
        return self.attack

    def cast_spell(self, other):
        damage_dealt = (other.attack / other.life)
        other.life -= damage_dealt
        print(f"{self.name} has casted a spell on {other.name}.")
        print(f"{other.name}'s health has decreased by {damage_dealt}.")
        print(f"{other.name}'s overall health is now {other.life}.")
        return other.life and damage_dealt
w = Warrier("gerki")
m = Mage("james")
d = Druid("Stasia")

m.curse(d)
m.summon()
m.cast_spell(w)

d.meditate()
d.animal_help()
d.fight(m)

w.train()
w.brawl(m)
w.roar(d)

