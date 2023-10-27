from PIL import Image, ImageTk
def distribute_traits():
    dirt_traits = {"1gold": 15,         # Dirt tales: 50
                   "Trader": 4,
                   "Bomb": 6,
                   "Pick": 10,
                   "CursedKey": 2,
                   "Lockpick": 2,
                   "Smugglers": 4,
                   "Tinker": 2,
                   "Crystal mirror": 2,
                   "Scanner": 3
                   }
    rock_traits = {"1key": 5,           # Rock tales: 30
                   "Megabomb": 3,
                   "Wish Stone": 2,
                   "Supplies": 3,
                   "5gold": 15,
                   "Wicked Stone": 2,
                    }

    def add_traits(traits, category):
        trait_list = []
        while sum(traits.values()) > 0:
            for key in traits:
                if traits[key] == 0:
                    continue
                trait_list.append([category, key])
                traits[key] -= 1
        return trait_list

    dirt_trait_list = add_traits(dirt_traits, "dirt")
    rock_trait_list = add_traits(rock_traits, "rock")
    dirt_trait_list.extend(rock_trait_list)
    return dirt_trait_list


def set_item_texture(texture: str, size: tuple):
    texture = Image.open("Resources/" + texture)
    texture = texture.resize(size)
    texture = ImageTk.PhotoImage(texture)
    return texture


def check_surrounding_tiles(cls, coords: tuple):
    """ Functionality for the scanner tile. It checks if surrounding fields in 1 tile radius has key (any),
     and returns number of a keys nearby"""
    adj_tiles = [(coords[0] - 1, coords[1] - 1),
                 (coords[0] - 1, coords[1]),
                 (coords[0] - 1, coords[1] + 1),

                 (coords[0], coords[1] - 1),
                 (coords[0], coords[1] + 1),

                 (coords[0] + 1, coords[1] - 1),
                 (coords[0] + 1, coords[1]),
                 (coords[0] + 1, coords[1] + 1),
                  ]
    adj_traits = []
    for field_instance in cls.instances:
        if cls.get_attr(field_instance)[1] in adj_tiles:
            adj_traits.append(cls.get_attr(field_instance)[2])
    scan_results = 0
    for entry in adj_traits:
        if entry in ["1key", "CursedKey", "Lockpick"]:
            scan_results += 1
    return scan_results
