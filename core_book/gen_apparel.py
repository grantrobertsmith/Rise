#!/usr/bin/env python3

import click
from generation.magic_item import MagicItem
from generation.util import latexify

def generate_armor():
    apparel = []

    apparel.append(MagicItem(
        name='Shield of Arrow Catching',
        level=5,
        material_type='shield',
        tags=['Telekinesis'],
        description="""
            Whenever a creature within a \\areamed radius emanation from you would be attacked by a ranged weapon, the attack is redirected to target you instead.
            Resolve the attack as if it had initially targeted you, except that the attack is not affected by cover or concealment.
            This item can only affect projectiles and thrown objects that are Small or smaller.
        """,
        short_description="Redirects small nearby projectiles to hit you",
    ))

    apparel.append(MagicItem(
        name='Shield of Arrow Catching, Greater',
        level=10,
        tags=['Telekinesis'],
        material_type='shield',
        description="""
            This item functions like the \\mitem<shield of arrow catching> item, except that it affects a \\arealarge radius from you.
            In addition, you may choose to exclude creature from this item's effect, allowing projectiles to target nearby foes normally.
        """,
        short_description="Selectively redirects small nearby projectiles to hit you",
    ))

    apparel.append(MagicItem(
        name='Shield of Boulder Catching',
        level=8,
        tags=['Telekinesis'],
        material_type='shield',
        description="""
            This item functions like the \\mitem<shield of arrow catching> item, except that it can affect projectile and thrown objects of up to Large size.
        """,
        short_description="Redirects large nearby projectiles to hit you",
    ))

    apparel.append(MagicItem(
        name="Shield of Arrow Deflection",
        level=2,
        tags=['Telekinesis'],
        material_type='shield',
        description="""
            As an \\glossterm<immediate action> when you are attacked by a ranged \\glossterm<strike>, you can use this item.
            If you do, you gain a +5 bonus to Armor defense against the attack.
            You must be aware of the attack to deflect it in this way.
            This item can only affect projectiles and thrown objects that are Small or smaller.
        """,
        short_description="React to block small projectiles",
    ))

    apparel.append(MagicItem(
        name="Shield of Arrow Deflection, Greater",
        level=12,
        tags=['Telekinesis'],
        material_type='shield',
        description="""
            This item functions like the \\mitem<shield of arrow deflection> item, except that the defense bonus increases to +10.
        """,
        short_description="React to completely block small projectiles",
    ))

    apparel.append(MagicItem(
        name="Shield of Boulder Deflection",
        level=6,
        tags=['Telekinesis'],
        material_type='shield',
        description="""
            This item functions like the \\mitem<shield of arrow deflection> item, except that it can affect projectiles and thrown objects of up to Large size.
        """,
        short_description="React to block large projectiles",
    ))

    apparel.append(MagicItem(
        name="Shield of Bashing",
        level=2,
        tags=['Enhancement'],
        material_type='shield',
        description="""
            % Should this be strike damage?
            You gain a +1d bonus to damage with \\glossterm<physical attacks> using this shield.
        """,
        short_description="Deals +1d damage",
    ))

    apparel.append(MagicItem(
        name="Shield of Bashing, Greater",
        level=11,
        tags=['Enhancement'],
        material_type='shield',
        description="""
            % Should this be strike damage?
            You gain a +2d bonus to damage with \\glossterm<physical attacks> using this shield.
        """,
        short_description="Deals +2d damage",
    ))

    apparel.append(MagicItem(
        name="Armor of Energy Resistance",
        level=4,
        tags=['Shielding'],
        material_type='body armor',
        description="""
            You have \\glossterm<damage reduction> equal to the item's \\glossterm<power> against \\glossterm<energy damage>.
            Whenever you resist energy with this item, it sheds light as a torch until the end of the next round.
            The color of the light depends on the energy damage resisted: blue for cold, yellow for electricity, red for fire, and brown for sonic.
        """,
        short_description="Reduces energy damage",
    ))

    apparel.append(MagicItem(
        name="Armor of Energy Resistance, Greater",
        level=12,
        tags=['Shielding'],
        material_type='body armor',
        description="""
            This item functions like the \\mitem<armor of energy resistance> item, except that the damage reduction is equal to twice the item's \\glossterm<power>.
        """,
        short_description="Drastically reduces energy damage",
    ))

    apparel.append(MagicItem(
        name="Featherlight Armor",
        level=4,
        tags=['Enhancement'],
        material_type='body armor',
        description="""
            This armor's \\glossterm<encumbrance penalty> is reduced by 2.
        """,
        short_description="Reduces encumbrance penalty by 2",
    ))

    apparel.append(MagicItem(
        name="Featherlight Armor, Greater",
        level=10,
        tags=['Enhancement'],
        material_type='body armor',
        description="""
            This armor's \\glossterm<encumbrance penalty> is reduced by 4.
        """,
        short_description="Reduces encumbrance penalty by 4",
    ))

    apparel.append(MagicItem(
        name="Armor of Fortification",
        level=7,
        tags=['Imbuement'],
        material_type='body armor',
        description="""
            You gain a +5 bonus to defenses when determining whether a \\glossterm<strike> gets a \\glossterm<critical hit> against you instead of a normal hit.
        """,
        short_description="Reduces critical hits from strikes",
    ))

    apparel.append(MagicItem(
        name="Armor of Fortification, Greater",
        level=15,
        tags=['Imbuement'],
        material_type='body armor',
        description="""
            This item functions like the \\mitem<armor of fortification> item, except that the bonus increases to +10.
        """,
        short_description="Drastically reduces critical hits from strikes",
    ))

    apparel.append(MagicItem(
        name="Armor of Fortification, Mystic",
        level=12,
        tags=['Imbuement'],
        material_type='body armor',
        description="""
            This item functions like the \\mitem<armor of fortification> item, except that it applies against all attacks instead of only against; \\glossterm<strikes>.
        """,
        short_description="Reduces critical hits from all attacks",
    ))

    apparel.append(MagicItem(
        name="Hidden Armor",
        level=4,
        tags=['Glamer'],
        material_type='body armor',
        description="""
             As a standard action, you can use this item.
             If you do, it appears to change shape and form to assume the shape of a normal set of clothing.
             You may choose the design of the clothing.
             The item retains all of its properties, including weight and sound, while disguised in this way.
             Only its visual appearance is altered.

             Alternately, you may return the armor to its original appearance.
        """,
        short_description="Can look like normal clothing",
    ))

    apparel.append(MagicItem(
        name="Hidden Armor, Greater",
        level=9,
        material_type='body armor',
        tags=['Alteration'],
        description="""
            This item functions like the \\mitem<hidden armor> item, except that the item also makes sound appropriate to its disguised form while disguised.
        """,
        short_description="Can look and sound like normal clothing",
    ))

    apparel.append(MagicItem(
        name="Armor of Invulnerability",
        level=8,
        tags=['Shielding'],
        material_type='body armor',
        description="""
            You have \\glossterm<damage reduction> equal to this item's \\glossterm<power> against damage from \\glossterm<physical attacks>.
        """,
        short_description="Reduces damage from physical attacks",
    ))

    apparel.append(MagicItem(
        name="Armor of Invulnerability, Greater",
        level=16,
        tags=['Shielding'],
        material_type='body armor',
        description="""
            This item functions like the \\mitem<armor of invulnerability> item, except that the damage reduction is equal to twice the item's \\glossterm<power>.
            You have \\glossterm<damage reduction> equal to the item's \\glossterm<power> against damage from \\glossterm<physical attacks>.
        """,
        short_description="Drastically reduces damage from physical attacks",
    ))

    apparel.append(MagicItem(
        name="Armor of Magic Resistance",
        level=14,
        tags=['Shielding'],
        material_type='body armor',
        description="""
            You have \\glossterm<magic resistance> equal to 5 + the item's \\glossterm<power>.
        """,
        short_description="Provides magic resistance",
    ))

    apparel.append(MagicItem(
        name="Shield of Mystic Reflection",
        level=12,
        tags=['Thaumaturgy'],
        material_type='shield',
        description="""
            As an \\glossterm<immediate action> when you are targeted by a targeted \\glossterm<magical> ability, you can spend an \\glossterm<action point> to use this ability.
            If you do, the ability targets the creature using the ability instead of you.
            Any other targets of the ability are affected normally.
        """,
        short_description="React to reflect magical attacks",
    ))

    return apparel

