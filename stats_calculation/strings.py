
STRENGTH = 'strength'
STR = STRENGTH
DEXTERITY = 'dexterity' 
DEX = DEXTERITY
CONSTITUTION = 'constitution'
CON = CONSTITUTION
INTELLIGENCE = 'intelligence'
INT = INTELLIGENCE
PERCEPTION = 'perception'
PER = PERCEPTION
WILLPOWER = 'willpower'
WIL = WILLPOWER
ATTRIBUTE_NAMES = (STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE,
        PERCEPTION, WILLPOWER)
ATTRIBUTES = ATTRIBUTE_NAMES

ARMOR = 'armor'
SHIELD = 'shield'

FORTITUDE = 'fortitude'
FORT = FORTITUDE
REFLEX = 'reflex'
REF = REFLEX
MENTAL = 'mental'
SPECIAL_DEFENSE_NAMES = [FORTITUDE, REFLEX, MENTAL]
SPECIAL_DEFENSE = 'special defense'

WEAPON_DAMAGE = 'damage'
WEAPON_ENCUMBRANCE = 'encumbrance'
WEAPON_FEATURES = [WEAPON_DAMAGE, WEAPON_ENCUMBRANCE]

ARMOR_BONUS = 'ac bonus'
ARMOR_ENCUMBRANCE = 'encumbrance'
ARMOR_CHECK = 'check penalty'
ARMOR_ASF = 'arcane spell failure'
ARMOR_FEATURES = [ARMOR_BONUS, ARMOR_ENCUMBRANCE, ARMOR_CHECK, ARMOR_ASF]
ARMOR_TYPE_BODY = 'body'
ARMOR_TYPE_SHIELD = 'shield'

ENCUMBRANCE_LIGHT = 'light'
ENCUMBRANCE_MEDIUM = 'medium'
ENCUMBRANCE_HEAVY = 'heavy'
ENCUMBRANCE_DOUBLE = 'double'
ENCUMBRANCE_NONE = 'none'

ATTACK_TYPE_MELEE = 'melee'
ATTACK_TYPE_PROJECTILE = 'projectile'
ATTACK_TYPE_THROWN = 'thrown'
ATTACK_TYPE_SPECIAL = 'special'

EXTREME = 'extreme'
GOOD = 'good'
AVERAGE = 'average'
AVG = AVERAGE
POOR = 'poor'
PROGRESSIONS = [None, POOR, AVERAGE, GOOD, EXTREME]

SIZE_FINE = 'fine'
SIZE_DIMINUITIVE = 'diminuitive'
SIZE_TINY = 'tiny'
SIZE_SMALL = 'small'
SIZE_MEDIUM = 'medium'
SIZE_LARGE = 'large'
SIZE_HUGE = 'huge'
SIZE_GARGANTUAN = 'gargantuan'
SIZE_COLOSSAL = 'colossal'
SIZES = [SIZE_FINE, SIZE_DIMINUITIVE, SIZE_TINY, SIZE_SMALL, SIZE_MEDIUM, SIZE_LARGE,
        SIZE_HUGE, SIZE_GARGANTUAN, SIZE_COLOSSAL]

DAMAGE_PHYSICAL = 'physical'
DAMAGE_SLASHING = 'slashing'
DAMAGE_PIERCING = 'piercing'
DAMAGE_BLUDGEONING = 'bludgeoning'
DAMAGE_ACID = 'acid'
DAMAGE_COLD = 'cold'
DAMAGE_ELECTRICITY = 'electricity'
DAMAGE_FIRE = 'fire'

ABILITY = 'ability'
ABILITY_TEMPLATE = 'template'
ABILITY_FEAT = 'feat'
ABILITY_TRAIT = 'trait'
ABILITY_TYPES = set((ABILITY, ABILITY_TEMPLATE, ABILITY_FEAT, ABILITY_TRAIT))
ABILITY_TYPE_GROUPS = set('abilities templates feats traits'.split())

