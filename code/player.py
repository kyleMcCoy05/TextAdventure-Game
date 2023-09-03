from config import *
from file import getAttacks
from gui import maker, loader

class Player:

    def __init__(self) -> None:

        self.maxHealth = 0
        self.maxMana = 0

        self.stats = {
            "STR" : 0,
            "DEX" : 0,
            "CON" : 0,
            "WIS" : 0,
            "INT" : 0,
            "CHA" : 0,
        }

        self.id = {
            "name" : '',
            "class" : '',
        }

        self.attributes = {
            "Health" : 0,
			"Mana" : 0,
			"Level" : 1,
			"EXP" : 0,
			"maxEXP" : 50,
        }

        self.attacks = {

        }

    def playerSheet(self) -> None:

        os.system('cls')

        for i in self.id:
            print(f'{i}: {self.id[i]}')

        print()

        for i in self.attributes:
            if i != 'maxEXP':
                if i == 'EXP':
                    print(f"{i}: {self.attributes[i]} / {self.attributes['maxEXP']}")
                elif i == 'Health':
                    print(f"{i}: {self.attributes[i]} / {self.maxHealth}")
                else:
                    print(f"{i}: {self.attributes[i]}")

        print()

        for i in self.stats:
            print(f'{i}: {self.stats[i]}')
        
        input()

    def setHealth(self) -> None:
        self.maxHealth = int((baseHealth + (maxHP - baseHealth) * self.attributes['Level'] / maxLevel) + (0.5**int(self.stats['CON'])))
        self.attributes['Health'] = self.maxHealth

    def setMana(self) -> None:
        self.maxMana = int((baseHealth + (maxMana - baseHealth) * self.attributes['Level'] / maxLevel) + (0.5**int(self.stats['INT']) // 0.5**int(self.stats['WIS'])))
        self.attributes['Mana'] = self.maxMana

    def setAttributes(self) -> None:
        self.setHealth()
        self.setMana()

    def setAttacks(self):

        attacks = []
        attacksRaw = getAttacks(self.id['class']).split('\n')
        for i in range(len(attacksRaw)):
            attack = attacksRaw[i].split(',')
            attacks.append((attack[0], attack[1]))
        for i in attacks:
            self.attacks.setdefault(i[0],i[1])

    def make(self):
        p = maker(self)
        if p == None:
            return None
        self.setAttributes()
        self.setAttacks()
        self.playerSheet()
        return True
    
    def select(self):
        playerSave = loader()
        if playerSave == None:
            return None
        loadData(playerSave, self)
        self.setAttributes()
        self.setAttacks()
        self.playerSheet()
        return True
    