#  Read the README

# from config import *
from player import *
from support import *
from battle import *

player = Player()

def main() -> None:

    playing = titleScreen()
    loading = playing

    while loading == True:
        if playing == True:
            newCharacter = input("Do you want to make a new character?(y/n): ").lower()
            if newCharacter == 'n':
                load = player.select()
                if load != None:
                    loading = False
                    break
            else:
                load = player.make()
                if load != None:
                    loading = False
                    break
                

    while playing:
        
        b = Battle(player)
        
        b.start()

        break

if __name__ == "__main__":
    main()