from config import *
from player import *
from support import *
from gui import maker, loader

player = Player()

def characterSelect() -> None:
    playerSave = loader()
    loadData(playerSave, player)
    player.setAttributes()
    player.playerSheet()

def characterMaker() -> None:
    maker(player)
    player.setAttributes()
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
        
        break

if __name__ == "__main__":
    main()