def generate_worn():
    apparel = []

    apparel.append(MagicItem(
        name="Bracers of Archery",
        level=1,
        material_type='bracer',
        tags=['Enhancement'],
        description="""
            You are proficient with bows.
        """,
        short_description="Grants proficiency with bows",
    ))

    apparel.append(MagicItem(
        name="Bracers of Armor",
        level=2,
        material_type='bracer',
        tags=['Shielding'],
        description="""
            You gain a +2 bonus to Armor defense.
            The protection from these bracers is treated as body armor, and it does not stack with any other body armor you wear.
        """,
        short_description="Grants invisible armor",
    ))

    apparel.append(MagicItem(
        name="Bracers of Repulsion",
        level=4,
        material_type='bracer',
        tags=['Telekinesis'],
        description="""
            Whenever a creature hits you with a melee \\glossterm<strike> during the \\glossterm<action phase>,
                you can spend an \\glossterm<action point> to use this item as an \\glossterm<immediate action>.
            If you do, you make a \\glossterm<shove> attack against that creature during the \\glossterm<delayed action phase>, using this item's power in place of your Strength.
        """,
        short_description="React to shove a foe that struck you",
    ))

    apparel.append(MagicItem(
        name="Bracers of Repulsion, Greater",
        level=11,
        material_type='bracer',
        tags=['Telekinesis'],
        description="""
            This item functions like the \\mitem<bracers of repulsion> item, except that it does not cost an action point to use.
        """,
        short_description="React freely to shove a foe that struck you",
    ))

    apparel.append(MagicItem(
        name="Torchlight Gloves",
        level=2,
        material_type='glove',
        tags=['Figment', 'Light'],
        description="""
            These gloves shed light as a torch.
            As a \\glossterm<standard action>, you may choose to suppress or resume the light from either or both gloves.
        """,
        short_description="Sheds light as a torch",
    ))

    apparel.append(MagicItem(
        name="Gauntlets of Improvisation",
        level=2,
        material_type='gauntlet',
        tags=['Enhancement'],
        description="""
            You gain a +1d bonus to damage with \\glossterm<improvised weapons>.
        """,
        short_description="Grants +1d damage with improvised weapons",
    ))

    apparel.append(MagicItem(
        name="Gauntlets of Improvisation, Greater",
        level=7,
        material_type='gauntlet',
        tags=['Enhancement'],
        description="""
            This item functions like the \\mitem<gauntlets of improvisation>, except that the damage bonus is increased to +2d.
        """,
        short_description="Grants +2d damage with improvised weapons",
    ))

    apparel.append(MagicItem(
        name="Gauntlet of the Ram",
        level=2,
        material_type='gauntlet',
        tags=['Telekinesis'],
        description="""
            If you hit on a \\glossterm<strike> with this gauntlet during the \\glossterm<action phse>, you can attempt to \\glossterm<shove> your foe during the \\glossterm<delayed action phase>.
            Making a strike with this gauntlet is equivalent to an \\glossterm<unarmed attack>.
            You do not need to move with your foe to push it back the full distance.
        """,
        short_description="Shoves foe when use to strike",
    ))

    apparel.append(MagicItem(
        name="Gauntlet of the Ram, Greater",
        level=7,
        material_type='gauntlet',
        tags=['Telekinesis'],
        description="""
            This item functions like the \\mitem<gauntlet of the ram>, except that you gain a bonus to the \\glossterm<shove> attack equal to the damage you dealt with the \\glossterm<strike>.
        """,
        short_description="Shoves foe hard when use to strike",
    ))

    apparel.append(MagicItem(
        name="Greatreach Bracers",
        level=9,
        material_type='bracer',
        tags=['Imbuement'],
        description="""
            Your \\glossterm<reach> is increased by 5 feet.
        """,
        short_description="Increases reach by five feet",
    ))

    apparel.append(MagicItem(
        name="Greatreach Bracers, Greater",
        level=17,
        material_type='bracer',
        tags=['Imbuement'],
        description="""
            Your \\glossterm<reach> is increased by 10 feet.
        """,
        short_description="Increases reach by ten feet",
    ))

    apparel.append(MagicItem(
        name="Throwing Gloves",
        level=4,
        material_type='glove',
        tags=['Enhancement'],
        description="""
            % TODO: reference basic "not designed to be thrown" mechanics?
            You can throw any item as if it was designed to be thrown.
            This does not improve your ability to throw items designed to be thrown, such as darts.
        """,
        short_description="Allows throwing any item accurately",
    ))

    apparel.append(MagicItem(
        name="Mask of Water Breathing",
        level=4,
        material_type='mask',
        tags=['Imbuement'],
        description="""
            You can breathe water through this mask as easily as a human breaths air.
            This does not grant you the ability to breathe other liquids.
        """,
        short_description="Allows breathing water like air",
    ))

    apparel.append(MagicItem(
        name="Mask of Air",
        level=9,
        material_type='mask',
        tags=['Imbuement'],
        description="""
            If you breathe through this mask, you breathe in clean, fresh air, regardless of your environment.
            This can protect you from inhaled poisons and similar effects.
        """,
        short_description="Allows breathing in any environment",
    ))

    apparel.append(MagicItem(
        name="Crown of Flame",
        level=5,
        material_type='crown',
        tags=['Fire'],
        description="""
            This crown is continuously on fire.
            The flame sheds light as a torch.

            You and all allies within an \\arealarge radius emanation from you are immune to fire damage.
        """,
        short_description="Grants nearby allies immunity to fire damage",
    ))

    apparel.append(MagicItem(
        name="Crown of Lightning",
        level=7,
        material_type='crown',
        tags=['Electricity'],
        description="""
            This crown continuously crackles with electricity.
            The constant sparks shed light as a torch.

            At the end of each \\glossterm<action phase>, you make a Power vs. Reflex attack against all enemies within an \\areamed radius emanation from you.
            A hit deals electricity \\glossterm<standard damage> -3d.
        """,
        short_description="Continuously damages nearby enemies",
    ))

    apparel.append(MagicItem(
        name="Crown of Frost",
        level=11,
        material_type='crown',
        tags=['Cold'],
        description="""
            At the end of each \\glossterm<action phase>, you make a Power vs. Fortitude attack against all enemies within an \\areamed radius emanation from you.
            A hit deals cold \\glossterm<standard damage> -3d.
            Each creature that takes damage in this way is \\fatigued until the end of the next round.
        """,
        short_description="Continuously damages and fatigues nearby enemies",
    ))

    apparel.append(MagicItem(
        name="Crown of Thunder",
        level=9,
        material_type='crown',
        tags=['Sonic'],
        description="""
            The crown constantly emits a low-pitched rumbling.
            To you and your allies, the sound is barely perceptible.
            However, all enemies within an \\arealarge radius emanation from you hear the sound as a deafening, continuous roll of thunder.
            The noise blocks out all other sounds quieter than thunder, causing them to be \\deafened while they remain in the area and until the end of the next round after they leave.
        """,
        short_description="Continously deafens nearby enemies",
    ))

    apparel.append(MagicItem(
        name="Boots of Earth's Embrace",
        level=4,
        material_type='boot',
        tags=['Earth', 'Enhancement'],
        description="""
            While you are standing on solid ground, you are immune to effects that would force you to move.
            This does not protect you from other effects of those attacks, such as damage.
        """,
        short_description="Grants immunity to forced movement",
    ))

    apparel.append(MagicItem(
        name="Boots of Freedom",
        level=6,
        material_type='boot',
        tags=['Imbuement'],
        description="""
            You are immune to effects that restrict your mobility.
            This removes all penalties you would suffer for acting underwater, except for those relating to using ranged weapons.
            This does not prevent you from being \\grappled, but you gain a +10 bonus to your defense against \\glossterm<grapple> attacks.
        """,
        short_description="Grants immunity to most mobility restrictions",
    ))

    apparel.append(MagicItem(
        name="Boots of Freedom, Greater",
        level=12,
        material_type='boot',
        tags=['Imbuement'],
        description="""
            These boots function like \\mitem<boots of freedom>, except that you are also immune to being \\grappled.
        """,
        short_description="Grants immunity to grappling and other mobility restrictions",
    ))

    apparel.append(MagicItem(
        name="Boots of Gravitation",
        level=8,
        material_type='boot',
        tags=['Imbuement'],
        description="""
            While these boots are within 5 feet of a solid surface, gravity pulls you towards the solid surface closest to your boots rather than in the normal direction.
            This can allow you to walk easily on walls or even ceilings.
        """,
        short_description="Redirects personal gravity",
    ))

    apparel.append(MagicItem(
        name="Boots of Speed",
        level=5,
        material_type='boot',
        tags=['Temporal'],
        description="""
            You gain a +10 foot bonus to your speed in all your movement modes, up to a maximum of double your normal speed.
        """,
        short_description="Increases speed by ten feet",
    ))

    apparel.append(MagicItem(
        name="Boots of Speed, Greater",
        level=13,
        material_type='boot',
        tags=['Temporal'],
        description="""
            You gain a +30 foot bonus to your speed in all your movement modes, up to a maximum of double your normal speed.
        """,
        short_description="Increases speed by thirty feet",
    ))

    apparel.append(MagicItem(
        name="Astral Boots",
        level=16,
        material_type='boot',
        tags=['Teleportation'],
        description="""
            Whenever you move, you can teleport the same distance instead.
            This does not change the total distance you can move, but you can teleport in any direction, even vertically.
            You cannot teleport to locations you do not have \\glossterm<line of sight> and \\glossterm<line of effect> to.
        """,
        short_description="Allows teleporting instead of moving",
    ))

    apparel.append(MagicItem(
        name="Boots of Water Walking",
        level=7,
        material_type='boot',
        tags=['Imbuement'],
        description="""
            You treat the surface of all liquids as if they were firm ground.
            Your feet hover about an inch above the liquid's surface, allowing you to traverse dangerous liquids without harm as long as the surface is calm.

            If you are below the surface of the liquid, you rise towards the surface at a rate of 60 feet per round.
            Thick liquids, such as mud and lava, may cause you to rise more slowly.
        """,
        short_description="Allows walking on liquids",
    ))

    apparel.append(MagicItem(
        name="Boots of the Winterlands",
        level=2,
        material_type='boot',
        tags=['Enhancement'],
        description="""
            You can travel across snow and ice without slipping or suffering movement penalties for the terrain.
            % TODO: degree symbol?
            In addition, the boots keep you warn, protecting you in environments as cold as -50 Fahrenheit.
        """,
        short_description="Eases travel in cold areas",
    ))

    apparel.append(MagicItem(
        name="Seven League Boots",
        level=12,
        material_type='boot',
        tags=['Teleportation'],
        description="""
            As a standard action, you can spend an \glossterm{action point} to use this item.
            If you do, you teleport exactly 25 miles in a direction you specify.
            If this would place you within a solid object or otherwise impossible space, the boots will shunt you up to 1,000 feet in any direction to the closest available space.
            If there is no available space within 1,000 feet of your intended destination, the effect fails and you take \\glossterm<standard damage> -1d.
        """,
        short_description="Teleport seven leages with a step",
    ))

    apparel.append(MagicItem(
        name="Winged Boots",
        level=10,
        material_type='boot',
        tags=['Imbuement'],
        description="""
            You gain a \\glossterm<fly speed> equal to your land speed.
            However, the boots are not strong enough to keep you aloft indefinitely.
            At the end of each round, if you are not standing on solid ground, the magic of the boots fails and you fall normally.
            The boots begin working again at the end of the next round, even if you have not yet hit the ground.
        """,
        short_description="Grants limited flight",
    ))

    apparel.append(MagicItem(
        name="Ring of Energy Resistance",
        level=6,
        material_type='ring',
        tags=['Shielding'],
        description="""
            You have \\glossterm<damage reduction> equal to the ring's \\glossterm<power> against \\glossterm<energy damage>.
            Whenever you resist energy with this ability, the ring sheds light as a torch until the end of the next round.
            The color of the light depends on the energy damage resisted: blue for cold, yellow for electricity, red for fire, and brown for sonic.
        """,
        short_description="Reduces energy damage",
    ))

    apparel.append(MagicItem(
        name="Ring of Energy Resistance, Greater",
        level=14,
        material_type='ring',
        tags=['Shielding'],
        description="""
            This item functions like the \\mitem<ring of energy resistance>, except that the damage reduction is equal to twice the item's \\glossterm<power>.
        """,
        short_description="Drastically reduces energy damage",
    ))

    apparel.append(MagicItem(
        name="Ring of Elemental Endurance",
        level=2,
        material_type='ring',
        tags=['Shielding'],
        description="""
            You can exist comfortably in conditions between -50 and 140 degrees Fahrenheit without any ill effects.
            You suffer the normal penalties in temperatures outside of that range.
        """,
        short_description="Grants tolerance of temperature extremes",
    ))

    apparel.append(MagicItem(
        name="Ring of Nourishment",
        level=3,
        material_type='ring',
        tags=['Creation'],
        description="""
            You continuously gain nourishment, and no longer need to eat or drink.
            This ring must be worn for 24 hours before it begins to work.
        """,
        short_description="Provides food and water",
    ))

    apparel.append(MagicItem(
        name="Ring of Sustenance",
        level=7,
        material_type='ring',
        tags=['Creation', 'Temporal'],
        description="""
            You continuously gain nourishment, and no longer need to eat or drink.
            In addition, you need only one-quarter your normal amount of sleep (or similar activity, such as elven trance) each day.

            The ring must be worn for 24 hours before it begins to work.
        """,
        short_description="Provides food, water, and rest",
    ))

    apparel.append(MagicItem(
        name="Ring of Protection",
        level=8,
        material_type='ring',
        tags=['Shielding'],
        description="""
            You gain a +1 bonus to Armor defense.
        """,
        short_description="Grants +1 Armor defense",
    ))

    apparel.append(MagicItem(
        name="Ring of Regeneration",
        level=11,
        material_type='ring',
        tags=['Life'],
        description="""
            At the end of each \\glossterm<action phase>, you heal hit points equal to this item's \\glossterm<power>.
            Only damage taken while wearing the ring can be healed in this way.
        """,
        short_description="Grants fast healing",
    ))

    apparel.append(MagicItem(
        name="Amulet of Mighty Fists",
        level=6,
        material_type='amulet',
        tags=['Enhancement'],
        description="""
            You gain a +1d bonus to \\glossterm<strike damage> with \\glossterm<unarmed attacks> and natural weapons.
        """,
        short_description="Grants +1d damage with your body",
    ))

    apparel.append(MagicItem(
        name="Amulet of Mighty Fists, Greater",
        level=14,
        material_type='amulet',
        tags=['Enhancement'],
        description="""
            You gain a +2d bonus to \\glossterm<strike damage> with \\glossterm<unarmed attacks> and natural weapons.
        """,
        short_description="Grants +2d damage with your body",
    ))

    apparel.append(MagicItem(
        name="Assassin's Cloak",
        level=7,
        material_type='cloak',
        tags=['Glamer'],
        description="""
            At the end of each round, if you took no actions that round, you become \\glossterm<invisible> until the end of the next round.
        """,
        short_description="Grants invisibility while inactive",
    ))

    apparel.append(MagicItem(
        name="Assassin's Cloak, Greater",
        level=17,
        material_type='cloak',
        tags=['Glamer'],
        description="""
            At the end of each round, if you did not attack a creature that round, you become \\glossterm<invisible> until the end of the next round.
        """,
        short_description="Grants invisibility while not attacking",
    ))

    apparel.append(MagicItem(
        name="Belt of Healing",
        level=1,
        material_type='belt',
        tags=['Life'],
        description="""
            When you use the \\textit<recover> action, you heal +1d hit points.
        """,
        short_description="Grants +1d healing from the \\textit<recover> action",
    ))

    apparel.append(MagicItem(
        name="Belt of Healing, Greater",
        level=8,
        material_type='belt',
        tags=['Life'],
        description="""
            When you use the \\textit<recover> action, you heal +2d hit points.
        """,
        short_description="Grants +2d healing from the \\textit<recover> action",
    ))

    apparel.append(MagicItem(
        name="Belt of Heroic Recovery",
        level=6,
        material_type='belt',
        tags=['Life'],
        description="""
            % TODO: timing?
            As an \\glossterm<immediate action> when you get a \\glossterm<critical hit>, you can take the \\textit<recover> action.
        """,
        short_description="React to heal after getting a critical hit",
    ))

    apparel.append(MagicItem(
        name="Cloak of Mist",
        level=8,
        material_type='cloak',
        tags=['Fog', 'Manifestation'],
        description="""
            Fog constantly fills an \\areamed radius emanation from you.
            This fog does not fully block sight, but it provides \\concealment.

            If a 5-foot square of fog takes fire damage equal to half this item's \\glossterm<power>, the fog disappears from that area until the end of the next round.
        """,
        short_description="Fills nearby area with fog",
    ))

    apparel.append(MagicItem(
        name="Cloak of Mist, Greater",
        level=16,
        material_type='cloak',
        tags=['Fog', 'Manifestation'],
        description="""
            A thick fog constantly fills an \\areamed radius emanation from you.
            This fog completely blocks sight beyond 10 feet.
            Within that range, it still provides \\concealment.

            If a 5-foot square of fog takes fire damage equal to this item's \\glossterm<power>, the fog disappears from that area until the end of the next round.
        """,
        short_description="Fills nearby area with thick fog",
    ))

    apparel.append(MagicItem(
        name="Vanishing Cloak",
        level=8,
        material_type='cloak',
        tags=['Glamer', 'Teleportation'],
        description="""
            As a standard action, you can spend an \glossterm{action point} to use this item.
            If you do, you teleport to an unoccupied location within \\rngmed range of your original location.
            In addition, you become \\glossterm<invisible> unitl the end of the next round.

            If your intended destination is invalid, or if your teleportation otherwise fails, you still become invisible.
        """,
        short_description="Can teleport a short distance and grant invisibility",
    ))

    apparel.append(MagicItem(
        name="Hexward Cloak",
        level=10,
        material_type='cloak',
        tags=['Thaumaturgy'],
        description="""
            You gain a +5 bonus to defenses against \\glossterm<magical> abilities that target you directly.
            This does not protect you from abilities that affect an area.
        """,
        short_description="Grants +5 defenses against targeted magical attacks",
    ))

    apparel.append(MagicItem(
        name="Hexproof Cloak",
        level=18,
        material_type='cloak',
        tags=['Thaumaturgy'],
        description="""
            All \\glossterm<magical> abilities that target you directly fail to affect you.
            This does not protect you from abilities that affect an area.
        """,
        short_description="Grants +10 defenses against targeted magical attacks",
    ))

    return apparel


