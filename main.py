import random
from random import randint

def rollstat(min_num , max_num, rollamount):
    numbers = []
    for i in range(rollamount):
        numbers.append(random.randint(min_num, max_num))
    numbers.remove(min(numbers))
    return sum(numbers)

class NPC:
    def __init__(self, nom, race, espece, profession):
        self.Force = rollstat(1,6,4)
        self.Agility = rollstat(1,6,4)
        self.Constitution = rollstat(1,6,4)
        self.Intelligence = rollstat(1,6,4)
        self.Sagesse = rollstat(1,6,4)
        self.Charisme = rollstat(1,6,4)

        self.ClasseArmure = random.randint(1,12)
        self.Nom = nom
        self.Race = race
        self.Espece = espece
        self.PointDeVie = random.randint(1,20)
        self.Profession = profession

    def afficher_characteristiques(self):
        print(vars(self))

class Kobold(NPC):
    def attaque(self, cible):
        print("Vous attaquer:", cible.Nom)
        cible.subir_dommage(random.randint(1,6))

    def subir_dommage(self, dmg):
        self.PointDeVie -= dmg

class Hero(NPC):
    def attaque(self, cible):
        print("Vous attaquer:", cible.Nom)
        cible.subir_dommage(random.randint(1,6))

    def subir_dommage(self, dmg):
        self.PointDeVie -= dmg

Koblito = Kobold("Joe", "Kobold", "Idk", "Attaquant")
Joe = Hero("Billy", "Humain", "Idk", "Defenseur")
Joe.afficher_characteristiques()
Koblito.attaque(Joe)
Joe.afficher_characteristiques()

