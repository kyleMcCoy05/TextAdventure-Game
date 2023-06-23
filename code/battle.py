from config import *
from enemy import *

class Battle:

    def __init__(self, player) -> None:
        
        self.p = player

    def start(self) -> None:

        e = Enemy(random.choice(classes))
        e.setAttributes()
        

        