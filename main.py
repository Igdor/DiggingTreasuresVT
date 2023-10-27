from Elements import *
from Interface import *
from Mechanics import distribute_traits, check_surrounding_tiles
import sys


def place_field(canvas):
    rows = "ABCDEFGH"
    traits = distribute_traits()
    for row in range(0, len(rows)):
        for column in range(1, 11):
            trait = random.choice(traits)
            traits.remove(trait)
            territory = Field(window=canvas, coords=(row, column), name=rows[row] + str(column), field_type=trait[0], trait=trait[1], color=main_color)
            territory.field_place()
    for instance in Field.instances:
        if Field.get_attr(instance)[2] == "Scanner":
            scan_results = check_surrounding_tiles(Field, Field.get_attr(instance)[1])
            Field.set_trait(instance, "Scan: " + str(scan_results))
            Field.field_place(instance)
    print(sys.getrefcount(Field))


def start():
    btn_celebrate.place(x=1680, y=10)
    game_map.place(x=470, y=140)
    place_field(game_map)
    btn_start.destroy()


def place_player(main_window, coords: list[int, int], color: str, name: str):
    player = Player(main_window, coords, color, name)
    player.player_place()


def start_phase_2():
    game_map.place_forget()
    canvas_description_list[0].place_forget()
    canvas_trade.place_forget()
    newbackgroundimg = set_item_texture("Background_1.jpg", (1810, 900))
    title.config(text="Drinking Pleasures")
    bcg.config(image=newbackgroundimg)
    bcg.image = newbackgroundimg
    window.update()
    canvas_roll.place(x=1300, y=100)

    for row in range(0, 3):
        for column in range(1, 4):
            canvas_roll.create_text((40 + 80 * column), (205 + 80 * (row + 1)), text=str((row * 3) + column), font=("Helvetica", 18), anchor="n", activefill="blue")
    celebration_map.place(x=600, y=200)
    for row in range(0, 4):
        for column in range(1, 5):
            territory = CelebrationField(window=celebration_map, coords=(row, column), color=main_color,
                                         image=set_item_texture("Table.png", (110, 110)),
                                         name=str((row * 4) + column))
            territory.cf_place()


btn_start = tk.Button(window, text="Start", bg=main_color, command=start, height=2, width=10, font=("Helvetica", 10))
btn_start.place(x=10, y=10)
btn_celebrate = tk.Button(window, text="Celebrate", bg=main_color, command=start_phase_2, height=2, width=10, font=("Helvetica", 10))

canvas_description_list[0].place(x=1300, y=100)
place_player(players_interface, [0, 0], main_color, "Player 1")
place_player(players_interface, [1, 0], main_color, "Player 2")

window.mainloop()
