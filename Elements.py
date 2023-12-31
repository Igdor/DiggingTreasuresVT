import tkinter as tk
from Mechanics import read_config, set_item_texture


class Player:
    """A class for creating player interface for each player. Contains an Item subclass for handling each type of item in player`s posession."""
    def __init__(self, window, coords: list[int, int], color: str, name: str):
        self.window = window
        self.coords = coords
        self.player_interface = None
        self.name = name
        self.color = color
        self.items = [0, 0, 0, 0]

    class Item:
        """Subclass of a Player class. Created for manipulations with items in player inventory."""
        def __init__(self, name, canvas, coords: list[int, int], amount: int, color: str, icon: str):
            self.name = name
            self.canvas = canvas
            self.coords = coords
            self.amount = amount
            self.icon = icon
            self.item_frame = None
            self.button_add = None
            self.button_subtract = None
            self.color = color

        def add_item(self, amount=1):
            self.amount += amount
            self.canvas.itemconfig(self.name, text=self.amount)

        def subtract_item(self):
            self.amount -= 1
            self.canvas.itemconfig(self.name, text=self.amount)

        def get_icon(self):
            return self.icon

        def create_item(self):
            """Creates an item widget in player interface. Consists of icon of the item, amount label and buttons for changing amount"""
            self.item_frame = tk.Frame(self.canvas, width=50, height=50, relief=tk.GROOVE, borderwidth=5, bg=self.color)
            self.button_add = tk.Button(self.canvas, text="+", bg=self.color, command=self.add_item, height=1,
                                        width=1, font=("Helvetica", 10))
            self.button_subtract = tk.Button(self.canvas, text="-", bg=self.color, command=self.subtract_item, height=1,
                                             width=1, font=("Helvetica", 10))

            self.icon = set_item_texture(self.icon, (60, 50))

            self.canvas.create_text(self.coords[0], self.coords[1] + 40, text=0, font=("Helvetica", 10), width=140, justify="center", tags=self.name)
            self.canvas.create_window(self.coords[0] + 20, self.coords[1] + 40, window=self.button_add)
            self.canvas.create_window(self.coords[0] - 20, self.coords[1] + 40, window=self.button_subtract)
            self.canvas.create_image(self.coords[0], self.coords[1], image=self.icon)

    def player_place(self):
        """Creates a player interface in a main window."""
        self.player_interface = tk.Canvas(self.window, width=290, height=200, relief=tk.GROOVE, borderwidth=5, bg=self.color,
                                          highlightbackground="black")
        self.player_interface.grid(row=self.coords[0], column=self.coords[1])

        player_name = tk.Entry(self.player_interface, bd=4, width=15, bg=self.color, font=("Helvetica", 10),
                               justify="center")
        player_name.insert(0, self.name)

        label_buffs = tk.Label(self.player_interface, text="Effects", fg='black', font=("Helvetica", 10), anchor="n",
                               bg=self.color)
        entry_buffs = tk.Entry(self.player_interface, bd=4, width=20, bg=self.color, font=("Helvetica", 10),
                               justify="center")

        item_1 = self.Item("item1", self.player_interface, [50, 75], self.items[0], self.color, "coins.png")
        item_1.create_item()
        item_2 = self.Item("item2", self.player_interface, [115, 75], self.items[1], self.color, "pickaxe.png")
        item_2.create_item()
        item_3 = self.Item("item3", self.player_interface, [180, 75], self.items[2], self.color, "KeyPart.png")
        item_3.create_item()
        item_4 = self.Item("item4", self.player_interface, [245, 75], self.items[3], self.color, "Trade.png")
        item_4.create_item()
        item_4.add_item(2)

        self.player_interface.create_window(150, 10, window=player_name, anchor="n")
        self.player_interface.create_window(10, 160, window=label_buffs, anchor="w")
        self.player_interface.create_window(70, 160, window=entry_buffs, anchor="w")


