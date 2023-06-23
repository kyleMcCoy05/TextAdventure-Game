import os, time, random
from file import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

DATADIR = r'C:\Users\kyleo\Documents\Projects\Code\Text Game\data'

# Player config
maxStartStats = 25
maxLevel = 60
maxStat = 99
maxHP = 999
maxMana = 100

baseHealth = 15
baseMana = 5

classes = [
    'Fighter',
    'Wizard',
    'Rouge',
    'Ranger',
]

# for future class ideas
#     'Druid',
#     'Mage',
#     'Paladin',
#     'Monk',