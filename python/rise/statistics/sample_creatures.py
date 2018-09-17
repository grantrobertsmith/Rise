from rise.statistics.creature import Creature
from rise.statistics.character_class import CharacterClass
from rise.statistics.race import Race
from rise.statistics.size import Size
from rise.statistics.weapon import Weapon
from rise.statistics.armor import Armor
from rise.statistics.shield import Shield

cache = None

def get_sample_creatures():
    global cache
    if not cache:
        cache = generate_sample_creatures()

    return cache

def generate_sample_creatures():
    global cache

    samples = {
        'monsters': generate_sample_monsters(),
    }

    cache = samples
    return cache

def generate_sample_monsters():
    monsters = {}

    # Animals
    monsters['aboleth'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('adept'),
        level=12,
        key_attribute='willpower',
        name='Aboleth',
        natural_armor=6,
        race=Race('aberration'),
        size=Size('huge'),
        starting_attributes=[2, 0, 2, 2, 1, 4],
        weapons=[Weapon('tentacle')],
    )
    monsters['eel'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('slayer'),
        level=6,
        name='Eel',
        natural_armor=6,
        race=Race('animal'),
        size=Size('large'),
        starting_attributes=[2, 2, 0, -8, 1, 0],
        weapons=[Weapon('bite')],
    )
    monsters['black_bear'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('behemoth'),
        level=2,
        name='Bear',
        name_suffix='Black',
        natural_armor=4,
        race=Race('animal'),
        starting_attributes=[3, 1, 2, -7, 1, 0],
        weapons=[Weapon('bite'), Weapon('claw')],
    )
    monsters['brown_bear'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('behemoth'),
        level=4,
        name='Bear',
        natural_armor=4,
        name_suffix='Brown',
        race=Race('animal'),
        size=Size('large'),
        starting_attributes=[3, 1, 2, -7, 1, 0],
        weapons=[Weapon('bite'), Weapon('claw')],
    )
    monsters['dire_wolf'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('slayer'),
        level=5,
        name='Dire Wolf',
        natural_armor=4,
        race=Race('animal'),
        size=Size('large'),
        starting_attributes=[3, 3, 1, -6, 2, 0],
        weapons=[Weapon('bite')],
    )
    monsters['ferret'] = Creature(
        character_class=CharacterClass('slayer'),
        level=1,
        name='Ferret',
        natural_armor=2,
        race=Race('animal'),
        size=Size('tiny'),
        starting_attributes=[-6, 1, -4, -7, 1, -2],
        weapons=[Weapon('bite')],
    )
    monsters['pony'] = Creature(
        character_class=CharacterClass('behemoth'),
        level=2,
        name='Pony',
        natural_armor=4,
        race=Race('animal'),
        size=Size('medium'),
        starting_attributes=[1, 1, 1, -7, 1, 0],
        weapons=[Weapon('bite')],
    )
    monsters['raven'] = Creature(
        character_class=CharacterClass('slayer'),
        level=1,
        name='Raven',
        natural_armor=2,
        race=Race('animal'),
        size=Size('tiny'),
        starting_attributes=[-9, 3, -4, -6, 2, 0],
        weapons=[Weapon('talon')],
    )
    monsters['roc'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('behemoth'),
        level=9,
        name='Roc',
        natural_armor=6,
        race=Race('animal'),
        size=Size('gargantuan'),
        starting_attributes=[4, 2, 1, -7, 1, 0],
        weapons=[Weapon('talon')],
    )
    monsters['wasp'] = Creature(
        character_class=CharacterClass('slayer'),
        level=6,
        name='Wasp',
        name_suffix='Giant',
        natural_armor=6,
        race=Race('animal'),
        size=Size('large'),
        starting_attributes=[2, 4, 0, -8, 3, -1],
        weapons=[Weapon('bite')],
    )
    monsters['wolf'] = Creature(
        character_class=CharacterClass('slayer'),
        level=1,
        name='Wolf',
        natural_armor=4,
        race=Race('animal'),
        size=Size('large'),
        starting_attributes=[1, 3, 1, -6, 2, 0],
        weapons=[Weapon('bite')],
    )
    monsters['dire_beetle'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('behemoth'),
        level=7,
        name='Beetle',
        name_suffix='Dire',
        natural_armor=6,
        race=Race('animal'),
        size=Size('large'),
        starting_attributes=[3, 0, 3, -9, 2, 0],
        weapons=[Weapon('bite')],
    )
    monsters['huge_centipede'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('behemoth'),
        level=8,
        name='Centipede',
        name_suffix='Huge',
        natural_armor=6,
        race=Race('animal'),
        size=Size('huge'),
        starting_attributes=[3, 0, 3, -9, 2, 0],
        weapons=[Weapon('bite')],
    )

    # Animates
    monsters['elemental_air'] = Creature(
        challenge_rating=1,
        character_class=CharacterClass('slayer'),
        level=10,
        name='Elemental',
        name_suffix='Air',
        natural_armor=4,
        race=Race('animate'),
        size=Size('large'),
        starting_attributes=[0, 4, 1, 0, 3, 0],
        weapons=[Weapon('slam')],
    )
    monsters['ram_animus'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('behemoth'),
        level=6,
        name='Animus',
        name_suffix='Ram',
        natural_armor=6,
        race=Race('animate'),
        size=Size('huge'),
        starting_attributes=[3, 0, 2, 0, 3, 0],
        weapons=[Weapon('slam'), Weapon('hoof')],
    )

    # Humanoids
    monsters['cultist'] = Creature(
        armor=Armor('breastplate'),
        character_class=CharacterClass('adept'),
        level=1,
        key_attribute='willpower',
        name='Cultist',
        race=Race('humanoid'),
        starting_attributes=[0, 0, 0, -1, -1, 3],
        weapons=[Weapon('club')],
    )
    monsters['goblin_shouter'] = Creature(
        armor=Armor('hide'),
        challenge_rating=2,
        character_class=CharacterClass('slayer'),
        level=2,
        name='Goblin Shouter',
        natural_armor=0,
        race=Race('humanoid'),
        size=Size('small'),
        starting_attributes=[0, 2, -1, -2, 2, 1],
        weapons=[Weapon('club'), Weapon('sling')],
    )
    monsters['goblin_stabber'] = Creature(
        armor=Armor('hide'),
        character_class=CharacterClass('slayer'),
        level=1,
        name='Goblin Stabber',
        natural_armor=0,
        race=Race('humanoid'),
        size=Size('small'),
        starting_attributes=[0, 3, -1, -2, 2, 0],
        weapons=[Weapon('shortsword'), Weapon('sling')],
    )
    monsters['orc_chieftain'] = Creature(
        armor=Armor('breastplate'),
        challenge_rating=3,
        character_class=CharacterClass('slayer'),
        level=5,
        name='Orc Chieftain',
        natural_armor=2,
        race=Race('humanoid'),
        size=Size('medium'),
        starting_attributes=[4, 0, 1, 0, 2, 2],
        weapons=[Weapon('greataxe')],
    )
    monsters['orc_grunt'] = Creature(
        armor=Armor('breastplate'),
        character_class=CharacterClass('slayer'),
        level=2,
        name='Orc Grunt',
        natural_armor=0,
        race=Race('humanoid'),
        size=Size('medium'),
        starting_attributes=[3, 0, 1, -1, 0, 0],
        weapons=[Weapon('greataxe')],
    )
    monsters['orc_loudmouth'] = Creature(
        armor=Armor('breastplate'),
        challenge_rating=2,
        character_class=CharacterClass('slayer'),
        level=3,
        name='Orc Loudmouth',
        natural_armor=0,
        race=Race('humanoid'),
        size=Size('medium'),
        starting_attributes=[3, 0, 1, -1, 0, 2],
        weapons=[Weapon('greataxe')],
    )
    monsters['orc_shaman'] = Creature(
        armor=Armor('breastplate'),
        challenge_rating=2,
        character_class=CharacterClass('adept'),
        key_attribute='willpower',
        level=3,
        name='Orc Shaman',
        natural_armor=0,
        race=Race('humanoid'),
        size=Size('medium'),
        starting_attributes=[2, 0, 1, -1, 0, 2],
        weapons=[Weapon('greatstaff')],
    )
    monsters['orc_savage'] = Creature(
        armor=Armor('breastplate'),
        character_class=CharacterClass('slayer'),
        level=4,
        name='Orc Savage',
        natural_armor=2,
        race=Race('humanoid'),
        size=Size('medium'),
        starting_attributes=[4, 2, 1, -1, 0, 0],
        weapons=[Weapon('greataxe')],
    )

    # Magical beasts
    monsters['large_red_dragon'] = Creature(
        character_class=CharacterClass('behemoth'),
        level=9,
        name='Dragon',
        name_suffix='Large Red',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('large'),
        starting_attributes=[3, 0, 3, 2, 2, 2],
        weapons=[Weapon('bite')],
    )
    monsters['ankheg'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('slayer'),
        level=7,
        key_attribute='constitution',
        name='Ankheg',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('large'),
        starting_attributes=[3, 1, 2, -7, 1, 0],
        weapons=[Weapon('bite')],
    )
    monsters['aranea'] = Creature(
        character_class=CharacterClass('adept'),
        level=5,
        name='Aranea',
        natural_armor=4,
        race=Race('magical beast'),
        starting_attributes=[0, 2, 0, 2, 1, 3],
        weapons=[Weapon('bite')],
    )
    monsters['basilisk'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('behemoth'),
        key_attribute='perception',
        level=5,
        name='Basilisk',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('medium'),
        starting_attributes=[2, -1, 2, -6, 2, 0],
        weapons=[Weapon('bite')],
    )
    monsters['behir'] = Creature(
        challenge_rating=3,
        character_class=CharacterClass('behemoth'),
        key_attribute='constitution',
        level=8,
        name='Behir',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('huge'),
        starting_attributes=[4, 1, 2, -3, 1, 0],
        weapons=[Weapon('bite'), Weapon('claw')],
    )
    monsters['blink_dog'] = Creature(
        character_class=CharacterClass('slayer'),
        level=3,
        name='Blink Dog',
        natural_armor=4,
        race=Race('magical beast'),
        size=Size('medium'),
        starting_attributes=[0, 3, 0, 0, 1, 0],
        weapons=[Weapon('bite')],
    )
    monsters['centaur'] = Creature(
        armor=Armor('leather'),
        character_class=CharacterClass('slayer'),
        level=3,
        name='Centaur',
        natural_armor=4,
        race=Race('magical beast'),
        size=Size('large'),
        starting_attributes=[1, 2, 2, 0, 2, 0],
        weapons=[Weapon('longsword'), Weapon('longbow'), Weapon('hoof')],
    )
    monsters['cockatrice'] = Creature(
        character_class=CharacterClass('adept'),
        key_attribute='constitution',
        level=3,
        name='Cockatrice',
        natural_armor=4,
        race=Race('magical beast'),
        size=Size('small'),
        starting_attributes=[-2, 3, 0, -8, 1, 0],
        weapons=[Weapon('bite')],
    )
    monsters['darkmantle'] = Creature(
        character_class=CharacterClass('slayer'),
        level=1,
        name='Darkmantle',
        natural_armor=4,
        race=Race('magical beast'),
        size=Size('small'),
        starting_attributes=[3, 0, 1, -8, 0, 0],
        weapons=[Weapon('slam')],
    )
    monsters['frost_worm'] = Creature(
        challenge_rating=3,
        character_class=CharacterClass('behemoth'),
        key_attribute='constitution',
        level=12,
        name='Frost Worm',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('gargantuan'),
        starting_attributes=[4, 0, 3, -8, 2, 0],
        weapons=[Weapon('bite'), Weapon('slam')],
    )
    monsters['girallon'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('slayer'),
        level=5,
        name='Girallon',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('large'),
        starting_attributes=[3, 3, 0, -8, 2, -1],
        weapons=[Weapon('claw')],
    )
    monsters['griffin'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('slayer'),
        level=4,
        name='Griffon',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('large'),
        starting_attributes=[2, 3, 2, -4, 1, 0],
        weapons=[Weapon('talon')],
    )
    monsters['hydra5'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('behemoth'),
        level=5,
        name='Hydra, 5 Headed',
        natural_armor=4,
        race=Race('magical beast'),
        size=Size('huge'),
        starting_attributes=[2, 0, 4, -8, 0, 0],
        weapons=[Weapon('bite')],
    )
    monsters['hydra6'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('behemoth'),
        level=6,
        name='Hydra, 6 Headed',
        natural_armor=4,
        race=Race('magical beast'),
        size=Size('huge'),
        starting_attributes=[2, 0, 4, -8, 0, 0],
        weapons=[Weapon('bite')],
    )
    monsters['minotaur'] = Creature(
        character_class=CharacterClass('slayer'),
        level=4,
        name='Minotaur',
        natural_armor=4,
        race=Race('magical beast'),
        size=Size('large'),
        starting_attributes=[3, 2, 1, -2, 2, 0],
        weapons=[Weapon('greataxe'), Weapon('gore')],
    )
    monsters['thaumavore'] = Creature(
        character_class=CharacterClass('slayer'),
        level=3,
        name='Thaumavore',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('small'),
        starting_attributes=[2, 3, 0, -7, 1, 0],
        weapons=[Weapon('bite')],
    )
    monsters['banehound'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('slayer'),
        level=5,
        name='Banehound',
        natural_armor=6,
        race=Race('magical beast'),
        size=Size('huge'),
        starting_attributes=[1, 3, 0, 1, 3, 0],
        weapons=[Weapon('bite')],
    )

    # Monstrous humanoids<M-F7>
    monsters['banshee'] = Creature(
        character_class=CharacterClass('adept'),
        key_attribute='willpower',
        level=3,
        name='Banshee',
        natural_armor=4,
        race=Race('monstrous humanoid'),
        size=Size('medium'),
        starting_attributes=[1, 2, 0, 0, 1, 2],
        weapons=[Weapon('claw')],
    )
    monsters['hill_giant'] = Creature(
        armor=Armor('breastplate'),
        character_class=CharacterClass('behemoth'),
        level=5,
        name='Giant',
        name_suffix='Hill',
        natural_armor=4,
        race=Race('monstrous humanoid'),
        size=Size('large'),
        starting_attributes=[3, -2, 1, -2, 0, 0],
        weapons=[Weapon('greatclub'), Weapon('boulder')],
    )
    monsters['stone_giant'] = Creature(
        armor=Armor('breastplate'),
        character_class=CharacterClass('behemoth'),
        level=9,
        name='Giant',
        name_suffix='Stone',
        natural_armor=6,
        race=Race('monstrous humanoid'),
        size=Size('huge'),
        starting_attributes=[3, -2, 3, -1, 2, 0],
        weapons=[Weapon('greatclub'), Weapon('boulder')],
    )
    monsters['storm_giant'] = Creature(
        armor=Armor('breastplate'),
        character_class=CharacterClass('slayer'),
        key_attribute='willpower',
        level=15,
        name='Giant',
        name_suffix='Storm',
        natural_armor=4,
        race=Race('monstrous humanoid'),
        size=Size('gargantuan'),
        starting_attributes=[3, -1, 1, 1, 2, 2],
        weapons=[Weapon('greatsword')],
    )
    monsters['green_hag'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('adept'),
        key_attribute='perception',
        level=5,
        name='Hag',
        name_suffix='Green',
        natural_armor=6,
        race=Race('monstrous humanoid'),
        size=Size('medium'),
        starting_attributes=[0, 2, 0, 2, 3, 2],
        weapons=[Weapon('claw')],
    )
    monsters['medusa'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('adept'),
        key_attribute='perception',
        level=7,
        name='Medusa',
        natural_armor=4,
        race=Race('monstrous humanoid'),
        size=Size('medium'),
        starting_attributes=[0, 1, 0, 1, 2, 2],
        weapons=[Weapon('longbow'), Weapon('snakes')],
    )

    # Outsiders
    monsters['astral_deva'] = Creature(
        character_class=CharacterClass('adept'),
        key_attribute='willpower',
        level=14,
        name='Angel',
        name_suffix='Astral Deva',
        natural_armor=6,
        race=Race('outsider'),
        shield=Shield('heavy'),
        starting_attributes=[2, 2, 2, 2, 2, 2],
        weapons=[Weapon('mace')],
    )
    monsters['arrowhawk'] = Creature(
        character_class=CharacterClass('slayer'),
        key_attribute='dexterity',
        level=3,
        name='Arrowhawk',
        natural_armor=4,
        race=Race('outsider'),
        starting_attributes=[1, 4, -1, 0, 3, 0],
        weapons=[Weapon('bite')],
    )
    monsters['bebelith'] = Creature(
        character_class=CharacterClass('slayer'),
        key_attribute='constitution',
        level=11,
        name='Demon',
        name_suffix='Bebelith',
        natural_armor=6,
        race=Race('outsider'),
        size=Size('huge'),
        starting_attributes=[2, 3, 2, 0, 1, 0],
        weapons=[Weapon('bite')],
    )
    monsters['hell_hound'] = Creature(
        character_class=CharacterClass('slayer'),
        key_attribute='constitution',
        level=4,
        name='Hell Hound',
        natural_armor=4,
        race=Race('outsider'),
        size=Size('medium'),
        starting_attributes=[1, 3, 0, -3, 2, 0],
        weapons=[Weapon('bite')],
    )
    monsters['flamebrother_salamander'] = Creature(
        character_class=CharacterClass('slayer'),
        key_attribute='constitution',
        level=4,
        name='Salamander',
        name_suffix='Flamebrother',
        natural_armor=6,
        race=Race('outsider'),
        size=Size('medium'),
        starting_attributes=[4, 2, 0, 1, 1, 0],
        # TODO: weapons deal fire damage, and its strength is lower
        weapons=[Weapon('spear'), Weapon('tail slam')],
    )
    monsters['janni'] = Creature(
        armor=Armor('studded leather'),
        character_class=CharacterClass('adept'),
        level=7,
        name='Janni',
        natural_armor=6,
        race=Race('outsider'),
        size=Size('medium'),
        starting_attributes=[2, 3, 0, 1, 2, 1],
        weapons=[Weapon('shortsword')],
    )
    monsters['salamander_battlemaster'] = Creature(
        challenge_rating=3,
        character_class=CharacterClass('slayer'),
        key_attribute='constitution',
        level=5,
        name='Salamander',
        name_suffix='Battlemaster',
        natural_armor=6,
        race=Race('outsider'),
        size=Size('medium'),
        starting_attributes=[4, 2, 0, 1, 2, 1],
        # TODO: weapons deal fire damage, and its strength is lower
        weapons=[Weapon('spear'), Weapon('tail slam')],
    )

    # Undead
    monsters['allip'] = Creature(
        character_class=CharacterClass('adept'),
        level=4,
        name='Allip',
        natural_armor=4,  # How does this interact with being incorporeal?
        race=Race('undead'),
        starting_attributes=[0, 3, 0, 0, 0, 3],
        weapons=[Weapon('draining touch')],
    )
    monsters['spectre'] = Creature(
        challenge_rating=2,
        character_class=CharacterClass('adept'),
        level=7,
        name='Spectre',
        natural_armor=4,  # How does this interact with being incorporeal?
        race=Race('undead'),
        starting_attributes=[0, 3, 0, 0, 0, 3],
        weapons=[Weapon('draining touch')],
    )
    monsters['dirgewalker'] = Creature(
        challenge_rating=4,
        character_class=CharacterClass('adept'),
        key_attribute='willpower',
        level=4,
        name='Dirgewalker',
        natural_armor=6,
        race=Race('undead'),
        size=Size('medium'),
        starting_attributes=[0, 3, 0, 1, 3, 2],
        weapons=[Weapon('claw')],
    )
    monsters['skeleton'] = Creature(
        character_class=CharacterClass('slayer'),
        level=1,
        name='Skeleton',
        natural_armor=6,
        race=Race('undead'),
        size=Size('medium'),
        starting_attributes=[2, 2, 0, 0, 0, 0],
        weapons=[Weapon('claw')],
    )
    monsters['skeleton_warrior'] = Creature(
        character_class=CharacterClass('slayer'),
        level=3,
        name='Skeleton',
        name_suffix='Warrior',
        natural_armor=6,
        race=Race('undead'),
        size=Size('medium'),
        starting_attributes=[2, 2, 0, 0, 0, 0],
        weapons=[Weapon('claw')],
    )
    monsters['zombie'] = Creature(
        character_class=CharacterClass('behemoth'),
        level=1,
        name='Zombie',
        natural_armor=6,
        race=Race('undead'),
        size=Size('medium'),
        starting_attributes=[2, 0, 3, 0, 0, 0],
        weapons=[Weapon('slam')],
    )

    return monsters
