from cgi_simple import value_sum

ATTRIBUTES = 'Strength Dexterity Constitution Intelligence Perception Willpower'.split()
DEFENSES = 'Armor Fortitude Reflex Mental'.split()
ATTRIBUTE_SKILLS = {
    'strength': 'Climb Jump Swim'.split(),
    'dexterity': ['Acrobatics', 'Escape Artist', 'Ride', 'Sleight of Hand', 'Stealth'],
    'constitution': [],
    'intelligence': ['Craft ______', 'Deduction', 'Devices', 'Disguise', 'Heal', 'Knowledge ______', 'Knowledge ______', 'Linguistics'],
    'perception': ['Awareness', 'Creature Handling', 'Sense Motive', 'Spellcraft', 'Survival'],
    'willpower': [],
}

ALL_SKILLS_BY_ATTRIBUTE = [
    *ATTRIBUTE_SKILLS['strength'],
    *ATTRIBUTE_SKILLS['dexterity'],
    *ATTRIBUTE_SKILLS['constitution'],
    *ATTRIBUTE_SKILLS['intelligence'],
    *ATTRIBUTE_SKILLS['perception'],
    *ATTRIBUTE_SKILLS['willpower'],
    *['Bluff', 'Intimidate', 'Perform ______', 'Persuasion'],
]


ALL_SKILLS = ['Awareness', 'Balance', 'Bluff', 'Climb', 'Craft', 'Creature Handling',
              'Devices', 'Disguise', 'Escape Artist', 'Heal', 'Intimidate', 'Jump',
              'Knowledge', 'Linguistics', 'Perform', 'Persuasion',
              'Ride', 'Sense Motive', 'Sleight of Hand', 'Spellcraft', 'Sprint',
              'Stealth', 'Survival', 'Swim', 'Tumble']

def at(text):
    return '@{' + text + '}'

def attribute_roll20_text(attribute_name):
    return value_sum([
        attribute_name.lower() + '_starting',
        # 0 if attribute_starting is 0, level / 2 if attribute_starting is 1,
        attribute_name.lower() + '_scaling',
        # f"{{starting_formula} * {at('level')}
        attribute_name.lower() + '_misc',
    ])

def roll20_max_text(x, y):
    return '(ceil(floor(({0}-0.1+100)/({1}+100))/200)*({0}+100)  + ceil(floor(({1}+100)/({0}+100))/(200))*({1}+100)-100)'.format(
        x,
        y,
    )

def roll20_min_text(x, y):
    return '-1 * ' + roll20_max_text(f"(-1 * {x})", f"(-1 * {y})")

ROLL20_CALC = {
    'action_points': value_sum([
        'action_points_base',
        'action_points_willpower',
        'action_points_misc',
    ]),
    'armor_defense': value_sum([
        'armor_scaling',
        'body_armor_defense_value',
        'shield_defense_value',
        'armor_misc',
    ]),
    'armor_scaling': roll20_max_text('@{level}', '@{dexterity}'),
    'hit_points': '(@{hit_points_misc} + (@{hit_points_level} * @{hit_points_constitution}))',
    'fortitude_scaling': roll20_max_text(
        roll20_max_text('@{strength}', '@{constitution}'),
        '@{level}',
    ),
    'mental_scaling': roll20_max_text(
        roll20_max_text('@{intelligence}', '@{willpower}'),
        '@{level}',
    ),
    'reflex_scaling': roll20_max_text(
        roll20_max_text('@{dexterity}', '@{perception}'),
        '@{level}',
    ),
    'strike_accuracy': value_sum([
        'strike_accuracy_scaling',
        'strike_accuracy_misc',
    ]),
    'strike_accuracy_scaling': roll20_max_text('@{level}', '@{perception}'),
}
for attribute in ATTRIBUTES:
    ROLL20_CALC[attribute.lower()] = attribute_roll20_text(attribute.lower())
    starting_formula = at(attribute.lower() + '_starting')
    ROLL20_CALC[attribute.lower() + '_scaling'] = f"""({roll20_min_text(f"({starting_formula} * ({at('level')} / 2))", at('level'))} - ({roll20_min_text(starting_formula, 1)}))"""

for defense in ['fortitude', 'mental', 'reflex']:
    ROLL20_CALC[defense + '_defense'] = value_sum([
        defense + '_scaling',
        defense + '_starting_attribute',
        defense + '_class',
        defense + '_misc',
    ]),