WEAPON_PRIMARY = 'primary weapon'
WEAPON_SECONDARY = 'secondary weapon'
WEAPONS = (WEAPON_PRIMARY, WEAPON_SECONDARY)
AD = 'armor defense'
MD = 'maneuver defense'
NAME = 'name'
CLASS_NAME = 'class name'
ATTACK_BONUS = 'attack bonus'
MANEUVER_BONUS = 'maneuver bonus'
LEVEL = 'level'
CLASS_PROGRESSION = 'level progression'
ALIGNMENT = 'alignment'
ABILITIES = 'abilities'
HIT_POINTS = 'hit points'
HIT_VALUE = 'hit value'
INITIATIVE = 'initiative'
REACH = 'reach'
SPACE = 'space'
SPEEDS = 'speeds'
SIZE = 'size'
VERBOSE = 'verbose'
DAMAGE_REDUCTION = 'damage reduction'
DR = DAMAGE_REDUCTION
DAMAGE = 'damage'

BARBARIAN = 'barbarian'
CLERIC = 'cleric'
DRUID = 'druid'
FIGHTER = 'fighter'
MONK = 'monk'
PALADIN = 'paladin'
RANGER = 'ranger'
ROGUE = 'rogue'
SPELLWARPED = 'spellwarped'
SORCERER = 'sorcerer'
WIZARD = 'wizard'
PC_CLASSES = (BARBARIAN, CLERIC, DRUID, FIGHTER, MONK, PALADIN, RANGER, ROGUE, SPELLWARPED, SORCERER, WIZARD)
GENERIC = 'generic'
WARRIOR = 'warrior'

ANIMAL = 'animal'
ABERRATION = 'aberration'
CONSTRUCT = 'construct'
DRAGON = 'dragon'
FEY = 'fey'
HUMANOID = 'humanoid'
MAGICAL_BEAST = 'magical beast'
MONSTROUS_HUMANOID = 'monstrous humanoid'
OOZE = 'ooze'
OUTSIDER = 'outsider'
PLANT = 'plant'
UNDEAD = 'undead'

ENDLINE = '\\par\n'

BASE = 'base'
ENHANCEMENT = 'enhancement'
BAB = 'base attack bonus'
USE_MAGIC_BONUSES = 'use magic bonuses'
IDEAL = 'ideal'

LAND_SPEED = 'land'
BURROW_SPEED = 'burrow'
CLIMB_SPEED = 'climb'
FLY_SPEED = 'fly'
SWIM_SPEED = 'swim'
SPEED_MODES = (LAND_SPEED, BURROW_SPEED, CLIMB_SPEED, FLY_SPEED, SWIM_SPEED)

ACROBATICS = 'acrobatics'
ATHLETICS = 'athletics'
BLUFF = 'bluff'
CLIMB = 'climb'
CRAFT = 'craft'
CREATURE_HANDLING = 'creature_handling'
DEVICES = 'devices'
DISGUISE = 'disguise'
ESCAPE_ARTIST = 'escape_artist'
HEAL = 'heal'
INTIMIDATE = 'intimidate'
KNOWLEDGE = 'knowledge'
LINGUISTICS = 'linguistics'
PERCEPTION = 'perception'
PERFORM = 'perform'
PERSUASION = 'persuasion'
PROFESSION = 'profession'
RIDE = 'ride'
SENSE_MOTIVE = 'sense_motive'
SLEIGHT_OF_HAND = 'sleight_of_hand'
SPELLCRAFT = 'spellcraft'
STEALTH = 'stealth'
SURVIVAL = 'survival'
SWIM = 'swim'
SKILLS = 'skills'
SKILL_NAMES = (ATHLETICS, BLUFF, CLIMB, CRAFT, CREATURE_HANDLING, DEVICES, DISGUISE, ESCAPE_ARTIST, HEAL, INTIMIDATE, KNOWLEDGE, LINGUISTICS, PERCEPTION, PERFORM, PERSUASION, PROFESSION, RIDE, SENSE_MOTIVE, SLEIGHT_OF_HAND, SPELLCRAFT, STEALTH, SURVIVAL, SWIM)

#tags
TAG_ATTACK = 'special attack'
TAG_AURA = 'aura'
TAG_DEFENSE = 'special defense'
TAG_SENSE = 'sense'
TAG_MOVE = 'movement'
TAG_PROTECTION = 'protection'
TAG_IMMUNITY = 'immunity'
TAG_POWER = 'power'
TAG_STYLE = 'style'

DESCRIPTION = 'description'
COMBAT_DESCRIPTION = 'combat'

ACTIVE = 'active'
INACTIVE = 'inactive'

CLASS = 'class'
CURRENT_HIT_POINTS = 'current hit points'
CRITICAL_DAMAGE = 'critical damage'
NATURAL_ARMOR = 'natural armor'
CREATURE_TYPE = 'creature_type'
SPECIAL = 'special'