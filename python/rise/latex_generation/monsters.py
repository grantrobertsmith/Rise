#!/usr/bin/env python3

import click
from rise.latex_generation.book_path import book_path
from rise.latex.get_creature_latex import get_creature_latex
from rise.latex.ability import active_ability, passive_ability
from rise.statistics.weapon import Weapon
from rise.latex.util import latexify
from rise.statistics.sample_creatures import get_sample_creatures

def trunc_to_five(n):
    return (n // 5) * 5


# These are functions commmon to multiple creatures that modify the creature's
# statistics in some way.
modifiers = {}

def ichor_modifier(creature):
    creature.name = f"Ichor {creature.name}"
    creature.species.mental_defense_bonus = 6
    return creature
modifiers['ichor'] = ichor_modifier


# These are passive abiliites common to multiple creature. The abilities take
# the creature as an argument to alow referencing aspects of the creature in the
# description.
passives = {
    'ichor healing': lambda creature: passive_ability('Ichor Healing', f"""
        The {creature.name} heals {creature.level * creature.cr_mod} hit points at the end of each round.
    """),
}

def aberrations(sample_monsters):
    monsters = []

    aboleth = sample_monsters['aboleth']
    monsters.append(get_creature_latex(
        aboleth,
        active_abilities=[
            active_ability('Mind Crush', f"""
                The aboleth makes a +{aboleth.accuracy()} vs. Mental attack against a creature in Long range.
                \\hit The target takes {aboleth.standard_damage('magical') + 3} psionic damage and is \\glossterm<stunned> as a \\glossterm<condition>.
                \\crit The aboleth can spend an action point.
                If it does, the target is \\glossterm<dominated> by the aboleth for as long as the aboleth \\glossterm<attunes> to this ability.
                Otherwise, the target takes double the damage of a non-critical hit.
            """, tags=['Mind']),
            active_ability('Psionic Blast', f"""
                The aboleth makes a +{aboleth.accuracy()} vs. Mental attack against enemies in a Large cone.
                \\hit Each target takes {aboleth.standard_damage('magical') + 1} psionic damage and is \\glossterm<stunned> as a \\glossterm<condition>.
            """, tags=['Mind']),
        ],
        passive_abilities=[
            passive_ability('Rituals', f"""
                The aboleth can learn and perform arcane rituals of up to 6th level.
            """),
        ],
        speed='50 ft. swim',
    ))

    return '\n\n'.join(monsters)


def animals(sample_monsters):
    monsters = []

    eel = sample_monsters['eel']
    monsters.append(get_creature_latex(
        eel,
    ))

    black_bear = sample_monsters['black_bear']
    monsters.append(get_creature_latex(
        black_bear,
        active_abilities=[
            active_ability('Rend', """
                The bear makes a claw strike against two targets within reach.
            """),
        ],
        immunities=['staggered'],
    ))

    monsters.append(get_creature_latex(
        modifiers['ichor'](black_bear),
        active_abilities=[
            active_ability('Rend', """
                The bear makes a claw strike against two targets within reach.
            """),
        ],
        passive_abilities=[
            passives['ichor healing'](black_bear),
        ],
        immunities=['staggered'],
    ))

    brown_bear = sample_monsters['brown_bear']
    monsters.append(get_creature_latex(
        brown_bear,
        active_abilities=[
            active_ability('Rend', """
                The bear makes a claw strike against two targets within reach.
            """),
        ],
        immunities=['staggered'],
    ))

    dire_wolf = sample_monsters['dire_wolf']
    monsters.append(get_creature_latex(
        dire_wolf,
        active_abilities=[
            active_ability('Pounce', """
                The dire wolf moves up to its movement speed.
                If it uses this ability during the action phase, it can make a bite strike during the delayed action phase.
            """),
        ],
    ))

    ferret = sample_monsters['ferret']
    monsters.append(get_creature_latex(
        ferret,
    ))

    pony = sample_monsters['pony']
    monsters.append(get_creature_latex(
        pony,
    ))

    raven = sample_monsters['raven']
    monsters.append(get_creature_latex(
        raven,
    ))

    roc = sample_monsters['roc']
    monsters.append(get_creature_latex(
        roc,
        active_abilities=[
            active_ability('Flyby Attack', """
                The roc flies up to its flying movement speed.
                It can make a talon strike or use the \\textit<grapple> ability at any point during this movement.
            """),
        ],
        speed="80 ft. fly",
    ))

    wasp = sample_monsters['wasp']
    monsters.append(get_creature_latex(
        wasp,
        speed="50 ft. fly (good)",
    ))

    wolf = sample_monsters['wolf']
    monsters.append(get_creature_latex(
        wolf,
    ))

    dire_beetle = sample_monsters['dire_beetle']
    monsters.append(get_creature_latex(
        dire_beetle,
    ))

    huge_centipede = sample_monsters['huge_centipede']
    monsters.append(get_creature_latex(
        huge_centipede,
    ))

    monsters.sort()

    return '\n\n'.join(monsters)


def animates(sample_monsters):
    monsters = []

    elemental_air = sample_monsters['elemental_air']
    monsters.append(get_creature_latex(
        elemental_air,
        active_abilities=[],
    ))

    ram_animus = sample_monsters['ram_animus']
    monsters.append(get_creature_latex(
        ram_animus,
        active_abilities=[
            active_ability('Forceful Smash', f"""
                The ram makes a slam strike.
                In addition to the strike's normal effects, compare the attack result against the target's Fortitude defense.
                \\hit The target moves up to 10 feet in a direction of the ram's choice, as the \\textit<shove> ability (see \\pcref<Shove>).
                The ram does not have to move with the target to push it back.
            """),
        ],
    ))

    return '\n\n'.join(monsters)

def humanoids(sample_monsters):
    monsters = []

    cultist = sample_monsters['cultist']
    monsters.append(get_creature_latex(
        cultist,
        active_abilities=[
            active_ability('Hex', f"""
                The cultist makes a +{cultist.accuracy()} vs. Fortitude attack against one creature in Medium range.
                \hit The target takes {cultist.standard_damage() + 1} life damage and is \\glossterm<sickened> as a \\glossterm<condition>.",
            """),
        ],
    ))

    goblin_shouter = sample_monsters['goblin_shouter']
    monsters.append(get_creature_latex(
        goblin_shouter,
        active_abilities=[
            active_ability('Shout of Running', """
                The shouter chooses any number of willing creatures other than itself who can hear it.
                Each target does not have to spend \\glossterm<action points> to use use the \\textit<sprint> ability.
            """, tags=['Sustain (standard)']),
            active_ability('Shout of Stabbing', """
                The shouter chooses any number of willing creatures other than itself who can hear it.
                Each target gains a +1d bonus to damage with \\glossterm<strikes>.
            """, tags=['Sustain (standard)']),
        ],
        behavior='Attack lowest threat',
    ))

    goblin_stabber = sample_monsters['goblin_stabber']
    monsters.append(get_creature_latex(
        goblin_stabber,
        active_abilities=[
            active_ability('Sneeky Stab', f"""
                The stabber makes a shortsword strike.
                If the target is defenseless, overwhelmed, or unaware, the damage becomes {goblin_stabber.weapon_damage(Weapon('shortsword')) + 2}.
            """),
        ],
        behavior='Attack lowest threat',
    ))

    orc_chieftain = sample_monsters['orc_chieftain']
    monsters.append(get_creature_latex(
        orc_chieftain,
        active_abilities=[
            active_ability('Hit Everyone Else', """
                The chieftain chooses any number of willing creatures other than itself who can hear it.
                Each target gains a +2 bonus to \\glossterm<accuracy> with \\glossterm<strikes>.
            """, tags=['Sustain (standard)']),
            active_ability('Hit Hardest', f"""
                The chieftain makes a greataxe strike.
                The strike deals {orc_chieftain.weapon_damage(Weapon('greataxe')) + 2} damage.
            """),
            active_ability('Hit Fast', f"""
                The chieftain makes a greataxe strike.
                Its accuracy is increased to {orc_chieftain.accuracy('perception') + 2}.
            """),
        ],
    ))

    orc_grunt = sample_monsters['orc_grunt']
    monsters.append(get_creature_latex(
        orc_grunt,
        active_abilities=[
            active_ability('Hit Harder', f"""
                The grunt makes a greataxe strike.
                Its accuracy is reduced to {orc_grunt.accuracy('perception') - 2}, but the strike deals {orc_grunt.weapon_damage(Weapon('greataxe')) + 2} damage.
            """),
        ],
    ))

    orc_loudmouth = sample_monsters['orc_loudmouth']
    monsters.append(get_creature_latex(
        orc_loudmouth,
        active_abilities=[
            active_ability('Hit Harder', f"""
                The loudmouth makes a greataxe strike.
                Its accuracy is reduced to {orc_loudmouth.accuracy('perception') - 2}, but the strike deals {orc_loudmouth.weapon_damage(Weapon('greataxe')) + 2} damage.
            """),
            active_ability('Hit That One Over There', """
                The loudmouth chooses any number of willing creatures other than itself who can hear it.
                In addition, it chooses an enemy within Long range.
                Each target gains a +2 bonus to accuracy with strikes against the chosen enemy.
            """, tags=['Sustain (standard)']),
        ],
    ))

    orc_shaman = sample_monsters['orc_shaman']
    monsters.append(get_creature_latex(
        orc_shaman,
        active_abilities=[
            active_ability('Hit Worse', f"""
                The shaman makes a +{orc_shaman.accuracy()} vs. Mental attack against one creature in Close range.
                \\hit The target takes a -3 penalty to accuracy with strikes as a \\glossterm<condition>.
                \\crit As above, except that the penalty is increased to -6.
            """),
            active_ability('Hurt Less', f"""
                One other willing creature in Close range heals {orc_shaman.standard_damage() + 2} hit points.
            """),
        ],
    ))

    orc_savage = sample_monsters['orc_savage']
    monsters.append(get_creature_latex(
        orc_savage,
        active_abilities=[
            active_ability('Hit Fast', f"""
                The savage makes a greataxe strike.
                Its accuracy is {orc_savage.accuracy('perception') + 2}.
            """),
        ],
    ))

    return '\n\n'.join(monsters)


def magical_beasts(sample_monsters):
    monsters = []

    large_red_dragon = sample_monsters['large_red_dragon']
    monsters.append(get_creature_latex(
        large_red_dragon,
    ))

    ankheg = sample_monsters['ankheg']
    monsters.append(get_creature_latex(
        ankheg,
        active_abilities=[
            active_ability('Drag Prey', f"""
                This ability functions like the \\textit<shove> ability (see \\pcref<Shove>), except that the ankheg's accuracy is +{ankheg.accuracy() + 5}.
                In addition, the ankheg can move with the target up to a maximum distance equal to its \\glossterm<base speed>.
            """),
            active_ability('Spit Acid', f"""
                The ankheg makes a +{ankheg.accuracy()} vs. Armor attack against everything in a 5 ft. wide Medium line.
                \\hit Each target takes {ankheg.standard_damage()} acid damage, and creatures are \\glossterm<sickened> as a \\glossterm<condition>.
            """),
        ]
    ))

    aranea = sample_monsters['aranea']
    monsters.append(get_creature_latex(
        aranea,
        active_abilities=[
            # Is this how shapeshifting should work?
            active_ability('Shapeshift', """
                The aranea makes a Disguise check to change its appearance.
                It ignores all penalties for differences between its natural appearance and its intended appearance.
            """),
        ]
    ))

    basilisk = sample_monsters['basilisk']
    monsters.append(get_creature_latex(
        basilisk,
        active_abilities=[
            active_ability('Petrifying Gaze', f"""
                The basilisk makes a +{basilisk.accuracy()} vs. Fortitude attack against one creature in Medium range.
                \\hit The target is \\glossterm<nauseated> as a \\glossterm<condition>.
                \\crit As above, and as an additional condition, the target takes {basilisk.standard_damage() - 1} physical damage at the end of each action phase.
                If it takes vital damage in this way, it is petrified permanently.
            """),
        ],
    ))

    behir = sample_monsters['behir']
    monsters.append(get_creature_latex(
        behir,
        active_abilities=[
            active_ability('Electric Breath', f"""
                The behir makes a +{behir.accuracy()} vs. Armor attack against everything in a \\areamed cone.
                \\hit Each target takes {behir.standard_damage() + 1} electricity damage, and is \\glossterm<dazed> as a \\glossterm<condition>.
            """),
            active_ability('Natural Grab', f"""
                The behir makes a bite \\glossterm<strike>.
                In addition to the effects of the strike, it also makes a +{behir.accuracy('perception')+4} vs. Fortitude and Reflex attack against the same target.
                \\hit The target is \\glossterm<grappled> by the behir.
            """),
            active_ability('Rake', f"""
                The behir makes four claw \\glossterm<strikes> against a target that is \\glossterm<grappled> by it.
            """, ap_cost=True),
        ],
    ))

    blink_dog = sample_monsters['blink_dog']
    monsters.append(get_creature_latex(
        blink_dog,
        active_abilities=[
            active_ability('Blink', f"""
                As a \\glossterm<move action>, the blink dog can use this ability.
                If it does, it teleports to an unoccupied location within Medium range.
            """),
        ],
    ))

    centaur = sample_monsters['centaur']
    monsters.append(get_creature_latex(
        centaur,
    ))

    cockatrice = sample_monsters['cockatrice']
    monsters.append(get_creature_latex(
        cockatrice,
        active_abilities=[
            active_ability('Petrifying Bite', f"""
                The cockatrice makes a bite \\glossterm<strike>.
                In addition to the strike's normal effects, the cockatrice also makes a +{cockatrice.accuracy()} vs. Fortitude attack against the target.
                \\hit If the strike also hit, the target is \\glossterm<nauseated> as a \\glossterm<condition>.
                \\crit As above, and as an additional condition, the target takes {cockatrice.standard_damage() - 1} physical damage at the end of each action phase.
                If it takes vital damage in this way, it is petrified permanently.
            """),
        ],
    ))

    darkmantle = sample_monsters['darkmantle']
    monsters.append(get_creature_latex(
        darkmantle,
        active_abilities=[
            active_ability('Natural Grab', f"""
                The darkmantle makes a slam \\glossterm<strike>.
                In addition to the effects of the strike, it also makes a +{darkmantle.accuracy('perception') - 2} vs. Fortitude and Reflex attack against the same target.
                \\hit The target is \\glossterm<grappled> by the darkmantle.
            """),
        ],
    ))

    frost_worm = sample_monsters['frost_worm']
    monsters.append(get_creature_latex(
        frost_worm,
        immunities=['cold'],
        active_abilities=[
            active_ability('Frost Breath', f"""
                The frost worm makes a +{frost_worm.accuracy()} vs. Fortitude attack against everything in a \\arealarge cone from it.
                \\hit Each target takes {frost_worm.standard_damage() + 2} cold damage.
            """, tags=['Cold']),
            active_ability('Trill', f"""
                The frost worm emits a piercing noise that compels prey to stay still.
                It makes a +{frost_worm.accuracy()} vs. Mental attack against creatures in a \\areahuge radius from it.
                This area can pass through solid objects, including the ground, but every 5 feet of solid obstacle counts as 20 feet of distance.
                \\hit Each target is \\glossterm<dazed> and \\glossterm<immobilized> as two separate \\glossterm<conditions>.
                \\crit Each target is \\glossterm<stunned> and \\glossterm<immobilized> as two separate \\glossterm<conditions>.
            """, tags=['Mind'], ap_cost=True),
        ],
        passive_abilities=[
            passive_ability('Bitter Cold', f"""
                The frost worm's bite and slam strikes deal cold damage in addition to their other damage types.
            """),
            passive_ability('Death Throes', f"""
                When a frost worm is killed, its corpse turns to ice and shatters in a violent explosion.
                It makes a +{frost_worm.accuracy()} vs. Fortitude attack against everything in a \\areahuge radius from it.
                \\hit Each target takes {frost_worm.standard_damage() + 4} cold and piercing damage.
            """),
        ],
    ))

    girallon = sample_monsters['girallon']
    monsters.append(get_creature_latex(
        girallon,
    ))

    griffin = sample_monsters['griffin']
    monsters.append(get_creature_latex(
        griffin,
        active_abilities=[
            active_ability('Flyby Attack', """
                The griffin flies up to its flying movement speed.
                It can make a talon strike at any point during this movement.
            """),
        ],
        speed="80 ft. fly",
    ))

    hydra5 = sample_monsters['hydra5']
    monsters.append(get_creature_latex(
        hydra5,
        actions='Five in action phase',
        passive_abilities=[
            passive_ability('Multi-Headed', f"""
                A hydra can take a number of actions in each \\glossterm<action phase> equal to the number of heads it has active.
                At the end of each action phase, if the hydra took at least {trunc_to_five(hydra5.hit_points // 5)} damage during that phase, it loses one of its heads.
                Severed heads leave behind a stump that can quickly grow new heads.

                At the end of each delayed action phase, if the hydra has a severed stump, the stump is either sealed or it grows two new heads.
                If the hydra took {trunc_to_five(hydra5.hit_points // 10)} acid, cold, or fire damage during that phase, the stump is sealed, and will stop growing new heads.
                Otherwise, the hydra grows two new heads from the stump.
                This grants it additional actions during the action phase as normal.

                A hydra cannot sustain too many excess heads for a prolonged period of time.
                At the end of each round, if the hydra has more heads than twice its normal head count, it loses an action point.
                If it has no action points remaining, the hydra collapses unconscious for 8 hours.
                During that time, the excess heads shrivel and die, and any sealed stumps heal, restoring the hydra to its normal head count.
            """),
        ]
    ))

    hydra6 = sample_monsters['hydra6']
    monsters.append(get_creature_latex(
        hydra6,
        actions='Six in action phase',
        passive_abilities=[
            passive_ability('Multi-Headed', f"""
                A hydra can take a number of actions in each \\glossterm<action phase> equal to the number of heads it has active.
                At the end of each action phase, if the hydra took at least {trunc_to_five(hydra6.hit_points // 5)} damage during that phase, it loses one of its heads.
                Severed heads leave behind a stump that can quickly grow new heads.

                At the end of each delayed action phase, if the hydra has a severed stump, the stump is either sealed or it grows two new heads.
                If the hydra took {trunc_to_five(hydra6.hit_points // 10)} acid, cold, or fire damage during that phase, the stump is sealed, and will stop growing new heads.
                Otherwise, the hydra grows two new heads from the stump.
                This grants it additional actions during the action phase as normal.

                A hydra cannot sustain too many excess heads for a prolonged period of time.
                At the end of each round, if the hydra has more heads than twice its normal head count, it loses an action point.
                If it has no action points remaining, the hydra collapses unconscious for 8 hours.
                During that time, the excess heads shrivel and die, and any sealed stumps heal, restoring the hydra to its normal head count.
            """),
        ]
    ))

    minotaur = sample_monsters['minotaur']
    monsters.append(get_creature_latex(
        minotaur,
        active_abilities=[
            active_ability('Impaling Charge', f"""
                The minotaur moves up to its speed in a single straight line.
                If it uses this ability during the \\glossterm<action phase>, it can make a gore \\glossterm<strike> from its new location during the \\glossterm<delayed action phase>.
            """),
        ],
        passive_abilities=[
            passive_ability('Labyrinth Dweller', f"""
                The minotaur never gets lost or loses track of its current location.
            """)
        ],
    ))

    thaumavore = sample_monsters['thaumavore']
    monsters.append(get_creature_latex(
        thaumavore,
        passive_abilities=[
            passive_ability('Consume Magic', f"""
                The thaumavore gains a +4 bonus to \\glossterm<defenses> against \\glossterm<magical> abilities.
                Whenever it resists a \\glossterm<magical> attack, it heals hit points equal to twice the \\glossterm<power> of the effect.
            """),
            passive_ability('Sense Magic', f"""
                The thaumavore can sense the location of all sources of magic within 100 feet of it.
                This includes magic items, attuned magical abilities, and so on.
            """)
        ],
        behavior='Attack highest threat that has a source of magic; if no souces of magic exist, attack highest threat',
    ))

    banehound = sample_monsters['banehound']
    monsters.append(get_creature_latex(
        banehound,
    ))

    return '\n\n'.join(monsters)


def monstrous_humanoids(sample_monsters):
    monsters = []

    banshee = sample_monsters['banshee']
    monsters.append(get_creature_latex(
        banshee,
        active_abilities=[
            active_ability('Wail', f"""
                The banshee makes a +{banshee.accuracy()} vs. Fortitude attack against everything in a Large radius.
                \\hit Each target takes {banshee.standard_damage()} sonic damage, and creatures are sickened as a condition.
            """),
        ],
    ))

    hill_giant = sample_monsters['hill_giant']
    monsters.append(get_creature_latex(
        hill_giant,
        active_abilities=[
            active_ability('Boulder Toss', """
                The giant makes a ranged boulder strike, treating it as a thrown weapon with a 100 ft.\\ range increment.
            """),
        ],
    ))

    stone_giant = sample_monsters['stone_giant']
    monsters.append(get_creature_latex(
        stone_giant,
        active_abilities=[
            active_ability('Boulder Toss', """
                The giant makes a ranged boulder strike, treating it as a thrown weapon with a 100 ft.\\ range increment.
            """),
        ],
    ))

    storm_giant = sample_monsters['storm_giant']
    monsters.append(get_creature_latex(
        storm_giant,
        active_abilities=[
            active_ability('Lightning Javelin', f"""
                The storm giant makes a +{storm_giant.accuracy()} vs. Fortitude attack against everything in a 10 ft. wide Large line.
                \\hit Each target takes {storm_giant.standard_damage() + 2} electricity damage.
            """),
            active_ability('Thunderstrike', f"""
                The storm giant makes a greatsword strike against a target.
                If its attack result beats the target's Fortitude defense,
                    the target also takes {storm_giant.standard_damage()} sonic damage
                    and is deafened as a condition.
            """),
        ],
        immunities=['deafened'],
    ))

    green_hag = sample_monsters['green_hag']
    monsters.append(get_creature_latex(
        green_hag,
        active_abilities=[
            active_ability('Vital Surge', f"""
                The hag makes a +{green_hag.accuracy()} vs. Fortitude attack against one creature within Medium range.
                \\hit The target takes {green_hag.standard_damage() + 2} life damage.
            """),
            active_ability("Green Hag's Curse", f"""
                The hag makes a +{green_hag.accuracy()} vs. Mental atack aginst one creature within Medium range.
                \\hit As a condition, the target is either dazed, fatigued, or sickened, as the hag chooses.
                \\crit As three separate conditions, the target is dazed, fatigued, and sickened.
            """),
        ],
        passive_abilities=[
            passive_ability('Coven Rituals', """
                When three or more hags work together, they form a coven.
                All members of the coven gain the ability to perform nature rituals as long as they work together.
                Hags of any type can form a coven together.
            """),
        ],
    ))

    medusa = sample_monsters['medusa']
    monsters.append(get_creature_latex(
        medusa,
        active_abilities=[
            active_ability('Petrifying Gaze', f"""
                The medusa makes a +{medusa.accuracy()} vs. Fortitude attack against one creature in Medium range.
                \\hit The target is \\glossterm<nauseated> as a \\glossterm<condition>.
                \\crit As above, and as an additional condition, the target takes {medusa.standard_damage() - 1} physical damage at the end of each action phase.
                If it takes vital damage in this way, it is petrified permanently.
            """),
        ],
    ))

    return '\n\n'.join(monsters)


def outsiders(sample_monsters):
    monsters = []

    astral_deva = sample_monsters['astral_deva']
    monsters.append(get_creature_latex(
        astral_deva,
        active_abilities=[
            active_ability('Smite', """
                The angel makes a mace strike.
                If its target is evil, it gains a +2 bonus to accuracy and a +2d bonus to damage on the strike.
            """),
            active_ability("Angel's Grace", f"""
                One willing creature within reach heals {astral_deva.standard_damage() + 3} hit points.
            """),
        ],
    ))

    arrowhawk = sample_monsters['arrowhawk']
    monsters.append(get_creature_latex(
        arrowhawk,
        active_abilities=[
            active_ability('Electrobolt', f"""
                The arrowhawk makes a +{arrowhawk.accuracy()} vs. Fortitude attack against one creature or object in Medium range.
                \\hit The target takes {arrowhawk.standard_damage() + 2} electricity damage.
            """),
        ],
        speed='60 ft. fly (good)',
        behavior='Attack lowest threat',
    ))

    bebelith = sample_monsters['bebelith']
    monsters.append(get_creature_latex(
        bebelith,
        active_abilities=[
            active_ability('Venomous Bite', f"""
                The bebelith makes a bite strike.
                If it hits, and the attack result beats the target's Fortitude defense, the target is also poisoned as a condition.
                If the target is poisoned, it takes {bebelith.standard_damage()} poison damage at the end of each action phase after the first round.
            """),
        ],
    ))

    hell_hound = sample_monsters['hell_hound']
    monsters.append(get_creature_latex(
        hell_hound,
        active_abilities=[
            active_ability('Fire Breath', f"""
                The hell hound makes a +{hell_hound.accuracy()} vs. Armor attack against everything in a Medium cone.
                \\hit Each target takes {hell_hound.standard_damage() + 1} fire damage.
            """),
        ],
        immunities=['fire damage'],
    ))

    flamebrother_salamander = sample_monsters['flamebrother_salamander']
    monsters.append(get_creature_latex(
        flamebrother_salamander,
        active_abilities=[
            active_ability('Flame Aura', f"""
                The salamander intensifies its natural body heat, creating a burning aura around it.
                At the end of each action phase, the salamander makes a +{flamebrother_salamander.accuracy()} vs. Armor
                    attack against everything within a Medium radius emanation of it.
                \\hit Each target takes {flamebrother_salamander.standard_damage()} fire damage.
            """, tags=['Sustain (standard)'], ap_cost=True),
            active_ability('Natural Grab', f"""
                The salamander makes a tail slam \\glossterm<strike>.
                In addition to the effects of the strike, it also makes a +{flamebrother_salamander.accuracy('perception')} vs. Fortitude and Reflex attack against the same target.
                \\hit The target is \\glossterm<grappled> by the salamander.
            """),
        ],
        immunities=['fire damage'],
    ))

    janni = sample_monsters['janni']
    monsters.append(get_creature_latex(
        janni,
    ))

    salamander_battlemaster = sample_monsters['salamander_battlemaster']
    monsters.append(get_creature_latex(
        salamander_battlemaster,
        active_abilities=[
            active_ability('Flame Aura', f"""
                The salamander intensifies its natural body heat, creating a burning aura around it.
                At the end of each action phase, the salamander makes a +{flamebrother_salamander.accuracy()} vs. Armor
                    attack against everything within a Medium radius emanation of it.
                \\hit Each target takes {flamebrother_salamander.standard_damage()} fire damage.
            """, tags=['Sustain (standard)'], ap_cost=True),
            active_ability('Natural Grab', f"""
                The salamander makes a tail slam \\glossterm<strike>.
                In addition to the effects of the strike, it also makes a +{salamander_battlemaster.accuracy('perception')} vs. Fortitude and Reflex attack against the same target.
                \\hit The target is \\glossterm<grappled> by the salamander.
            """),
        ],
    ))

    return '\n\n'.join(monsters)


def undead(sample_monsters):
    monsters = []

    allip = sample_monsters['allip']
    monsters.append(get_creature_latex(
        allip,
    ))

    spectre = sample_monsters['spectre']
    monsters.append(get_creature_latex(
        spectre,
    ))

    dirgewalker = sample_monsters['dirgewalker']
    monsters.append(get_creature_latex(
        dirgewalker,
        active_abilities=[
            active_ability('Animating Caper', """
                One corpse within Close range is animated as a skeleton under the dirgewalker's control.
            """, tags=['Attune (self)']),
            active_ability('Mournful Dirge', f"""
                The dirgewalker makes a +{dirgewalker.accuracy()} vs. Mental attack against all creatures in a Medium radius.
                \\hit Each target is dazed as a condition.
                \\crit Each target is stunned as a condition.
            """),
        ],
    ))

    skeleton = sample_monsters['skeleton']
    monsters.append(get_creature_latex(
        skeleton,
    ))

    skeleton_warrior = sample_monsters['skeleton_warrior']
    monsters.append(get_creature_latex(
        skeleton_warrior,
    ))

    zombie = sample_monsters['zombie']
    monsters.append(get_creature_latex(
        zombie,
        # TODO: this creature acts during the delayed action phase
    ))

    return '\n\n'.join(monsters)


def generate_monsters():
    sample_monsters = get_sample_creatures()['monsters']
    monsters = f"""
        \\section<Aberrations>
        {aberrations(sample_monsters)}

        \\section<Animates>
        {animates(sample_monsters)}

        \\section<Animals>
        {animals(sample_monsters)}

        \\section<Humanoids>
        {humanoids(sample_monsters)}

        \\section<Magical Beasts>
        {magical_beasts(sample_monsters)}

        \\section<Monstrous Humanoids>
        {monstrous_humanoids(sample_monsters)}

        \\section<Outsiders>
        {outsiders(sample_monsters)}

        \\section<Undead>
        {undead(sample_monsters)}
    """

    return monsters


def sanity_check(monsters):
    pass


# This is an incredibly trivial function, but it matches the style of the
# other files in this directory
def generate_monster_latex():
    return latexify(generate_monsters())


def write_to_file():
    monster_latex = generate_monster_latex()
    with open(book_path('monster_descriptions.tex'), 'w') as file:
        file.write(monster_latex)


@click.command()
@click.option('-c', '--check/--no-check', default=False)
@click.option('-o', '--output/--no-output', default=False)
def main(output, check):
    if output:
        write_to_file()
    else:
        print(generate_monster_latex())


if __name__ == "__main__":
    main()
