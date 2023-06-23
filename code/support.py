from config import *

def title() -> None:
    print("                                                      _")
    print("                        ___                          (_)")
    print("                      _/XXX\\")
    print("       _             /XXXXXX\_                                    __")
    print("       X\__    __   /X XXXX XX\                          _       /XX\__      ___")
    print("           \__/  \_/__       \ \                       _/X\__   /XX XXX\____/XXX\\")
    print("         \  ___   \/  \_      \ \               __   _/      \_/  _/  -   __  -  \__/")
    print("       ___/   \__/   \ \__     \\__           /  \_//  _ _ \  \     __  /  \____//")
    print("      /  __    \  /     \ \_   _//_\___     _/    //           \___/  \/     __/")
    print("      __/_______\________\__\_/________\_ _/_____/_____________/_______\____/_______")
    print("                                       /|\\")
    print("                                      / | \\")
    print("                                     /  |  \\")
    print("                                    /   |   \\")
    print("                                   /    |    \\")
    print("                                  /     |     \\")
    print("                                 /      |      \\")
    print("                                /       |       \\")
    print("                               /        |        \\")
    print("                              /         |         \\")

def titleScreen() -> None:
    os.system('cls')
    title()

    start = input("press 'Enter' to continue\nEnter 'q' to Quit")
    
    if start == "":
        os.system('cls')
        return True
    
    os.system('cls')
    return False
        
