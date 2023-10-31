import random
import tkinter as tk

from Mechanics import read_config, set_item_texture


# inintialising main window
main_color = '#BFA173'
window = tk.Tk()
window.title("Digging treasures")
window.geometry("1800x900+10+20")
window.configure(bg=main_color)
window.iconbitmap("Resources/icon.ico")

title = tk.Label(window, text="Digging treasures", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color)
title.pack()
version = tk.Label(window, text="v1.0", fg='black', font=("Helvetica", 9), anchor="e", bg=main_color)
version.pack()

backgroundimg = set_item_texture("Background_2.jpg", (1810, 900))
bcg = tk.Label(window, image=backgroundimg)
bcg.place(x=-5, y=60)

# creating interface with players
players_interface = tk.Frame(window, width=200, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color)
players_interface.place(x=100, y=100)

# main tables of a game, stage 1 and 2
game_map = tk.Canvas(window, width=850, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color,
                     highlightbackground="black")
celebration_map = tk.Canvas(window, width=600, height=600, relief=tk.GROOVE, borderwidth=5, bg=main_color,
                            highlightbackground="black")

# creating trading interface
canvas_trade = tk.Canvas(window, width=300, height=200, relief=tk.GROOVE, borderwidth=5, bg=main_color,
                         highlightbackground="black")
canvas_trade.place(x=100, y=600)
label_trade = tk.Label(canvas_trade, text="Trading", fg='black', font=("Helvetica", 16), anchor="n", bg=main_color)
label_trade.place(x=110, y=10)
image_pickaxe = set_item_texture("pickaxe.png", (35, 35))
image_coins = set_item_texture("Coins.png", (35, 35))
canvas_trade.create_image(60, 60, image=image_coins)
canvas_trade.create_image(120, 60, image=image_pickaxe)
canvas_trade.create_image(95, 90, image=image_coins)
canvas_trade.create_image(155, 90, image=image_pickaxe)
canvas_trade.create_image(230, 90, image=image_coins)
canvas_trade.create_image(290, 90, image=image_pickaxe)
canvas_trade.create_text(20, 60, text="10         > 1          ", font=("Helvetica", 12), width=400, anchor="w", activefill="#313d52")
canvas_trade.create_text(20, 90, text="Sale: 5         > 1     or 10        > 2     ", font=("Helvetica", 12), width=400, anchor="w", activefill="#313d52")
canvas_trade.create_text(20, 120, text="Finished Row: 3 Gold Rush", font=("Helvetica", 12), width=400, anchor="w", activefill="#313d52")
canvas_trade.create_text(20, 150, text="Finished Column: 2 Magic Mirror", font=("Helvetica", 12), width=400, anchor="w", activefill="#313d52")
canvas_trade.create_text(20, 180, text="Finished Center: Gold Touch", font=("Helvetica", 12), width=400, anchor="w", activefill="#313d52")

# creating window with items and mechanics descriptions
item_descriptions = read_config("item_descriptions")
effect_descriptions = read_config("effect_descriptions")
canvas_description_list = []
icons = []


def switch_page():
    if canvas_description_list[0]:
        canvas_description_list[0].place_forget()
        canvas_description_list[1].place(x=1300, y=100)
        canvas_description_list[0], canvas_description_list[1] = canvas_description_list[1], canvas_description_list[0]


def create_canvas_description(canvas_title, item_description_list):
    canvas_description = tk.Canvas(window, width=400, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color, highlightbackground="black")
    canvas_description.pack_propagate(False)

    item_description_label = tk.Label(canvas_description, text=canvas_title, fg='black', font=("Helvetica", 18), anchor="w", bg=main_color)
    item_description_label.pack(pady=8)
    position = 0
    for item in item_description_list:
        if item[0] != 0:
            icon = set_item_texture(item[0], (50, 50))
            icons.append(icon)
            canvas_description.create_image(30, 68 + position, image=icon)
        canvas_description.create_text(55, 68 + position, text=item[1], font=("Helvetica", 10), width=350, anchor="w",
                                       activefill="#313d52")
        position += 49
    button_next = tk.Button(canvas_description, text="►", bg=main_color, command=switch_page, height=1, width=2,
                            font=("Helvetica", 10))
    canvas_description.create_window(385, 30, window=button_next)
    canvas_description_list.append(canvas_description)


create_canvas_description("Items and traits:", item_descriptions)
create_canvas_description("Effects:", effect_descriptions)
active_canvas_description = canvas_description_list[0]


# dice roll interface, replaces perk description window after start of stage 2
canvas_roll = tk.Canvas(window, width=400, height=700, relief=tk.GROOVE, borderwidth=5, bg=main_color, highlightbackground="black")
dice_roll = tk.Label(canvas_roll, text="  ", fg='black', font=("Helvetica", 18), anchor="ne", bg=main_color,
                     borderwidth=2, relief="groove")
btn_image = set_item_texture("Octahedron.png", (100, 100))
btn_dice = tk.Button(canvas_roll, image=btn_image, bg=main_color,
                     command=lambda: dice_roll.configure(text=random.choice(range(1, 9))), height=100, width=100,
                     font=("Helvetica", 10))
wind_rose_image = set_item_texture("078wxn75.png", (150, 150))
tankard = set_item_texture("MagicTankard.png", (150, 150))
canvas_roll.create_window(200, 80, window=dice_roll)
canvas_roll.create_window(200, 180, window=btn_dice)
canvas_roll.create_image(200, 380, image=wind_rose_image)
canvas_roll.create_image(200, 600, image=tankard)
