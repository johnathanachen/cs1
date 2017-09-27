import sys

if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk
root = tk.Tk()
root.title("Roulette")
tk.Label(root, text='Welcome to Roulette!', bd="20", width="75").pack()
tk.Label(root, text='How much would you like to bet?').pack()

def create_betData():
    betEntry = tk.Entry(root, text='placeholder').get()
    betEntry.pack()
    betButton = tk.Button(root, text="Place Bet")
    betButton.pack()

create_betData()

# tk.Button(root, text="Black").pack()
# tk.Button(root, text="Red").pack()
# tk.Button(root, text="Even").pack()
# tk.Button(root, text="Odd").pack()

# def placeBet():
#     betLabel.text =  betEntry.text




tk.mainloop()

