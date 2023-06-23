import os, time
from file import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

DATADIR = r'C:\Users\kyleo\Documents\Projects\Code\idea\data'

# Player config
maxLevel = 60
maxStat = 99
maxHP = 999

baseHealth = 15
baseMana = 5

classes = [
    'Monk',
    'Fighter',
    'Wizard',
    'Rouge',
    'Druid',
    'Mage',
    'Paladin',
    'Ranger',
]