from typing import Any
from config import *

class Enemy:

    def __init__(self, cls: str) -> None:
        
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

        self.cls = cls

        self.attributes = {
            "Health" : 0,
			"Mana" : 0,
			"Level" : 1,
        }

        self.attacks = {
            
        }
    
    def setStats(self) -> None:
        pass
    
    def setHealth(self) -> None:
        self.maxHealth = int((baseHealth + (maxHP - baseHealth) * self.attributes['Level'] / maxLevel) + (0.5**int(self.stats['CON'])))
        self.attributes['Health'] = self.maxHealth

    def setMana(self) -> None:
        self.maxMana = int((baseHealth + (maxMana - baseHealth) * self.attributes['Level'] / maxLevel) + (0.5**int(self.stats['INT'] // 0.5**int(self.stats['WIS']))))
        self.attributes['Mana'] = self.maxMana

    def setAttributes(self) -> None:
        self.setHealth()
        self.setMana()

    def setAttacks(self):
        attacks = []
        attacksRaw = getAttacks(self.cls).split('\n')
        for i in range(len(attacksRaw)):
            attack = attacksRaw[i].split(',')
            attacks.append((attack[0], attack[1]))
        for i in attacks:
            self.attacks.setdefault(i[0],i[1])