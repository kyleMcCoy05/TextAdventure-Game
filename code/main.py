from config import *
from player import *
from support import *
from battle import *
from gui import maker, loader

player = Player()

def characterSelect() -> None:
    playerSave = loader()
    loadData(playerSave, player)
    player.setAttributes()
    player.setAttacks()
    player.playerSheet()

def characterMaker() -> None:
    maker(player)
    player.setAttributes()
    player.setAttacks()
    player.playerSheet()

def main() -> None:

    playing = titleScreen()

    if playing == True:
        newCharacter = input("Do you want to make a new character?(y/n): ").lower()
        if newCharacter == 'n':
            characterSelect()
        else:
            characterMaker()

    while playing:
        
        b = Battle(player)
        
        b.start()

        break

if __name__ == "__main__":
    main()