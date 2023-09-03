from config import *
from enemy import *

class Battle:

    def __init__(self, player) -> None:
        
        self.p = player

    def start(self) -> None:

        print('Start')

        e = Enemy(random.choice(classes))
        e.setAttributes()
        
        print("Enemy created")

        fight = True

        while fight:

            pass