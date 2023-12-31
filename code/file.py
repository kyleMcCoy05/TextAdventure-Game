from config import *
import pickle

def saveData(data, name: str = 'player.dat') -> None:

    if name.endswith('.dat'):
        name = name.removesuffix('.dat')
    
    name = f'data/{name}.dat'

    with open(name, 'wb') as f:
        pickle.dump(data, f)

def loadData(name: str, player) -> str:
    global p
    p = player
    try:
        with open(name, 'rb') as i:
            data = pickle.load(i)

            p.stats = {
                "STR" : int(data[2]),
                "DEX" : int(data[3]),
                "CON" : int(data[4]),
                "WIS" : int(data[5]),
                "INT" : int(data[6]),
                "CHA" : int(data[7]),
            }

            p.id = {
                "name" : str(data[0]),
                "class" : str(data[1]),
            }

    except Exception as e:
        error = f'{e} \n\n {LookupError}'
        return error
    
def getAttacks(cls) -> list:
    
    match cls:
        case 'Wizard':
            path = r'C:\Users\kyleo\OneDrive\Desktop\Game making\TextAdventure-Game-main\data\attacks\wizard.txt'
        case 'Fighter':
            path = r'C:\Users\kyleo\OneDrive\Desktop\Game making\TextAdventure-Game-main\data\attacks\fighter.txt'
        case 'Rouge':
            path = r'C:\Users\kyleo\OneDrive\Desktop\Game making\TextAdventure-Game-main\data\attacks\rouge.txt'
        case 'Ranger':
            path = r'C:\Users\kyleo\OneDrive\Desktop\Game making\TextAdventure-Game-main\data\attacks\ranger.txt'
    
    with open(path, 'r') as f:
        attacks = f.read()
        return attacks
