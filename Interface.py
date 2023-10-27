import random
import sys
import tkinter as tk
from PIL import Image, ImageTk
from Mechanics import set_item_texture

# inintialising main window
main_color = '#BFA173'
window = tk.Tk()
window.title("Digging treasures")
window.geometry("1800x900+10+20")
window.configure(bg=main_color)

lbl = tk.Label(window, text="Digging treasures", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color)
lbl.pack()
version = tk.Label(window, text="v0.8", fg='black', font=("Helvetica", 9), anchor="e", bg=main_color)
version.pack()

backgroundimg = Image.open("Resources/Background_2.jpg")
backgroundimg = backgroundimg.resize((1810, 900))
backgroundimg = ImageTk.PhotoImage(backgroundimg)
bcg = tk.Label(window, image=backgroundimg)
bcg.place(x=-5, y=60)

# creating interface with players
players_interface = tk.Frame(window, width=200, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color)
players_interface.place(x=100, y=100)

game_map = tk.Canvas(window, width=850, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color,
                         highlightbackground="black")

celebration_map = tk.Canvas(window, width=600, height=600, relief=tk.GROOVE, borderwidth=5, bg=main_color,
                            highlightbackground="black")
# creating trading interface
trade_interface = tk.Canvas(window, width=300, height=200, relief=tk.GROOVE, borderwidth=5, bg=main_color,
                     highlightbackground="black")
trade_interface.place(x=100, y=600)
label_trade = tk.Label(trade_interface, text="Trading", fg='black', font=("Helvetica", 16), anchor="n", bg=main_color)
label_trade.place(x=110, y=10)

# creating window with items and mechanics description
item_descriptions = [[0, "Trader: add 1 trade, or double\rthe efficiency of next trade"], [0, "Tinker: You can use 1 trade to\rexchange 1 pickaxe for lockpick"],
                     ["Bomb.png", "Bomb: Open 1 adjacent tile\rimmidiately, even rock"], ["CursedKey.png", "Cursed key: Gain 1 key. Lose 5 gold,\rgain 2 Curse"],
                     ["Smugglers.png", "Smugglers: Steal 1 pickaxe \ror open 1 nearest rock"], ["Key2.png", "Lockpick: Get 1 key,but give\r10 gold or 1 pickaxe to opponent"],
                     ["Treasure.png", "Treasury: Gain 5 gold\r "], ["MagicStone.png", "Wish Stone: you can exchange 10 gold for 1 key,\ropen any 1 tile, or add 2 trades"],
                     ["Megabomb.png", "Megabomb: Open 3 adjanced tiles,\ror 1 closest tile if no tiles nearby"], ["supplies.png", "Supplies: Gain 2 pickaxes\r "],
                     ["MagicMirror.png", "Crystal mirror: Skip 2 turns, but gain\rmagic mirror until your turn"], ["WickedStone.png", "Wicked Stone: steal 10 gold,\r1 pickaxe or inflict 2 curse on opponent"],
                     ["Scaner.png", "Scaner: See amount of keys on surrounding tiles"]]

effect_descriptions = ["Gold rush: Open up to 4 dirt tiles\r for 3 gold each", "Magic Mirror: you receive copy of any item your obtained by opponent",
                       "Curse: opponent recieve items you find instead of you", "Sale: next trade effect is doubled", ]

canvas_description = tk.Canvas(window, width=400, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color, highlightbackground="black")
canvas_description.place(x=1300, y=100)
canvas_description.pack_propagate(False)

item_description_label = tk.Label(canvas_description, text="Item and trait descriptions:", fg='black', font=("Helvetica", 18), anchor="w", bg=main_color)
item_description_label.pack(pady=8)
position = 0
icons = []
for item in item_descriptions:
    if item[0] != 0:
        icon = set_item_texture(item[0], (50, 50))
        icons.append(icon)
        canvas_description.create_image(30, 68 + position, image=icon)
    canvas_description.create_text(55, 68 + position, text=item[1], font=("Helvetica", 10), width=450, anchor="w")
    position += 49

def next_page():
    canvas_description.forget()
    canvas_description_2.place(x=1300, y=100)
    canvas_description_2.create_window(35, 30, window=button_back)
def prev_page():
    canvas_description_2.forget()
    canvas_description.place(x=1300, y=100)
    canvas_description.create_window(385, 30, window=button_next)


button_next = tk.Button(canvas_description, text="►", bg=main_color, command=next_page, height=1, width=2, font=("Helvetica", 10))
canvas_description.create_window(385, 30, window=button_next)

canvas_description_2 = tk.Canvas(window, width=400, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color, highlightbackground="black")
canvas_description_2.pack_propagate(False)
button_back = tk.Button(canvas_description_2, text="◄", bg=main_color, command=prev_page, height=1, width=2, font=("Helvetica", 10))


# dice roll interface, replaces perk description window after start of stage 2
canvas_roll = tk.Canvas(window, width=400, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color, highlightbackground="black")
dice_roll = tk.Label(canvas_roll, text="  ", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color,
                     borderwidth=2, relief="groove")
btn_image = set_item_texture("Octahedron.png", (100, 100))
btn_dice = tk.Button(canvas_roll, image=btn_image, bg=main_color,
                     command=lambda: dice_roll.configure(text=random.choice(range(1, 9))), height=100, width=100,
                     font=("Helvetica", 10))
wind_rose_image = set_item_texture("078wxn75.png", (150, 150))