class Field:
    """A class for creating main game map. Each field contain a trait, initially hidden under a button,
     and belongs to on of 2 types: dirt or rock."""
    instances = []

    def __init__(self, window, coords: tuple[int, int], name: str, field_type: int, trait: str, color: str):
        self.window = window
        self.territory = None
        self.coords = coords
        self.name = name
        self.field_type = field_type
        self.trait = trait
        self.color = color
        self.icon = None
        self.is_open = False
        self.btn_dig = None
        self.btn_rock = None
        self.btn_dirt = None
        self.__class__.instances.append(self)

    def get_attr(self):
        return [self.name, self.coords, self.trait]

    def set_trait(self, newtrait=None):
        if newtrait is not None:
            self.trait = newtrait

    def reveal(self):
        self.territory.itemconfigure(tagOrId="btndig", state="hidden")
        self.is_open = True

    def field_place(self):
        """Places a field of corresponding type on a coordinates in self.coords. Applies a special outline and color
         if field has a scaner trait or placed in a center of a map."""
        icons = read_config("fields_icons")
        center_fields = ("D4", "D5", "D6", "D7", "E4", "E5", "E6", "E7")
        self.territory = tk.Canvas(self.window, width=50, height=50, relief=tk.GROOVE, borderwidth=5,
                                   bg=self.color, highlightbackground="black")
        if self.name in center_fields:
            self.territory = tk.Canvas(self.window, width=50, height=50, relief=tk.RAISED, bd=7,
                                       bg="#ba950f", highlightbackground="orange")
        if "Scan: " in self.trait:
            self.territory = tk.Canvas(self.window, width=50, height=50, relief=tk.GROOVE, bd=7,
                                       bg="#8abcd4", highlightbackground="blue")
            self.territory.create_text(15, 50, text=self.trait, font=("Helvetica", 8), width=45, anchor="w")
        if "Tinker" in self.trait or "Trader" in self.trait:  # adds labels to a tiles with these traits in addition to an icon.
            self.territory.create_text(15, 50, text=self.trait, font=("Helvetica", 8), width=45, anchor="w")
        self.territory.grid(row=self.coords[0], column=self.coords[1], padx=5, pady=5)
        if self.trait in icons.keys() and "Scan: " not in self.trait:
            self.icon = set_item_texture(icons.get(self.trait), (50, 50))
            self.territory.create_image(32, 32, image=self.icon)
        elif "Scan: " in self.trait:  # this is required to properly place an icon for the scaner, as an actual trait name can differ bc of scan results
            self.trait = "Scaner"
            self.icon = set_item_texture(icons.get(self.trait), (40, 40))
            self.territory.create_image(33, 27, image=self.icon)
        else:
            self.territory.create_text(15, 20, text=self.trait, font=("Helvetica", 8), width=45, anchor="nw")

        self.btn_rock = set_item_texture("rockytexture.png", (60, 60))
        self.btn_dirt = set_item_texture("earthtexture.png", (60, 60))
        self.btn_dig = tk.Button(self.territory, height=48, width=48, text=self.name, command=self.reveal, font=("Arial", 12),
                                 bg="#915436" if self.field_type == "dirt" else "#a6a5a4",
                                 image=self.btn_dirt if self.field_type == "dirt" else self.btn_rock, compound="center")
        self.territory.create_window(33, 33, window=self.btn_dig, tags="btndig", anchor="center")


class CelebrationField:
    """A class to create a fields for a second (secret) stage of a game. Essentialy slightly altered Tic-Tac-Toe field."""
    def __init__(self, window, coords, name, image, color):
        self.window = window
        self.territory = None
        self.coords = coords
        self.name = name
        self.image = image
        self.state = 0
        self.color = color
        self.btn_cycle = None

    def cycle_mark(self):
        """Cycles between 3 appearances of field: empty table, table with one type of beer, and table with other type."""
        if self.state == 0:
            self.image = set_item_texture("BeerOnTable1.png", (110, 110))
            self.btn_cycle.config(image=self.image)
            self.territory.itemconfigure(tagOrId="table", window=self.btn_cycle)
            self.state = 1
        elif self.state == 1:
            self.image = set_item_texture("BeerOnTable2.png", (110, 110))
            self.btn_cycle.config(image=self.image)
            self.territory.itemconfigure(tagOrId="table", window=self.btn_cycle)
            self.state = 2
        else:
            self.image = set_item_texture("Table.png", (110, 110))
            self.btn_cycle.config(image=self.image)
            self.territory.itemconfigure(tagOrId="table", window=self.btn_cycle)
            self.state = 0

    def cf_place(self):
        self.territory = tk.Canvas(self.window, width=100, height=100, relief=tk.GROOVE, borderwidth=5,
                                   bg=self.color, highlightbackground="black")
        self.territory.grid(row=self.coords[0], column=self.coords[1], padx=5, pady=5)
        self.btn_cycle = tk.Button(self.territory, height=100, width=100, command=self.cycle_mark, text=self.name, compound="center",
                                   font=("Arial", 12), bg=self.color, image=self.image)
        self.territory.create_window(57, 55, window=self.btn_cycle, tags="table")
