from PIL import Image, ImageTk
import json


def read_config(section):
    with open('config.json', 'r') as file:
        config = json.load(file)[section]
        return config


def set_item_texture(texture: str, size: tuple):
    texture = Image.open("Resources/" + texture)
    texture = texture.resize(size)
    texture = ImageTk.PhotoImage(texture)
    return texture


def distribute_traits():
    """Creates list with 80 entries, every entry representing a single territory, consisting from two elements: trait and territory type.
    Required for creation of a main game field. Traits and amonut of territories can be customised in config.json"""
    dirt_traits = read_config('dirt_traits')  # 50 territories
    rock_traits = read_config('rock_traits')  # 30 territories

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


def check_surrounding_tiles(field_class, coords: tuple):
    """ Functionality for the scanner field. It checks if surrounding territories in 1 tile radius have a "key" trait (any of three types),
     and returns a number of a keys nearby"""
    adj_tiles = [(coords[0] - 1, coords[1] - 1),  # upper left
                 (coords[0] - 1, coords[1]),  # upper center
                 (coords[0] - 1, coords[1] + 1),  # upper right

                 (coords[0], coords[1] - 1),  # center left
                 (coords[0], coords[1] + 1),  # center right

                 (coords[0] + 1, coords[1] - 1),  # lower left
                 (coords[0] + 1, coords[1]),  # lower center
                 (coords[0] + 1, coords[1] + 1),  # lower right
                 ]
    adj_traits = []
    for field_instance in field_class.instances:
        if field_class.get_attr(field_instance)[1] in adj_tiles:
            adj_traits.append(field_class.get_attr(field_instance)[2])
    scan_results = 0
    for entry in adj_traits:
        if entry in ["1key", "CursedKey", "Lockpick"]:
            scan_results += 1
    return scan_results
