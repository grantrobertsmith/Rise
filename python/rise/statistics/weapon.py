# For brevity, return a three-item array instead of a dict.
# The order is [Damage die modifier, encumbrance category, attribute].
# If the weapon has no encumbrance, "encumbrance category" is None.
# If no special attribute is used, "attribute" is None.
def properties_from_weapon_name(name):
    return {
        # Manufactured weapons
        'greatsword': [1, Weapon.HEAVY, None],
        'longsword': [0, Weapon.MEDIUM, None],
        'mace': [0, Weapon.MEDIUM, None],
        'club': [-1, Weapon.MEDIUM, None],
        'draining touch': [-1, Weapon.LIGHT, None],
        'shortsword': [-1, Weapon.LIGHT, None],

        # Natural weapons
        'bite': [0, Weapon.MEDIUM, None],
        'claw': [-1, Weapon.LIGHT, None],
        'talon': [-1, Weapon.LIGHT, None],
        'tentacle': [0, Weapon.MEDIUM, None],

        # Special "weapons"
        # TODO: is this the correct representation?
        'fire breath': [-2, None, 'constitution'],
    }[name]

class Weapon(object):
    LIGHT = 'light'
    MEDIUM = 'medium'
    HEAVY = 'heavy'

    def __init__(self, name):
        self.name = name
        properties = properties_from_weapon_name(name)
        self.damage_modifier = properties[0]
        self.encumbrance_category = properties[1]
        self.attribute = properties[2]