def generate_apparel():
    return generate_armor() + generate_worn()


def generate_apparel_latex(check=False):
    apparel = sorted(generate_apparel(), key=lambda apparel: apparel.name)
    if check:
        sanity_check(apparel)

    texts = []
    for item in apparel:
        try:
            texts.append(item.latex())
        except Exception as e:
            raise Exception(f"Error converting item '{item.name}' to LaTeX") from e

    text = '\n'.join(texts)
    return latexify(text)


def generate_apparel_table():
    apparel = sorted(
        sorted(generate_apparel(), key=lambda item: item.name),
        key=lambda item: item.level
    )
    rows = [
        f"{item.name} & \\nth<{item.level}> & {item.short_description} & \\pageref<item:{item.name}> \\\\"
        for item in apparel
    ]
    row_text = '\n'.join(rows)
    return latexify(f"""
        \\begin<longtabuwrapper>
            \\begin<longtabu><l l X l>
                \\lcaption<Apparel Items> \\\\
                \\tb<Name> & \\tb<Level> & \\tb<Description> & \\tb<Page> \\\\
                \\bottomrule
                {row_text}
            \\end<longtabu>
        \\end<longtabuwrapper>
    """)


def sanity_check(armor, worn):
    pass

@click.command()
@click.option('-c', '--check/--no-check', default=False)
@click.option('-o', '--output/--no-output', default=False)
def main(output, check):
    apparel_latex = generate_apparel_latex()
    if output is None:
        print(apparel_latex)
    else:
        with open('apparel.tex', 'w') as apparel_description_file:
            apparel_description_file.write(apparel_latex)
        with open('apparel_table.tex', 'w') as apparel_table_file:
            apparel_table_file.write(generate_apparel_table())


if __name__ == "__main__":
    main()
