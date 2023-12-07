############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""
    
    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

    def __repr__(self):
        return f"This is the output:{self.name}"

    
    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        #self.code = f"Update to {new_code}"


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", False, False, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # print(melon_types)
    # print(type(melon_types))

    for melon in melon_types:
        print(f"{melon} pairs with {melon.pairings}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_lookup = {}
    for melon in melon_types:
          if melon.code not in melon_type_lookup:
                melon_type_lookup[melon.code] = melon
    
    return melon_type_lookup


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    
    def __init__(self, melon_types, shape_rating, color_rating, field, harvester):

        ids_of_melons = make_melon_type_lookup(melon_types)

        self.melon_types = melon_types
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    
        def is_sellable (melon_num):
            pass
        

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest

#test example for interactive mode

#melon  = MelonType(123, 1930, "green", True, True, "Canteloupe")
#melon2 = MelonType(345, 1960, "orange", True, True, "Honeydew")

#melon2 = Melon("Honeydew",5,5,3, "Sheila")

