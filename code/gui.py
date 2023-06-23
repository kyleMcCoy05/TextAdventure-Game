from config import *

# Basic starting tkinter startup
root = tk.Tk()
root.geometry("250x400")
root.withdraw()

# player data variables
name = tk.StringVar()
cls = tk.StringVar()
stats = []
stat = []

save = []

subtract = lambda: maxStartStats-1

# function to load player save location
def loader() -> str:
    master = tk.Tk()
    master.withdraw()
    playerSave = filedialog.askopenfilename(master = master, 
                                            filetypes=(('Dat Files', '*.dat'),
                                                       ('All Files', '*.*')), 
                                            title='Load Player Data', 
                                            initialdir=DATADIR)
    master.destroy()
    return playerSave

# funktion to make player
def maker(player: object):
    root.deiconify()
    global p
    
    p = player
    
    tk.Label(root, text='Name').grid(row=0)
    tk.Label(root, text='Class').grid(row=1)
    e1 = tk.Entry(root, textvariable=name)
    e2 = ttk.Combobox(root, values=classes, textvariable=cls, state = "readonly" )
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
    tk.Label(root).grid(row=2)

    for index, item in enumerate(player.stats):
        tk.Label(root, text=item).grid(row=(index+3))
        stats.append(tk.Spinbox(root,
                                increment=1, 
                                state='normal', 
                                from_=0, 
                                to=10))

    confirmButton = tk.Button(root, text='Confirm', command=setPlayer)
    confirmButton.grid(row=10, column=1)
    cancelButton = tk.Button(root, text='Cancel', command=cancel)
    cancelButton.grid(row=10, column=2)

    for e, i in enumerate(stats):
        i.grid(row=(e+3), column=1, pady = 5)

    root.mainloop()

# function to set player Nmae, class, and stats
def setPlayer():
    accepted = False
    check = 0
    while not accepted:

        # checks name
        try:
            n = name.get()
            if n == '':
                raise ValueError
        except ValueError:
            popupmsg("Name Not Accepted")
        else:
            n = name.get()
            p.id['name'] = n
            save.append(n)
            check += 1

        # cheaks if class is correct
        try:
            c = cls.get()
            if c == '':
                raise ValueError
            if c not in classes:
                raise ValueError
        except ValueError:
            popupmsg("Class Not Accepted")
        else:
            c = cls.get()
            p.id['class'] = c
            save.append(c)
            check += 1

        # clears stat list
        del stat[:]
        # iterates throw stats list
        for i in stats:
            # gets value of that isteration of stats
            _ = i.get()
            if int(_) > 10:
                popupmsg(" Invaled Input \n max stat is '10'")
            # if iteration is not empty
            if _ != '':
                # adds it to the stat liberary
                stat.append(_)
                save.append(_)
            # else stat is 0
            else:
                stat.append(0)
                save.append(0)  

        for index, item in enumerate(p.stats):
            p.stats[item] = stat[index]

        # if both name and class has been checked ends loop
        if check == 2:
            accepted = True

    # runs save player function
    saveData(save, save[0])
    
    # destroys root
    root.destroy()

# function to delete root
def cancel() -> None:
    root.destroy()

# function to display a popup message
def popupmsg(msg: str = 'invaled input') -> None:
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

if __name__ == '__main__':
    from player import *
    p = Player()
    maker(p)