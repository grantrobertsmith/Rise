#!/usr/bin/env python3

import click
from rise.latex_generation.book_path import book_path
from rise.latex.effects import Effects
from rise.latex.mystic_sphere import MysticSphere
from rise.latex.spell import Spell
from rise.latex.util import latexify
import rise.statistics.rise_data as rise_data
from logging import getLogger, WARNING
# from pprint import pformat
logger = getLogger(__name__)
def log(*args):
    logger.log(*args)
def warn(*args):
    logger.log(WARNING, *args)


def generate_mystic_spheres():
    mystic_spheres = []

    # Primary: damage
    # Secondary: utility
    # Tertiary: buff
    # None: debuff
    mystic_spheres.append(MysticSphere(
        name='Aeromancy',
        short_description="Command air to protect allies and blast foes",
        cantrips=[
            Effects('Minor Windstrike', """
                Make an attack vs. Armor against a creature or object within \\rngmed range.
                \\hit The target takes bludgeoning \\glossterm<standard damage>.
            """, tags=['Air'], ap_cost=False),
            Effects('Soften Landing', """
                Choose a willing creature in \\rngmed range.
                Until the end of the round, the target treats all falls as if they were 5 feet shorter per \\glossterm<power> for the purpose of determining \\glossterm<falling damage>.
            """, tags=['Air'], ap_cost=False),
        ],
        schools=['Transmutation'],
        lists=['Nature'],
        rituals=[
        ],
        spells=[
            Spell('Propulsion', 1, """
                Choose a willing creature in \\rngclose range.
                You move the target up to 50 feet in any direction.
                You cannot change direction partway through the movement.
                Moving the target upwards cost twice the normal movement cost.
            """, tags=['Air', 'Swift']),
            Spell('Wind Screen', 1, """
                Choose a willing creature in \\rngclose range.
                The target gains a +1 \\glossterm<magic bonus> to Armor defense.
                This bonus is increased to +5 against ranged \\glossterm<physical attacks> from weapons or projectiles that are Small or smaller.

                You can cast this spell as a \\glossterm<minor action>.
                Any effect which increases the size of creature this spell can affect also increases the size of ranged weapon it defends against by the same amount.
            """, tags=['Air', 'Attune (target)', 'Shielding']),
            Spell('Greater Wind Screen', 4, """
                This spell functions like the \\spell<wind screen> spell, except that the Armor defense bonus increases to +2 and the defense bonus against ranged attacks increases to +10.
            """, tags=['Air', 'Attune (target)', 'Shielding']),
            Spell('Windstrike', 1, """
                Make an attack vs. Armor against a creature or object within \\rngmed range.
                \\hit The target takes bludgeoning \\glossterm<standard damage> +2d.
            """, tags=['Air']),
            Spell('Greater Windstrike', 3, """
                This spell functions like the \\spell<windstrike> spell, except that it affects a target within \\rnglong range and you gain a +1d bonus to damage.
            """, tags=['Air']),
            Spell('Supreme Windstrike', 5, """
                This spell functions like the \\spell<windstrike> spell, except that it affects a target within \\rngext range and you gain a +2d bonus to damage.
            """, tags=['Air']),
            Spell('Greater Propulsion', 2, """
                This spell functions like the \\spell<propulsion> spell, except that the distance you can move the target is increased to 100 feet.
                In addition, the target gains a +1d bonus to damage with melee \\glossterm<strikes> during the same phase.
            """, tags=['Air', 'Swift']),
            Spell('Supreme Propulsion', 4, """
                This spell functions like the \\spell<propulsion> spell, except that the distance you can move the target is increased to 300 feet.
                In addition, the target gains a +2d bonus to damage with melee \\glossterm<strikes> during the same phase.
            """, tags=['Air', 'Swift']),
            Spell('Gentle Descent', 2, """
                Choose a willing, Large or smaller creature in \\rngclose range.
                The target gains a 30 foot \\glossterm<glide speed> (see \\pcref<Gliding>).
            """, tags=['Air', 'Attune (target)']),
            Spell('Gust of Wind', 2, """
                Make an attack vs. Armor against everything in a \\arealarge, 10 ft. wide line from you.
                \\hit Each target takes bludgeoning \\glossterm<standard damage>.
            """, tags=['Air']),
            Spell('Greater Gust of Wind', 5, """
                This spell functions like the \\spell<gust of wind> spell, except that it affects everything in a \\areahuge, 10 ft. wide line from you and you gain a +1d bonus to damage.
            """, tags=['Air']),
            Spell('Windblade', 1, """
                Choose a willing creature within \\rngclose range.
                Melee weapons wielded by the target gain an additional five feet of \\glossterm<reach>.
                This has no effect on ranged attacks the target makes.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Air', 'Attune (target)', 'Shaping']),
            Spell('Greater Windblade', 4, """
                Choose a willing creature within \\rngclose range.
                Melee weapons wielded by the target gain an additional ten feet of \\glossterm<reach>.
                In addition, the target gains a +1d \\glossterm<magic bonus> to damage with melee \\glossterm<strikes>.
                This has no effect on ranged attacks the target makes.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Air', 'Attune (target)', 'Shaping']),
            Spell('Stormlord', 3, """
                This spell functions like the \\spell<wind screen> spell, except that the air also retaliates against creatures that attack the target.
                When a creature within \\rngclose range of the target attacks it, make an attack vs. Armor against the attacking creature.
                A hit deals bludgeoning \\glossterm<standard damage> -1d.
                Any individual creature can only be dealt damage in this way once per round.

                Any effect which increases this spell's range increases the range of this retaliation by the same amount.
            """, tags=['Air', 'Attune (target)', 'Shielding']),
            Spell('Greater Stormlord', 6, """
                This spell functions like the \\spell<stormlord> spell, except that you gain a +2d bonus to damage.
            """, tags=['Air', 'Attune (target)', 'Shielding']),
            Spell('Air Walk', 4, """
                Choose a willing creature in \\rngclose range.
                The target can walk on air as if it were solid ground.
                The magic only affects the target's legs and feet.
                By choosing when to treat the air as solid, it can traverse the air with ease.
            """, tags=['Air', 'Attune (target)']),
            Spell('Control Weather', 4, """
                When you cast this spell, you choose a new weather pattern.
                You can only choose weather which would be possible in the climate and season of the area you are in.
                For example, you can normally create a thunderstorm, but not if you are in a desert.

                When you complete the spell, the weather begins to take effect in a two mile radius cylinder-shaped zone centered on from your location.
                After five minutes, your chosen weather pattern fully takes effect.

                You can control the general tendencies of the weather, such as the direction and intensity of the wind.
                You cannot control specific applications of the weather -- where lightning strikes, for example, or the exact path of a tornado.
                Contradictory weather conditions are not possible simultaneously.

                After the spell's effect ends, the weather continues on its natural course, which may cause your chosen weather pattern to end.
                % TODO: This should be redundant with generic spell mechanics
                If another ability would magically manipulate the weather in the same area, the most recently used ability takes precedence.
            """, tags=['Air', 'Attune (self)']),
            Spell('Cyclone', 1, """
                Make an attack vs. Armor against everything in a \\areasmall radius within \\rngmed range.
                \\hit Each target takes bludgeoning \\glossterm<standard damage>.
            """, tags=['Air']),
            Spell('Greater Cyclone', 3, """
                This spell functions like the \\spell<cyclone> spell, except that it affects everything in a \\areamed radius within \\rnglong range.
            """, tags=['Air']),
            Spell('Supreme Cyclone', 6, """
                This spell functions like the \\spell<cyclone> spell, except that it affects everything in a \\arealarge radius and you gain a +1d bonus to damage.
            """, tags=['Air']),
            Spell('Stripping Windstrike', 2, """
                This spell functions like the \\spell<windstrike> spell, except that the attack result is also compared to the target's Reflex defense.
                % Clarify: this can hit even if the damaging effect misses
                \\hit The target drops all items it is holding that are not well secured (such as a ring) or held in two hands.
            """, tags=['Air']),
            Spell('Stripping Gust of Wind', 3, """
                This spell functions like the \\spell<gust of wind> spell, except that the attack result is also compared to each target's Reflex defense.
                \\hit Each target drops all items it is holding that are not well secured (such as a ring) or held in two hands.
            """, tags=['Air']),
            Spell('Stripping Cyclone', 2, """
                This spell functions like the \\spell<cyclone> spell, except that the attack result is also compared to each target's Reflex defense.
                \\hit Each target drops all items it is holding that are not well secured (such as a ring) or held in two hands.
            """, tags=['Air']),
        ],
        category='buff, defense',
    ))

    # Primary: buff
    # Secondary: damage
    # Tertiary: debuff
    # None: utility
    mystic_spheres.append(MysticSphere(
        name="Aquamancy",
        short_description="Command water to crush and drown foes",
        cantrips=[
            Spell('Create Water', 1, """
                You create up to one gallon per \\glossterm<power> of wholesome, drinkable water anywhere within \\rngclose range.
                The water can be created at multiple locations within the ritual's range, allowing you to fill multiple small water containers.
                You must create a minimum of one ounce of water in each location.
            """, tags=['Creation', 'Water'], ap_cost=False),
            Effects('Whelming Wave', """
                Make an attack vs. Fortitude against everything in a \\areamed, 5 ft.\\ wide line from you.
                \\hit Each target takes bludgeoning \\glossterm<standard damage> -1d.
            """, tags=['Manifestation', 'Water'], ap_cost=False),
        ],
        schools=['Conjuration'],
        lists=['Nature'],
        spells=[
            Spell('Crushing Wave', 1, """
                Make an attack vs. Fortitude against everything in a \\arealarge, 10 ft.\\ wide line from you.
                \\hit Each target takes bludgeoning \\glossterm<standard damage>.
            """, tags=['Manifestation', 'Water']),
            Spell('Water Jet', 1, """
                Make an attack vs. Armor against a creature within \\rngclose range.
                \\hit The target takes bludgeoning \\glossterm<standard damage> +2d.
            """, tags=['Manifestation', 'Water']),
            Spell('Wall of Water', 3, """
                You create a wall of water in a 20 ft.\\ high, \\arealarge line within \\rngmed range.
                The wall is four inches thick, and blocks \\glossterm<line of effect> for abilities.
                Sight through the wall is possible, though distorted.
                The wall provides both \\glossterm<passive cover> and \\glossterm<concealment> to targets on the opposite side of the wall, for a total of a +4 bonus to Armor defense.
                Creatures can pass through the wall unharmed, though it costs five extra feet of movement to move through the wall.

                Each five-foot square of wall has hit points equal to four times your \\glossterm<power>, and all of its defenses are 0.
                It is immune to most forms of attack, but it can be destroyed by \\glossterm<fire damage> and similar effects that can destroy water.
            """, tags=['Manifestation', 'Water']),
            Spell('Underwater Freedom', 1, """
                Choose a willing creature within \\rngclose range.
                The target suffers no penalties for acting underwater, except for those relating to using ranged weapons.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Greater Underwater Freedom', 3, """
                This spell functions like the \\spell<underwater freedom> spell, except that the target can also breathe water as if it was air.
            """, tags=['Attune (target)']),
            Spell('Raging River', 3, """
                This spell functions like the \\spell<crushing wave> spell, except that it gains the \\glossterm<Sustain> (standard) tag.
                The area affected by the spell becomes a \\glossterm<zone> that is continuously filled with rushing water.
                Each struck target in the area suffers penalties appropriate for fighting underwater, and may be unable to breathe.
                In addition, at the end of each \\glossterm<action phase> in subsequent rounds, the attack is repeated in that area.
            """, tags=['Manifestation', 'Water']),
            Spell('Greater Raging River', 5, f"""
                This spell functions like the \\textit<raging river> spell, except that the spell gains the \\glossterm<Sustain> (minor) tag instead of the \\glossterm<Sustain> (standard) tag.
            """, tags=['Manifestation', 'Water']),
            Spell('Geyser', 2, """
                Make an attack vs. Armor against everything in a \\arealarge, 5 ft.\\ wide vertical line within \\rngmed range.
                If this spell has its area increased, such as with the Widened \\glossterm<augment>, only the length of the line increases.
                \\hit Each target takes takes bludgeoning \\glossterm<standard damage> +2d.
            """, tags=['Manifestation', 'Water']),
            Spell('Aqueous Sphere', 2, f"""
                This spell functions like the \\spell<crushing wave> spell, except that it targets everything in a \\areasmall radius within \\rngmed range.
            """, tags=['Manifestation', 'Water']),
            Spell('Greater Aqueous Sphere', 4, """
                This spell functions like the \\spell<crushing wave> spell, except that it targets everything in a \\areamed radius within \\rnglong range.
            """, tags=['Manifestation', 'Water']),
            Spell('Overpowering Wave', 3, """
                This spell functions like the \\spell<crushing wave> spell, except that it attacks Reflex defense instead of Fortitude defense.
            """, tags=['Manifestation', 'Water']),
        ],
        rituals=[
            Spell('Dampen', 1, """
                Choose up to five willing ritual participants.
                Each target gains a \\glossterm<magic bonus> equal to your \\glossterm<power> to damage reduction against fire damage.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (ritual)']),
            Spell('Water Breathing', 2, """
                Choose a Medium or smaller willing ritual participant.
                The target can breathe water as easily as a human breathes air, preventing it from drowning or suffocating underwater.

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)']),
        ],
        category='damage',
    ))

    # Primary: damage
    # Secondary: debuff
    # Tertiary: utility
    # None: buff
    mystic_spheres.append(MysticSphere(
        name="Astromancy",
        short_description="Transport creatures and objects instantly through space",
        cantrips=[
            Effects('Dimensional Disruption', """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\hit The target takes physical \\glossterm<standard damage>.
            """, tags=['Planar', 'Teleportation'], ap_cost=False),
            Effects('Minor Translocation', """
                Choose a Tiny or smaller unattended object within \\rngclose range.
                The target teleports into an unoccupied location on a stable surface within range that can support the weight of the target.
                If the destination is invalid, the ability fails without effect.
            """, tags=['Teleportation'], ap_cost=False),
        ],
        schools=['Conjuration'],
        lists=['Arcane', 'Pact'],
        spells=[
            Spell('Dimensional Jaunt', 1, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\hit The target takes physical \\glossterm<standard damage> +2d.
            """, tags=['Planar', 'Teleportation']),
            Spell('Teleport', 1, """
                Choose a Medium or smaller willing creature or unattended object within \\rngclose range.
                The target teleports into an unoccupied destination within range.
                If the destination is invalid, this spell is \\glossterm<miscast>.
            """, tags=['Teleportation']),
            Spell('Greater Teleport', 3, """
                This spell functions like the \\textit<teleport> spell, except that the range is increased to \\rngext.
            """, tags=['Teleportation']),
            Spell('Banishment', 2, """
                This spell functions like the \\spell<dimensional jaunt> spell, except that it gains a +2 bonus to \\glossterm<accuracy> against \\glossterm<outsiders> not on their home planes and creatures created by \\glossterm<Manifestation> abilities.
                \\crit The target takes double damage.
                In addition, if it is an outsider not on its home plane, it is teleported to a random location on its home plane.
                If it is a creature created by a \\glossterm<Manifestation> ability, it immediately disappears.
            """, tags=['Planar', 'Teleportation']),
            Spell('Dimension Door', 3, """
                You teleport to a location within \\rngext range of you.
                You must clearly visualize the destination's appearance, but you do not need \\glossterm<line of sight> or \\glossterm<line of effect> to your destination.
            """, tags=['Teleportation']),
            Spell('Dimensional Jaunt -- Plane of Earth', 2, """
                This spell functions like the \\spell<dimensional jaunt> spell, except that the target is partially teleported into the Plane of Earth.
                The damage becomes bludgeoning damage, and a struck target is \\glossterm<slowed> as a \\glossterm<condition>.
            """, tags=['Planar', 'Teleportation']),
            Spell('Dimensional Jaunt -- Plane of Fire', 3, """
                This spell functions like the \\spell<dimensional jaunt> spell, except that the target is partially teleported into the Plane of Fire.
                The damage becomes fire damage and increases by +1d.
                In addition, a struck target is \\glossterm<ignited> until it puts out the fire.
                This condition can also be removed if the target makes a \\glossterm<DR> 10 Dexterity check as a \\glossterm<move action> to put out the flames.
                Dropping \\glossterm<prone> as part of this action gives a +5 bonus to this check.
            """, tags=['Planar', 'Teleportation']),
            Spell('Dimensional Jaunt -- Deep Astral Plane', 5, """
                This spell functions like the \\spell<dimensional jaunt> spell, except that the target is partially teleported into the deep Astral Plane.
                The damage increases by +1d.
                In addition, a struck target is \\glossterm<stunned> as a \\glossterm<condition>.
            """, tags=['Planar', 'Teleportation']),
            Spell('Dimensional Jaunt -- Myriad', 6, """
                This spell functions like the \\spell<dimensional jaunt> spell, except that the target is partially teleported through a dizzying array of planes.
                The damage increases by +3d and becomes damage of all types.
            """, tags=['Planar', 'Teleportation']),
            Spell('Dimensional Shuffle', 2, """
                Choose up to five willing creatures within \\rngmed range.
                Each target teleports into the location of a different target.
            """, tags=['Teleportation']),
            Spell('Blink', 4, """
                Choose a willing creature within \\rngclose range.
                The target randomly blinks between its current plane and the Astral Plane.
                This blinking stops if the target takes actions on its current plane.
                In any phase where it does not take any actions, the target has a 50\% chance to completely ignore any effect that targets it directly.
                It is still affected normally by abilities that affect an area.
            """, tags=['Attune (target)', 'Teleportation', 'Planar']),
            Spell('Greater Blink', 7, """
                This spell functions like the \\spell<blink> spell, except that the target also has a 20\% chance to completely ignore any effect that targets it directly during phases where it takes an action.
            """, tags=['Attune (target)', 'Teleportation', 'Planar']),
        ],
        rituals=[
            Spell('Gate', 7, """
                Choose a plane that connects to your current plane, and a location within that plane.
                This ritual creates an interdimensional connection between your current plane and the location you choose, allowing travel between those two planes in either direction.
                The gate takes the form of a \\areasmall radius circular disk, oriented a direction you choose (typically vertical).
                It is a two-dimensional window looking into the plane you specified when casting the spell, and anyone or anything that moves through it is shunted instantly to the other location.
                The gate cannot be \\glossterm<sustained> for more than 5 rounds, and is automatically dismissed at the end of that time.

                You must specify the gate's destination with a precise mental image of its appearance.
                The image does not have to be perfect, but it must unambiguously identify the location.
                Incomplete or incorrect mental images may result in the ritual leading to an unintended destination within the same plane, or simply failing entirely.

                % TODO: Is this planar cosmology correct?
                The Astral Plane connects to every plane, but transit from other planes is usually more limited.
                From the Material Plane, you can only reach the Astral Plane.

                This ritual takes one week to perform, and requires 98 action points from its participants.
            """, tags=['Planar', 'Teleportation', 'Sustain (standard)']),
            Spell('Plane Shift', 3, """
                Choose up to five Large or smaller willing ritual participants.
                In addition, you choose a \\glossterm<planar rift> within \\rngmed range to travel through.
                The targets teleport to the unoccupied spaces closest to the other side of the planar rift.
                For details about \\glossterm<planar rifts>, see \\pcref<Planar Rifts>.

                % TODO: Is this planar cosmology correct?
                The Astral Plane connects to every plane, but transit from other planes is usually more limited.
                From the Material Plane, you can only reach the Astral Plane.

                This ritual takes 24 hours to perform, and requires 18 action points from its participants.
            """, tags=['Planar', 'Teleportation']),
            Spell('Astral Projection', 4, """
                Choose up to five Large or smaller willing ritual participants.
                The targets teleport to a random location within the Inner Astral Plane (see \\pcref<The Astral Plane>).

                In addition, a localized \\glossterm<planar rift> appears at the destination area on the Astral Plane which leads back to the location where this ritual was performed.
                The rift can only be passed through by the targets of this effect.
                It lasts for one week before disappearing permanently, potentially stranding the targets in the Astral Plane if they have not yet returned.

                This ritual takes 24 hours to perform, and requires 32 action points from its participants.
            """, tags=['Planar', 'Teleportation']),
            Spell('Homeward Shift', 5, """
                This ritual can only be performed on the Astral Plane.
                Choose up to five Large or smaller willing ritual participants.
                The targets teleport to the last spaces they occupied on their home planes.

                This ritual takes 24 hours to perform, and requires 50 action points from its participants.
            """, tags=['Planar', 'Teleportation']),
            Spell('Overland Teleportation', 4, """
                Choose up to five willing, Medium or smaller ritual participants.
                In addition, choose a destination up to 100 miles away from you on your current plane.
                Each target is teleported to the chosen destination.

                You must specify the destination with a precise mental image of its appearance.
                The image does not have to be perfect, but it must unambiguously identify the destination.
                If you specify its appearance incorrectly, or if the area has changed its appearance, the destination may be a different area than you intended.
                The new destination will be one that more closely resembles your mental image.
                If no such area exists, the ritual simply fails.
                % TODO: does this need more clarity about what teleportation works?

                This ritual takes 24 hours to perform and requires 32 action points from its ritual participants.
            """, tags=['Teleportation']),
            Spell('Retrieve Legacy', 3, """
                Choose a willing ritual participant.
                If the target's \\glossterm<legacy item> is on the same plane and \\glossterm<unattended>, it is teleported into the target's hand.

                This ritual takes 24 hours to perform, and requires 18 action points from its ritual participants.
            """, tags=['Teleportation']),
        ],
        category='damage',
    ))

    # Primary: buff
    # Secondary: utility
    # None: damage, debuff
    mystic_spheres.append(MysticSphere(
        name='Barrier',
        short_description="Shield allies from hostile forces",
        cantrips=[Effects('Kinetic Shield', """
            Choose a willing creature in \\rngclose range.
            The target gains a \\glossterm<magic bonus> equal to your \\glossterm<power> to \\glossterm<damage reduction> against \\glossterm<physical> damage.
        """, tags=['Sustain (standard)'], ap_cost=False)],
        schools=['Abjuration'],
        lists=['Arcane', 'Divine', 'Nature'],
        spells=[
            Spell('Ablative Shield', 1, """
                Choose a willing creature in \\rngclose range.
                The target gains a \\glossterm<magic bonus> equal to your \\glossterm<power> to \\glossterm<damage reduction> against all damage except for \\glossterm<energy damage>.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Shielding']),
            Spell('Resist Energy', 1, """
                Choose a willing creature in \\rngclose range.
                The target gains a \\glossterm<magic bonus> equal to your \\glossterm<power> to \\glossterm<damage reduction> against \\glossterm<energy damage>.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Shielding']),
            Spell('Complete Shield', 2, """
                This spell functions like the \\spell<ablative shield> spell, except that the damage reduction applies against all damage.
            """, tags=['Attune (target)', 'Shielding']),
            Spell('Repulsion Field', 2, """
                This spell creates a repulsive field in a \\areamed radius zone from your location.
                When an enemy makes physical contact with the spell's area for the first time, you make an attack vs. Mental against it.
                \\hit The target is unable to enter the spell's area with any part of its body.
                The rest of its movement in the current phase is cancelled.

                Creatures in the area at the time that the spell is cast are unaffected by the spell.
            """, tags=['Sustain (minor)']),
            Spell('Immunity', 3, """
                Choose a willing creature in \\rngclose range, and a type of damage that is not a kind of physical damage (see \\pcref<Damage Types>).
                The target becomes immune to damage of the chosen type.
                Attacks that deal damage of multiple types still inflict damage normally unless the target is immune to all types of damage dealt.
            """, tags=['Attune (target)', 'Shielding']),
            Spell('Retributive Shield', 3, """
                This spell functions like the \\spell<ablative shield> spell, except that damage resisted by this spell is dealt back to the attacker as life damage.
                If the attacker is beyond \\rngclose range of the target, this reflection fails.

                Any effect which increases this spell's range increases the range of this effect by the same amount.
                This spell is from both the Abjuration and Vivimancy schools and gains the \\glossterm<Life> tag in addition to the tags from the \\spell<ablative shield> spell.
            """, tags=['Attune (target)', 'Shielding']),
            Spell('Empowered Shield', 4, """
                This spell functions like the \\spell<ablative shield> spell, except that the bonus is equal to twice your \\glossterm<power>.
            """, tags=['Attune (target)', 'Shielding']),
            Spell('Deflective Shield', 3, """
                This spell functions like the \\spell<ablative shield> spell, except that the target also gains a +1 \\glossterm<magic bonus> to Armor defense.
            """, tags=['Attune (target)', 'Shielding']),
            Spell('Antilife Shell', 5, """
                This effect functions like the \\spell<repulsion field> spell, except that you gain a +10 bonus to accuracy with the attack against living creatures.
            """, tags=['Sustain (minor)']),
        ],
        rituals=[
            Spell('Endure Elements', 1, """
                Choose a willing creature or unattended object within \\rngclose range.
                The target suffers no harm from being in a hot or cold environment.
                It can exist comfortably in conditions between \minus50 and 140 degrees Fahrenheit.
                Its equipment, if any, is also protected.
                This does not protect the target from fire or cold damage.

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)', 'Shielding']),
            Spell('Mystic Lock', 2, """
                Choose a Large or smaller closable, nonmagical object within \\rngclose range, such as a door or box.
                The target object becomes magically locked.
                It can be unlocked with a Devices check against a DR equal to 20 \\add your \\glossterm<power>.
                The DR to break it open forcibly increases by 10.

                You can freely pass your own \\ritual<arcane lock> as if the object were not locked.
                This effect lasts as long as you \\glossterm<attune> to it.
                If you use this ability multiple times, you can attune to it each time.

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)']),
            Spell('Resilient Lock', 4, f"""
                This ritual functions like the \\ritual<mystic lock> ritual, except that the DR to unlock the target with a Devices check is instead equal to 30 + your \\glossterm<power>.
                In addition, the DR to break it open increases by 20 instead of by 10.
            """, tags=['Attune (ritual)']),
            Spell('Explosive Runes', 3, """
                Choose a Small or smaller unattended object with writing on it within \\rngclose range.
                % TODO: clarify how to identify that this is Explosive Runes instead of bad handwriting
                The writing on the target is altered by the runes in subtle ways, making it more difficult to read.
                To read the writing, a creature must concentrate on reading it, which requires a standard action.
                If a creature reads the target, the target explodes.
                You make an attack vs. Armor against everything within a \\areamed radius from the target.
                Each struck target takes bludgeoning \\glossterm<standard damage> from the explosion.

                After the target object explodes in this way, the ritual is \\glossterm<dismissed>.
                If the target is destroyed or rendered illegible, the ritual is dismissed without exploding.
                This ritual takes one hour to perform.
            """, tags=['Attune (ritual)', 'Trap']),
            Spell('Scryward', 2, """
                This ritual creates a ward against scrying in a \\arealarge radius zone centered on your location.
                All \\glossterm<Scrying> effects fail to function in the area.
                This effect is permanent.

                This ritual takes 24 hour to perform, and requires 8 action points from its participants.
            """, tags=['Mystic']),
            Spell('Private Sanctum', 4, """
                This ritual creates a ward against any external perception in a \\arealarge radius zone centered on your location.
                This effect is permanent.
                Everything in the area is completely imperceptible from outside the area.
                Anyone observing the area from outside sees only a dark, silent void, regardless of darkvision and similar abilities.
                In addition, all \\glossterm<Scrying> effects fail to function in the area.
                Creatures inside the area can see within the area and outside of it without any difficulty.

                This ritual takes 24 hours to perform, and requires 32 action points from its participants.
            """, tags=['Mystic']),
        ],
        category='buff, defense',
    ))

    # Primary: buff
    # None: debuff, utility, damage
    mystic_spheres.append(MysticSphere(
        name='Bless',
        short_description="Grant divine blessings to aid allies and improve combat prowess",
        cantrips=[Effects('Minor Cleansing Blessing', """
            Choose a willing creature within \\rngclose range.
            The target removes one \\glossterm<condition> affecting it.
        """, ap_cost=False)],
        schools=['Channeling'],
        lists=['Divine'],
        spells=[
            Spell('Blessing of Protection', 1, """
                Choose a willing creature within \\rngclose range.
                The target gains a +1 \\glossterm<magic bonus> to Armor defense and Mental defense.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Greater Blessing of Protection', 4, """
                This spell functions like the \\spell<blessing of protection> spell, except that bonus increases to +2.
            """, tags=['Attune (target)']),
            Spell('Supreme Blessing of Protection', 7, """
                This spell functions like the \\spell<blessing of protection> spell, except that bonus increases to +3.
            """, tags=['Attune (target)']),
            Spell('Battle Blessing', 2, """
                Choose a willing creature within \\rngclose range.
                The target gains a +1 \\glossterm<magic bonus> to \\glossterm<accuracy> with all attacks.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Greater Battle Blessing', 5, """
                This spell functions like the \\spell<battle blessing> spell, except that the bonus increases to +2.
            """, tags=['Attune (target)']),
            Spell('Blessing of Resilience', 3, """
                Choose a willing creature within \\rngclose range.
                The target ignores the next two \\glossterm<conditions> it would receive.
                After resisting two conditions in this way, this spell ends.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Greater Blessing of Resilience', 5, """
                This spell functions like the \\textit<blessing of resilience> spell, except that the spell does not end until it resists three \\glossterm<conditions>.
            """, tags=['Attune (target)']),
            Spell('Supreme Blessing of Resilience', 7, """
                This spell functions like the \\textit<blessing of resilience> spell, except that the spell does not end until it resists four \\glossterm<conditions>.
            """, tags=['Attune (target)']),
            Spell('Blessing of Supremacy', 4, """
                Choose a willing creature within \\rngclose range.
                The target gains a +1 \\glossterm<magic bonus> to \\glossterm<accuracy> and a +1d \\glossterm<magic bonus> to \\glossterm<damage> with all abilities.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Cleansing Blessing', 1, """
                All allies within \\arealarge radius from you can remove one \\glossterm<condition> affecting them.
            """, tags=[]),
            Spell('Greater Cleansing Blessing', 4, """
                This spell functions like the \\spell<cleansing blessing> spell, except that each ally can remove two conditions instead of one.
            """, tags=[]),
            Spell('Blessing of Might', 3, """
                The target gains a +1d \\glossterm<magic bonus> to damage with all abilities.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Greater Blessing of Might', 6, """
                The target gains a +2d \\glossterm<magic bonus> to damage with all abilities.
            """, tags=['Attune (target)']),
        ],
        rituals=[
            Spell('Blessing of Fortification', 1, """
                Choose an unattended, nonmagical object or part of an object of up to Large size.
                Unlike most abilities, this ritual can affect individual parts of a whole object.

                % How should this affect Strength break DRs?
                The target gains a +5 \\glossterm<magic bonus> to \\glossterm<hardness>.
                If the target is moved, this effect ends.
                Otherwise, it lasts for one year.

                This ritual takes one hour to perform.
            """, tags=['Attune (ritual)']),
            Spell('Enduring Fortification', 3, """
                This ritual functions like the \\spell<blessing of fortification> ritual, except that the effect lasts for one hundred years.
            """, tags=[]),
            Spell('Greater Enduring Fortification', 5, """
                This ritual functions like the \\spell<greater fortification> ritual, except that the effect lasts for one hundred years.
            """, tags=[]),
            Spell('Greater Fortification', 3, """
                This ritual functions like the \\spell<blessing of fortification> ritual, except that the \\glossterm<hardness> bonus increases to 10.
            """, tags=['Attune (ritual)']),
            Spell('Supreme Fortification', 6, """
                This ritual functions like the \\spell<blessing of fortification> ritual, except that the \\glossterm<hardness> bonus increases to 15.
            """, tags=['Attune (ritual)']),
            Spell('Bless Water', 1, """
                Choose one pint of unattended, nonmagical water within \\rngclose range.
                The target becomes holy water.
                Holy water can be can be thrown as a splash weapon, dealing 1d8 points of damage to a struck undead creature or an evil outsider.

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)']),
            Spell('Permanent Bless Water', 2, """
                This ritual functions like the \\spell<bless water> ritual, except that it loses the \\glossterm<Attune> (ritual) tag and the effect lasts permanently.
                This ritual takes one hour to perform.
            """, tags=[]),
            Spell('Curse Water', 1, """
                Choose one pint of unattended, nonmagical water within \\rngclose range.
                The target becomes unholy water.
                Unholy water can be can be thrown as a splash weapon, dealing 1d8 points of damage to a struck good outsider.

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)']),
            Spell('Permanent Curse Water', 2, """
                This ritual functions like the \\spell<curse water> ritual, except that it loses the \\glossterm<Attune> (ritual) tag and the effect lasts permanently.
                This ritual takes one hour to perform.
            """, tags=[]),
            Spell('Blessing of Purification', 1, """
                All food and water in a single square within \\rngclose range is purified.
                Spoiled, rotten, poisonous, or otherwise contaminated food and water becomes pure and suitable for eating and drinking.
                This does not prevent subsequent natural decay or spoiling.

                This ritual takes one hour to perform.
            """, tags=['Shaping']),
        ],
        category='buff, offense',
    ))

    # This spell is problematic
    # Primary: damage
    # None: buff, debuff, utility
    mystic_spheres.append(MysticSphere(
        name="Channel Divinity",
        short_description="Invoke divine power to smite foes and gain power",
        cantrips=[Effects('Divine Judgment', """
            Make an attack vs. Mental against a creature within \\rngmed range.
            \\hit The target takes divine \\glossterm<standard damage>.
        """, ap_cost=False)],
        schools=['Channeling'],
        lists=['Divine'],
        spells=[
            Spell('Judge Unworthy', 1, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\hit The target takes divine \\glossterm<standard damage> +2d.
            """, tags=[]),
            Spell('Word of Faith', 2, """
                Make an attack vs. Mental against all enemies in a \\areamed radius from you.
                \\hit Each target takes divine \\glossterm<standard damage>.
            """, tags=[]),
            Spell('Mantle of Faith', 1, """
                You gain a \\glossterm<magic bonus> to equal to your \\glossterm<power> to \\glossterm<damage reduction> against \\glossterm<physical> damage.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (self)']),
            Spell('Greater Mantle of Faith', 4, """
                This spell functions like the \\spell<mantle of faith> spell, except that the bonus is equal to twice your \\glossterm<power>.
            """, tags=['Attune (self)']),
            Spell('Complete Mantle of Faith', 2, """
                You gain a \\glossterm<magic bonus> equal to your \\glossterm<power> to \\glossterm<damage reduction> against all damage.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (self)']),
            Spell('Greater Complete Mantle of Faith', 5, """
                This spell functions like the \\spell<complete mantle of faith> spell, except that the bonus is equal to twice your \\glossterm<power>.
            """, tags=['Attune (self)']),
            Spell('Divine Might', 3, """
                You increase your size by one \\glossterm<size category>.
                This increases your \\glossterm<overwhelm value>, \\glossterm<overwhelm resistance>, and usually increases your \\glossterm<reach> (see \\pcref<Size in Combat>).
                However, your muscles are not increased fully to match its new size, and your Strength is unchanged.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (self)', 'Shaping', 'Sizing']),
            Spell('Divine Might, Greater', 5, """
                This spell functions like the \\textit<divine might> spell, except that you also gain a +2 \\glossterm<magic bonus> to Strength.
            """, tags=['Attune (self)', 'Shaping', 'Sizing']),
            Spell('Divine Might, Supreme', 7, """
                This spell functions like the \\spell<divine might> spell, except that your size is increased by two size categories.
                You gain a +2 \\glossterm<magic bonus> to Strength to partially match your new size.
            """, tags=['Attune (self)', 'Shaping', 'Sizing']),
        ],
        rituals=[
            Spell('Consecrate', 2, """
                The area within an \\arealarge radius \\glossterm<zone> from your location becomes sacred to your deity.
                % TODO: what cares about consecration?
                This has no tangible effects by itself, but some special abilities and monsters behave differently in consecrated areas.

                This ritual takes 24 hours to perform and requires 8 action points from its ritual participants.
            """, tags=['Attune (self)']),
            Spell('Divine Transit', 4, """
                Choose up to five willing, Medium or smaller ritual participants.
                In addition, choose a destination up to 100 miles away from you on your current plane.
                Each target is teleported to the temple or equivalent holy site to your deity that is closest to the chosen destination.

                You must specify the destination with a precise mental image of its appearance.
                The image does not have to be perfect, but it must unambiguously identify the destination.
                If you specify its appearance incorrectly, or if the area has changed its appearance, the destination may be a different area than you intended.
                The new destination will be one that more closely resembles your mental image.
                If no such area exists, the ritual simply fails.
                % TODO: does this need more clarity about what teleportation works?

                This ritual takes 24 hours to perform and requires 32 action points from its ritual participants.
                It is from the Conjuration school in addition to the Channeling school.
            """, tags=['Teleportation']),
        ],
        category='damage',
    ))

    # Primary: debuff
    # Secondary: buff
    # Tertiary: utility
    # None: damage
    mystic_spheres.append(MysticSphere(
        name="Chronomancy",
        short_description="Manipulate the passage of time to inhibit foes and aid allies",
        cantrips=[Effects('Minor Slow', """
            Make an attack vs. Mental against a creature within \\rngmed range.
            \\hit The target is \\glossterm<slowed> as a \\glossterm<condition>.
        """, tags=['Temporal'], ap_cost=False)],
        schools=['Transmutation'],
        lists=['Arcane', 'Pact'],
        spells=[
            Spell('Slow', 1, """
                Make an attack vs. Mental with a +2 bonus to \\glossterm<accuracy> against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\glossterm<slowed> as a \\glossterm<condition>.
                \\crit the target is \\glossterm<decelerated> as a \\glossterm<condition>.
            """, tags=['Temporal']),
            Spell('Decelerate', 3, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\glossterm<decelerated> as a \\glossterm<condition>.
                \\crit the target is \\glossterm<decelerated> twice as two separate \\glossterm<conditions>.
            """, tags=['Temporal']),
            Spell('Mental Lag', 2, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\glossterm<slowed> and \\glossterm<dazed> as two separate \\glossterm<conditions>.
                \\crit the target is \\glossterm<decelerated> and \\glossterm<dazed> as two separate \\glossterm<conditions>.
            """, tags=['Temporal']),
            Spell('Haste', 1, """
                Choose a willing creature within \\rngmed range.
                The target gains a +10 foot \\glossterm<magic bonus> to its \\glossterm<base speed>.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Temporal']),
            Spell('Greater Haste', 3, """
                Choose a willing creature within \\rngmed range.
                The target gains a +30 foot \\glossterm<magic bonus> to its \\glossterm<base speed>, up to a maximum of double its \\glossterm<base speed>.
                In addition, it gains a +2 \\glossterm<magic bonus> to Reflex defense.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Temporal']),
            Spell('Temporal Duplicate', 4, """
                Choose a willing creature within \\rngmed range.
                You reach into a possible future and create a duplicate of the target.
                The duplicate is identical in all ways to the target when the spell resolves, except that it has no \\glossterm<legend points>.
                The target and its duplicate can act during the next round.
                At the end of that round, the target and its duplicate cease to exist.
                At the end of the following round, the target reappears in the place where it ceased to exist.
                If that space is occupied, it appears in the closest unoccupied space.

                When the target reappears, its condition is unchanged from when it left, except that it loses all action points, spell points, and all similar resources equal to the amount used by its duplicate.
                Its hit points, conditions, and all other statistics are unaffected, regardless of any damage or other negative effects suffered by the duplicate.
                If this would reduce any of the target's resources below 0, it takes physical \\glossterm<standard damage> +4d from the paradox and becomes \\glossterm<stunned> as a \\glossterm<condition>.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Temporal']),
            Spell('Greater Temporal Duplicate', 7, """
                This spell functions like the \\spell<temporal duplicate> spell, except that you can reach up to five minutes into the future to summon the duplicate.
                When you cast the spell, you choose the length of time before the target disappears.
                The duplicate still only exists for a single round.
            """, tags=['Temporal']),
            Spell('Time Hop', 2, """
                Choose a Medium or smalller willing creature or unattended object within \\rngmed range.
                You send the target into the future, causing it to temporarily cease to exist.
                When you cast this spell, you choose how many rounds the target ceases to exist for, up to a maximum of five rounds.
                At the end of the last round, it reappears in the same location where it disappeared.

                The area the target occupied can be physically crossed, but it is treated as an invalid destination for teleportation and other similar magic.
                When the target reappears, all of its surroundings are adjusted as if the object had retroactively always existed in its space.
                For example, if the location is occupied by a creature that walked into the area, the creature is relocated to the closest unoccupied space along the path it took to reach the target.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Temporal']),
            Spell('Temporal Stasis', 3, """
                Choose a Medium or smaller willing creature within \\rngmed range.
                The target is placed into stasis, rendering it unconscious.
                While in stasis, it cannot take any actions and cannot be targeted, moved, damaged, or otherwise affected by outside forces in any way.

                % TODO: wording
                This effect normally lasts as long as you \\glossterm<attune> to it, and until the end of the round when you release the attunement.
                If you use this ability on yourself, it instead lasts for a number of rounds you choose when you cast the spell, up to a maximum of five rounds.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (self)', 'Temporal']),
            Spell('Delay Damage', 3, """
                When you take damage, half of the damage (rounded down) is not dealt to you immediately.
                This damage is tracked separately.
                When the ends, you take all of the delayed damage at once.
                This damage has no type, and ignores all effects that reduce or negate damage.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Sustain (minor)', 'Temporal']),
            Spell('Time Lock', 4, """
                Choose a willing creature within \\rngmed range.
                You lock the state of the target's body in time.
                Note the target's hit points, vital damage, and active conditions.
                If the target dies, this effect ends immediately.

                As a \\glossterm<standard action>, you can reach through time to restore the target's state.
                If you do, the target's hit points, vital damage, and active conditions become identical to what they were when you cast this spell.
                This does not affect any other properties of the target, such as any resources expended.
                After you restore the target's state in this way, the spell ends.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Sustain (minor)', 'Temporal']),
            Spell('Greater Time Lock', 7, """
                This spell functions like the \\textit<time lock> spell, except that the effect is not ended if the target dies, and restoring the target's state can also restore it to life.
                If the target is restored to life in this way, all of its properties not locked by this spell, such as any resources expended, are identical to what they were when the target died.
                In addition, this spell has the \\glossterm<Attune> (self) tag instead of the \\glossterm<Sustain> (minor) tag.
            """, tags=['Attune (self)', 'Temporal']),
            Spell('Time Stop', 7, """
                You can take two full rounds of actions immediately.
                During this time, all other creatures and objects are fixed in time, and cannot be targeted, moved, damaged, or otherwise affected by outside forces in any way.
                You can still affect yourself and create areas or new effects.

                You are still vulnerable to danger, such as from heat or dangerous gases.
                However, you cannot be detected by any means while you travel.

                After casting this spell, you cannot cast it again until you take a \\glossterm<short rest>.
            """, tags=['Temporal']),
        ],
        rituals=[
            Spell('Gentle Repose', 2, """
                Choose an unattended, nonmagical object within \\rngclose range.
                Time does not pass for the target, preventing it from decaying or spoiling.
                This can extend the time a poison or similar item lasts before becoming inert.
                % What effects have an explicit time limit?
                If used on a corpse, this effectively extends the time limit for effects that require a fresh or intact body.
                Additionally, this can make transporting a fallen comrade more pleasant.

                % Does this need to explicitly clarify that it doesn't stop time from passing for the creature's soul?

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)', 'Temporal']),
        ],
        category='debuff, combat',
    ))

    # This spell seems problematic
    # Primary: debuff
    # None: damage, utility, buff
    mystic_spheres.append(MysticSphere(
        name="Compel",
        short_description="Bend creatures to your will by controlling their actions",
        cantrips=[Effects('Fall', """
            Make an attack vs. Mental against a creature within \\rngmed range.
            \\hit The target falls \\glossterm<prone>.
        """, tags=['Compulsion', 'Mind'], ap_cost=False)],
        schools=['Enchantment'],
        lists=['Arcane', 'Divine', 'Pact'],
        spells=[
            Spell('Dance', 1, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit As a \\glossterm<condition>, the target is compelled to dance.
                It can spend a \\glossterm<move action> to dance, if it is physically capable of dancing.
                At the end of each round, if the target did not dance during that round, it takes a -2 penalty to \\glossterm<accuracy>, \\glossterm<checks>, and \\glossterm<defenses> as the compulsion intensifies.
                This penalty stacks each round until the target dances, which resets the penalties to 0.
                \\crit As above, except that the target must dance as a \\glossterm<standard action> to reset the penalties, instead of as a move action.
            """, tags=['Compulsion', 'Mind']),
            Spell('Collapse', 1, """
                Make an attack vs. Mental against all enemies in a \\areamed radius from you.
                \\hit Each target falls \\glossterm<prone>.
                \\crit As above, and as a \\glossterm<condition>, each target is unable to stand up.
                If a target is somehow brought into a standing position, it will immediately fall and become prone again.
            """, tags=['Compulsion', 'Mind']),
            Spell('Stay', 1, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target falls \\glossterm<prone> and is \\glossterm<slowed> as a \\glossterm<condition>.
                \\crit The target falls prone and is \\glossterm<decelerated> as a \\glossterm<condition>.
            """, tags=['Compulsion', 'Mind']),
            Spell('Confusion', 3, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\disoriented as a \\glossterm<condition>.
                \\crit The target is \\confused as a \\glossterm<condition>.
            """, tags=['Compulsion', 'Mind']),
            Spell('Sleep', 3, """
                Make an attack vs. Mental against a creature within \\rngclose range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\blinded as a \\glossterm<condition>.
                \\crit The target falls asleep.
                It cannot be awakened by any means while the spell lasts.
                After that time, it can wake up normally, though it continues to sleep until it would wake up naturally.
                % Awkward to sustain without the Sustain tag
                This effect lasts as long as you \\glossterm<sustain> it as a \\glossterm<minor action>.
                However, it is a \\glossterm<condition>, and can be removed by effects which remove conditions.
            """, tags=['Compulsion', 'Mind']),
            Spell('Discordant Song', 4, """
                Make an attack vs. Mental against all enemies in a \\areamed radius from you.
                \\hit Each target is \\disoriented as a \\glossterm<condition>.
                \\crit Each target is \\confused as a \\glossterm<condition>.
            """, tags=['Compulsion', 'Mind']),
            Spell('Irresistible Dance', 6, """
                This spell functions like the \\textit<dance> spell, except that you gain a +4 bonus to accuracy on the attack.
            """, tags=['Compulsion', 'Mind']),
            Spell('Dominate', 4, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\glossterm<confused> as a \\glossterm<condition>.
                \\crit The target is \\glossterm<stunned> as a \\glossterm<condition>.
                As a standard action, you can make an additional attack vs. Mental against the target as long as it remains stunned in this way and is within \\rngmed range of you.
                On a hit, the target becomes stunned in the same way as an additional condition, continuing the effect even if the target removed the original condition in the same phase.
                On a critical hit, the target becomes \\glossterm<dominated> by you as long as you \\glossterm<attune> to this ability.
            """, tags=['Compulsion', 'Mind']),
        ],
        category='debuff, combat',
    ))

    # Primary: debuff
    # Secondary: damage
    # None: buff, utility
    mystic_spheres.append(MysticSphere(
        name="Corruption",
        short_description="Weaken the life force of foes, reducing their combat prowess",
        cantrips=[Effects('Sicken', """
            Make an attack vs. Fortitude against a living creature within \\rngclose range.
            \\hit The target is \\glossterm<sickened> as a \\glossterm<condition>.
        """, tags=['Life'], ap_cost=False)],
        schools=['Vivimancy'],
        lists=['Arcane', 'Divine', 'Nature', 'Pact'],
        spells=[
            Spell('Sickening Decay', 1, """
                Make an attack vs. Fortitude against a living creature within \\rngclose range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\glossterm<sickened> as a \\glossterm<condition>.
                % TODO: clarify when exactly this damage is taken (should be at the end of the phase)
                In addition, it takes life \\glossterm<standard damage> -2d when it takes a \\glossterm<standard action>.
                It can only take damage in this way once per round.
                \\crit The target is \\glossterm<nauseated> as a \\glossterm<condition>.
                In addition, it takes life \\glossterm<standard damage> when it takes a \\glossterm<standard action>.
                It can only take damage in this way once per round.
            """, tags=['Life']),
            Spell('Corruption of Blood and Bone', 3, """
                This spell functions like the \\spell<sickening decay> spell, except that it gains a +1d bonus to damage.
                In addition, damage from the spell reduces the target's maximum hit points by the same amount.
                This hit point reduction is part of the same \\glossterm<condition> as the spell's other effects.
                When the condition is removed, the target's maximum hit points are restored.
            """, tags=['Life']),
            Spell('Curse of Decay', 4, """
                This spell functions like the \\spell<sickening decay> spell, except that the attack is made against Mental defense instead of Fortitude defense.
                In addition, if the attack critically hits, the spell's effect becomes a permanent curse.
                It is no longer a condition, and cannot be removed by abilities that remove conditions.
            """, tags=['Curse']),
            Spell('Miasma', 1, """
                Make an attack vs. Fortitude against all living enemies within an \\areamed radius from you.
                \\hit Each target is \\glossterm<sickened> as a \\glossterm<condition>.
                \\crit Each target is \\glossterm<nauseated> as a \\glossterm<condition>.
            """, tags=['Life']),
            Spell('Pernicious Sickness', 2, """
                Make an attack vs. Fortitude with a +2 bonus to \\glossterm<accuracy> against a living creature within \\rngmed range.
                \\hit The target is \\glossterm<sickened> as a \\glossterm<condition>.
                \\crit The target is \\glossterm<nauseated> as a \\glossterm<condition>.
            """, tags=['Life']),
            Spell('Greater Pernicious Sickness', 5, """
                This spell functions like the \\spell<pernicious sickness> spell, except that the accuracy bonus is increased to +4.
            """, tags=['Life']),
            Spell('Greater Miasma', 3, """
                Make an attack vs. Fortitude against all living enemies within an \\areamed radius from you.
                \\hit Each target is \\glossterm<nauseated> as a \\glossterm<condition>.
                \\crit Each target is \\glossterm<nauseated> twice as two separate \\glossterm<conditions>.
            """, tags=['Life']),
            Spell('Eyebite', 3, """
                Make an attack vs. Fortitude against a living creature within \\rngclose range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\glossterm<blinded> as a \\glossterm<condition>.
                \\crit The target is \\glossterm<blinded> twice by two separate \\glossterm<conditions>.
                    Both conditions must be removed before the target can see again.
            """, tags=['Life']),
            Spell('Bleed', 3, """
                This spell functions like the \\spell<sickening decay> spell, except that a struck target also begins bleeding as an additional \\glossterm<condition>.
                At the end of every \\glossterm<action phase> in subsequent rounds, the target takes slashing \\glossterm<standard damage> -1d.
            """, tags=['Life']),
            Spell('Crippling Decay', 3, """
                This spell functions like the \\spell<sickening decay> spell, except that a struck target is also \\glossterm<decelerated> as an additional \\glossterm<condition>.
            """, tags=['Life']),
        ],
        rituals=[
            Spell('Animate Dead', 2, """
                Choose any number of corpses within \\rngclose range.
                The combined levels of all targets cannot exceed your \\glossterm<power>.
                The target becomes an undead creature that obeys your spoken commands.
                You choose whether to create a skeleton or a zombie.
                Creating a zombie require a mostly intact corpse, including most of the flesh.
                Creating a skeleton only requires a mostly intact skeleton.
                If a skeleton is made from an intact corpse, the flesh quickly falls off the animated bones.

                This ritual takes one hour to perform.
            """, tags=['Attune (ritual)']),
        ],
        category='debuff, combat',
    ))

    # Primary: damage
    # Secondary: debuff
    # Tertiary: buff
    # None: utility
    mystic_spheres.append(MysticSphere(
        name='Cryomancy',
        short_description='Drain heat to injure and freeze foes',
        cantrips=[Effects('Chill', """
            Make an attack vs. Fortitude against one creature or object within \\rngmed range.
            \\hit The target takes cold \\glossterm<standard damage>.
        """, tags=['Cold'], ap_cost=False)],
        schools=['Evocation'],
        lists=['Arcane', 'Nature', 'Pact'],
        spells=[
            Spell('Cone of Cold', 1, """
                Make an attack vs. Fortitude against everything in a \\areamed cone from you.
                \\hit Each target takes cold \\glossterm<standard damage>, and is \\glossterm<fatigued> as a \\glossterm<condition>.
            """, tags=['Cold']),
            Spell('Greater Cone of Cold', 4, """
                This spell functions like the \\spell<cone of cold> spell, except it affects everything in a \\arealarge cone from you and you gain a +1d bonus to damage.
            """, tags=['Cold']),
            Spell('Supreme Cone of Cold', 7, """
                This spell functions like the \\spell<cone of cold> spell, except it affects everything in a \\areahuge cone from you and you gain a +2d bonus to damage.
            """, tags=['Cold']),
            Spell('Frostbite', 1, """
                Make an attack vs. Fortitude against one creature or object within \\rngmed range.
                \\hit The target takes cold \\glossterm<standard damage> +2d.
            """, tags=['Cold']),
            Spell('Greater Frostbite', 3, """
                This spell functions like the \\spell<frostbite> spell, except that a struck target is also \\glossterm<exhausted> as a \\glossterm<condition>.
            """, tags=['Cold']),
            Spell('Cold Snap', 2, """
                This spell functions like the \\spell<cone of cold> spell, except that it gains the \\glossterm<Sustain> (standard) tag.
                The area affected by the spell becomes a \\glossterm<zone> that is supernaturally chilled.
                At the end of each \\glossterm<action phase> in subsequent rounds, the attack is repeated in that area.
            """, tags=['Cold']),
            Spell('Greater Cold Snap', 3, f"""
                This spell functions like the \\textit<cold snap> spell, except that the spell gains the \\glossterm<Sustain> (minor) tag instead of the \\glossterm<Sustain> (standard) tag.
            """, tags=['Cold']),
            Spell('Freezing Cone', 3, """
                This spell functions like the \\spell<cone of cold> spell, except that you gain a +1d bonus to damage and each struck target is \\glossterm<exhausted> instead of \\glossterm<fatigued>.
            """, tags=['Cold']),
            Spell('Blizzard', 2, """
                This spell functions like the \\spell<cone of cold> spell, except that the area becomes a \\areamed radius from you.
            """, tags=['Cold']),
            Spell('Deep Freeze', 3, """
                This spell functions like the \\spell<cone of cold> spell, except that it attacks Reflex defense instead of Fortitude defense.
            """, tags=['Cold']),
            Spell('Icecraft', 1, """
                Choose a pool of unattended, nonmagical water within \\rngclose range.
                This spell creates an icy weapon or a suit of icy armor from the target pool of water.
                You can create any weapon, shield, or body armor that you are proficient with, and which would normally be made entirely from metal, except for heavy body armor.
                The pool of water targeted must be at least as large as the item you create.

                The item functions like a normal item of its type, except that it is more fragile.
                It has hit points equal to twice your \\glossterm<power>, does not have any \\glossterm<hardness>, and is \\glossterm<vulnerable> to fire damage.
                If the item would take cold damage, it instead heals that many hit points.

                When a creature wearing armor created in this way takes physical damage, cold damage, or fire damage, that damage is also dealt to the armor.
                Likewise, when a creature wielding a weapon created in this way deals damage with the weapon, that damage is also dealt to the weapon.
                If the item loses all of its hit points, this effect is \\glossterm<dismissed>.
            """, tags=['Attune (self)', 'Cold']),
            Spell('Sturdy Icecraft', 2, """
                This spell functions like the \\spell<icecraft> spell, except that the item created has hit points equal to four times your \\glossterm<power>.
                In addition, you can create heavy body armor.
            """, tags=['Attune (self)', 'Cold']),
            Spell('Enhanced Icecraft', 4, """
                This spell functions like the \\spell<sturdy icecraft> spell, except that the item created is magically enhanced.
                A weapon gains a +1d \\glossterm<magic bonus> to damage with \\glossterm<strikes>, and armor grants a +1 \\glossterm<magic bonus> to the defenses it improves.
            """, tags=['Attune (self)', 'Cold']),
        ],
        category='damage',
    ))

    # Primary: debuff
    # Secondary: damage
    # Tertiary: utility
    # None: buff
    mystic_spheres.append(MysticSphere(
        name="Delusion",
        short_description="Instill false emotions to influence creatures",
        cantrips=[Effects('Cause Fear', """
            Make an attack vs. Mental against a creature within \\rngmed range.
            \\hit The target is \\glossterm<shaken> by you as a \\glossterm<condition>.
            \\crit The target is \\glossterm<frightened> by you as a \\glossterm<condition>.
        """, tags=['Emotion', 'Mind'], ap_cost=False)],
        schools=['Enchantment'],
        lists=['Arcane', 'Divine', 'Pact'],
        spells=[
            Spell('Terror', 1, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\frightened by you as a \\glossterm<condition>.
                \\crit The target is \\panicked by you as a \\glossterm<condition>.
            """, tags=['Emotion', 'Mind']),
            Spell('Fearsome Aura', 1, """
                You radiate an aura of fear in a \\arealarge radius emanation.
                When you attune to this spell, and at the end of each \\glossterm<action phase> in subsequent rounds, make an attack vs. Mental against all creatures in the area that you did not already attack with this spell.
                \\hit Each target is \\glossterm<shaken> by you as a \\glossterm<condition>.
            """, tags=['Attune (self)', 'Emotion', 'Mind']),
            Spell('Greater Fearsome Aura', 4, """
                This spell functions like the \\spell<fearsome aura> spell, except that a struck target is \\glossterm<frightened> instead of \\glossterm<shaken>.
            """, tags=['Attune (self)', 'Emotion', 'Mind']),
            # Math: at 1st level, power is probably ~2, so standard damage is probably 2d6.
            # Casting this spell and then two standard damage spells deals 4d6+2d8 = 23 damage
            # casting three standard damage spells deals 6d6 = 21 damage
            # So when fighting alone, this takes 3 rounds of effectiveness to be equal
            # in power to a simple damage spell.

            # At 20th level, power is ~22, so standard damage is 9d10
            # Casting this spell and then two standard damage spells deals 18d10+7d10=25d10
            # Casting three standard damage spells deals 27d10
            Spell('Agony', 1, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is inflicted with agonizing pain as a \\glossterm<condition>.
                It suffers a -2 penalty to Mental defense.
                % Does this need to clarify that it takes effect in the round the spell was cast?
                In addition, at the end of each \\glossterm<delayed action phase>, if the target took damage that round, it takes \\glossterm<standard damage> -1d.
                This damage is of all damage types that the target was damaged by during that round.
            """, tags=['Emotion', 'Mind']),
            Spell('Redirected Terror', 2, """
                This spell functions like the \\spell<terror> spell, except that you also choose a willing ally within the spell's range.
                The target is afraid of the chosen ally instead of being afraid of you.
            """, tags=['Emotion', 'Mind']),
            Spell('Charm', 2, """
                Make an attack vs. Mental against a creature within \\rnglong range.
                If the target thinks that you or your allies are threatening it, you take a -5 penalty to accuracy on the attack.
                \\hit The target is \\charmed by you.
                Any act by you or your apparent allies that threatens or damages the \\spell<charmed> person breaks the effect.
                This effect is automatically \\glossterm<dismissed> after one hour.
                \\crit As above, except that the effect is not automatically dismissed.
            """, tags=['Attune (self)', 'Emotion', 'Mind', 'Subtle']),
            Spell('Amnesiac Charm', 5, """
                This spell functions like the \\spell<charm> spell, except that when the spell ends, an affected target forgets all events that transpired during the spell's duration.
                It becomes aware of its surroundings as if waking up from a daydream.
                The target is not directly aware of any magical influence on its mind, though unusually paranoid or perceptive creatures may deduce that their minds were affected.
            """, tags=['Attune (self)', 'Emotion', 'Mind', 'Subtle']),
            Spell('Calm Emotions', 3, """
                Make an attack vs. Mental against all creatures within a \\arealarge radius from you.
                \\hit Each target has its emotions calmed.
                The effects of all other \\glossterm<Emotion> abilities on that target are \\glossterm<suppressed>.
                It cannot take violent actions (although it can defend itself) or do anything destructive.
                If the target takes damage or feels that it is in danger, this effect is \\glossterm<dismissed>.
            """, tags=['Emotion', 'Mind', 'Sustain (standard)']),
            Spell('Enrage', 1, """
                Make an attack vs. Mental with a +2 bonus to \\glossterm<accuracy> against a creature within \\rngmed range.
                \\hit As a \\glossterm<condition>, the target is unable to take any \\glossterm<standard actions> that do not cause it to make an attack.
                For example, it could make a \\glossterm<strike> or cast an offensive spell, but it could not heal itself or summon an ally.
                This cannot prevent it from taking the \\textit<recover> or \\textit<desperate recovery> actions.
            """, tags=['Emotion', 'Mind']),
            Spell('Mass Enrage', 4, """
                This spell functions like the \\spell<enrage> spell, except that it affects all enemies within a \\areamed radius.
            """, tags=['Emotion', 'Mind']),
            Spell('Inevitable Doom', 4, """
                This spell functions like the \\spell<terror> spell, except that you gain a +2 bonus to \\glossterm<accuracy>.
            """, tags=['Emotion', 'Mind']),
        ],
        category='debuff, combat',
    ))

    # Primary: damage
    # Secondary: debuff
    # Tertiary: buff
    # None: utility
    mystic_spheres.append(MysticSphere(
        name="Electromancy",
        short_description='Create electricity to injure and stun foes',
        cantrips=[Effects('Spark', """
            Make an attack vs. Fortitude against everything in a \\areamed, 5 ft.\\ wide line from you.
            \\hit Each target takes electricity \\glossterm<standard damage> -1d.
        """, tags=['Electricity'], ap_cost=False)],
        schools=['Evocation'],
        lists=['Arcane', 'Nature', 'Pact'],
        spells=[
            Spell('Lightning Bolt', 1, """
                Make an attack vs. Fortitude against everything in a \\arealarge, 10 ft.\\ wide line from you.
                \\hit Each target takes electricity \\glossterm<standard damage>.
            """, tags=['Electricity']),
            # A little weird that "Shocking" Grasp doesn't daze
            Spell('Shocking Grasp', 1, """
                Make an attack vs. Fortitude against one creature or object you \\glossterm<threaten>.
                You gain a +4 bonus to \\glossterm<concentration> checks to cast this spell.
                \\hit The target takes electricity \\glossterm<standard damage> +2d.
            """, tags=['Electricity']),
            Spell('Uncontrolled Discharge', 2, """
                Make an attack vs. Fortitude against everything in a \\areamed radius from you.
                \\hit Each target takes electricity \\glossterm<standard damage>.
            """, tags=['Electricity']),
            Spell('Magnetic', 2, """
                This spell functions like the \\spell<lightning bolt> spell, except that you gain a +2 bonus to accuracy against targets wearing metal armor or otherwise carrying or composed of a significant amount of metal.
            """, tags=['Electricity']),
            Spell('Magnetic Blade', 3, """
                Choose a willing creature within \\rngclose range.
                Metal weapons wielded by the target gain a +2 \\glossterm<magic bonus> to \\glossterm<accuracy> against targets wearing metal armor or otherwise carrying or composed of a significant amount of metal.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Electricity']),
            Spell('Greater Magnetic Blade', 6, """
                This spell functions like the \\spell<magnetic blade> spell, except that the bonus is increased to +3.
            """, tags=['Attune (self)', 'Electricity']),
            Spell('Dynamo', 2, """
                This spell functions like the \\spell<lightning bolt> spell, except that it gains the \\glossterm<Sustain> (standard) tag.
                The area affected by the spell becomes a \\glossterm<zone> that is continuously filled with electrical pulses.
                At the end of each \\glossterm<action phase> in subsequent rounds, the attack is repeated in that area.
            """, tags=['Electricity']),
            Spell('Greater Dynamo', 3, f"""
                This spell functions like the \\textit<dynamo> spell, except that the spell gains the \\glossterm<Sustain> (minor) tag instead of the \\glossterm<Sustain> (standard) tag.
            """, tags=['Electricity']),
            Spell('Chain Lightning', 4, """
                Make an attack vs. Fortitude against one creature or object within \\rngmed range.
                \\hit The target takes electricity \\glossterm<standard damage> +3d.
                In addition, make an additional attack vs. Fortitude against any number of creatures in a \\areamed radius from the struck target.
                \\hit Each secondary target takes electricity \\glossterm<standard damage> +1d.
            """, tags=['Electricity']),
            Spell('Forked Lightning',3, """
                This spell functions like the \\spell<lightning bolt> spell, except that you gain a +1d bonus to damage.
                In addition, you create two separate line-shaped areas instead of one.
                The two areas can overlap, but targets in the overlapping area are only affected once.
            """, tags=['Electricity']),
            Spell('Shocking Bolt', 3, """
                This spell functions like the \\spell<lightning bolt> spell, except that each struck target is also \\glossterm<dazed> as a \\glossterm<condition>.
            """, tags=['Electricity']),
            Spell('Stunning Bolt', 6, """
                This spell functions like the \\spell<lightning bolt> spell, except that each struck target is also \\glossterm<stunned> as a \\glossterm<condition>.
            """, tags=['Electricity']),
            Spell('Call Lightning', 2, """
                Make an attack vs. Fortitude against everything in a \\arealarge, 5 ft.\\ wide vertical line within \\rngmed range.
                If you are outdoors in cloudy or stormy weather, you gain a +2 bonus to \\glossterm<accuracy> with the attack.
                If this spell has its area increased, such as with the Widened \\glossterm<augment>, only the length of the line increases.
                \\hit Each target takes takes electricity \\glossterm<standard damage> +2d.
            """, tags=['Electricity']),
        ],
        category='damage',
    ))

    # To restrict the narrative scope of Fabrication, it should be able to
    # create any kind of object, but it can't manipulate objects in specific
    # ways after their creation.

    # Primary: damage
    # Secondary: utility
    # Tertiary: debuff
    # None: buff
    mystic_spheres.append(MysticSphere(
        name='Fabrication',
        short_description="Create objects to damage and impair foes",
        # TODO: Narrative implications of at-will acid are annoying
        cantrips=[
            Effects('Acid Splash', """
                Make an attack vs. Armor against one creature or object within \\rngmed range.
                \\hit The target takes acid \\glossterm<standard damage>.
            """, tags=['Acid', 'Manifestation'], ap_cost=False),
            Effects('Fabricate Trinket', """
                You make a Craft check to create an object of Tiny size or smaller.
                The object appears in your hand or at your feet.
                It must be made of nonliving, nonmagical, nonreactive vegetable matter, such as wood or cloth.
            """, tags=['Attune (self)', 'Manifestation'], ap_cost=False),
        ],
        schools=['Conjuration'],
        lists=['Arcane', 'Pact'],
        spells=[
            Spell('Acid Orb', 1, """
                Make an attack vs. Armor against one creature or object within \\rngmed range.
                \\hit The target takes acid \\glossterm<standard damage> +2d.
            """, tags=['Acid', 'Manifestation']),
            Spell('Forge', 1, """
                Choose a type of weapon or shield that you are proficient with.
                You create a normal item of that type anywhere within \\rngclose range.

                The item cannot be constructed of any magical or extraordinary material.
                % This should allow the Giant augment; is this worded to allow that?
                It is sized appropriately for you, up to a maximum of a Medium size item.
            """, tags=['Attune (self)']),
            Spell('Greater Forge', 2, """
                This spell functions like the \\spell<forge> spell, except that you can also create any type of body armor you are proficient with.
                If you create body armor, you can create it already equipped to a willing creature within range.
            """, tags=['Attune (self)']),
            Spell('Corrosive Orb', 3, """
                This spell functions like the \\spell<acid orb> spell, except that you gain a +1d bonus to damage and it deals double damage to objects.
            """, tags=['Acid', 'Manifestation']),
            Spell('Meteor', 3, """
                You create a meteor in midair within \\rngmed range that falls to the ground, crushing foes in its path.
                The meteor takes up a \\areamed radius, and must be created in unoccupied space.
                After being summoned, it falls up to 100 feet before disappearing.
                Make an attack vs. Armor against everything in its path.
                \\hit Each target takes bludgeoning and fire \\glossterm<standard damage>.
            """, tags=['Manifestation']),
            Spell('Meteor Storm', 5, f"""
                This spell functions like the \\textit<meteor> spell, except that you can create up to five different meteors within \\rnglong range.
                The areas affected by two different meteors cannot overlap.
                If one of the meteors is created in an invalid area, that meteor is not created, but the others are created and dealt their damage normally.
            """, tags=['Manifestation']),
            Spell('Lingering Acid Orb', 3, f"""
                This spell functions like the \\spell<acid orb> spell, except that the acid lingers on a struck target.
                At the end of each \\glossterm<action phase> in subsequent rounds, the target takes acid \\glossterm<standard damage>.
                This is a \\glossterm<condition>, and lasts until removed.
            """, tags=['Acid', 'Manifestation']),
            Spell('Web', 2, """
                You fill a \\areasmall radius zone in \\rngclose range with webs.
                The webs make the area \\glossterm<difficult terrain>.
                Each 5-ft.\\ square of webbing has hit points equal to your \\glossterm<power>, and is \\glossterm<vulnerable> to fire.

                In addition, you make an attack vs. Reflex against all Large or smaller creatures in the area when the spell is cast.
                \\hit Each target is \\glossterm<immobilized> as long as it has webbing from this ability in its space.
            """, tags=['Manifestation', 'Sustain (minor)']),
            Spell('Reinforced Webbing', 3, f"""
                This spell functions like the \\textit<web> spell, except that each 5-ft.\\ square of webbing gains additional hit points equal to your \\glossterm<power>.
                In addition, the webs are no longer \\glossterm<vulnerable> to fire damage.
            """, tags=['Manifestation', 'Sustain (minor)']),
            Spell('Poison', 2, """
                Make an attack vs. Fortitude against a creature within \\rngmed range.

                \\hit The target takes poison \\glossterm<standard damage> +1d and is poisoned as a \\glossterm<condition>.
                If the target is poisoned, repeat this attack at the end of each \\glossterm<action phase> after the first round.
                On the second hit, the target takes poison \\glossterm<standard damage> and becomes \\glossterm<sickened>.
                On the third hit, the target takes poison \\glossterm<standard damage> +2d and becomes \\glossterm<nauseated> instead of sickened.
                After the third hit, no further attacks are made, but the target remains nauseated until the condition is removed.
            """, tags=['Manifestation', 'Poison']),
        ],
        rituals=[
            Spell('Manifest Object', 2, """
                Make a Craft check to create an object of Small size or smaller.
                The object appears out of thin air in an unoccupied square within \\rngclose range.
                % TODO: add ability to create objects of other sizes/materials
                It must be made of nonliving, nonmagical, nonreactive vegetable matter, such as wood or cloth.

                This ritual takes one hour to perform.
            """, tags=['Attune (ritual)', 'Manifestation']),
            Spell('Create Sustenance', 2, """
                Choose an unoccupied square within \\rngclose range.
                This ritual creates food and drink in that square that is sufficient to sustain two Medium creatures per \\glossterm<power> for 24 hours.
                The food that this ritual creates is simple fare of your choice -- highly nourishing, if rather bland.

                This ritual takes one hour to perform.
            """, tags=['Creation']),
        ],
        category='damage',
    ))

    # Primary: buff
    # Secondary: utility
    # None: damage, debuff
    mystic_spheres.append(MysticSphere(
        name="Glamer",
        short_description="Change how creatures and objects are perceived",
        cantrips=[
            Effects('Assist Disguise', """
                Choose a willing creature within \\rngclose range.
                % TODO: wording?
                If the target is disguised as another creature, it gains a +2 \\glossterm<magic bonus> to the result of the disguise.
            """, tags=['Sensation', 'Visual'], ap_cost=False),
            Effects('Blur Weapon', """
                Choose a willing creature within \\rngclose range.
                The target's weapons become blurred and harder to see, making its attacks harder to avoid.
                On the next melee \\glossterm<strike> the target makes, it rolls twice and takes the higher result.
                This effect ends at the end of the next round if the target has not made a strike by that time.

                This effect provides no offensive benefit against creatures immune to \\glossterm<Visual> abilities.
            """, tags=['Sensation', 'Visual'], ap_cost=False),
        ],
        schools=['Illusion'],
        lists=['Arcane'],
        spells=[
            Spell('Blur', 1, """
                Choose a willing creature within \\rngmed range.
                The target's physical outline is distorted so it appears blurred, shifting, and wavering.
                It gains a +1 \\glossterm<magic bonus> to Armor defense and Stealth (see \\pcref<Stealth>).
                This effect provides no defensive benefit against creatures immune to \\glossterm<Visual> abilities.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Sensation', 'Visual']),
            Spell('Hidden Blade', 1, """
                You can only cast this spell during the \\glossterm<action phase>.
                Choose a willing creature within \\rngclose range.
                The target's weapons become invisible, and its hands are blurred.
                On the next melee \\glossterm<strike> the target makes,
                    the attack roll automatically \\glossterm<explodes>,
                    as if the target was \\glossterm<unaware> of the attack.
                This effect ends at the end of the current round if the target has not made a strike by that time.
                % TODO: wording
                The target is not actually \\glossterm<unaware> of the attack, and this does not work with abilities that have effects if the target is unaware of attacks.

                This effect provides no offensive benefit against creatures immune to \\glossterm<Visual> abilities.
            """, tags=['Sensation', 'Visual']),
            Spell('Suppress Light', 1, """
                Choose a Small or smaller unattended object within \\rngclose range.
                This spell suppresses light in a \\areamed radius emanation from the target.
                Light within or passing through the area is dimmed to be no brighter than shadowy illumination.
                Any object or effect which blocks light also blocks this spell's emanation.
            """, tags=['Attune (self)', 'Light', 'Sensation']),
            Spell('Disguise Image', 2, """
                Choose a willing creature within \\rngclose range.
                You make a Disguise check to alter the target's appearance (see \\pcref<Disguise Creature>).
                You gain a +5 bonus on the check, and you can freely alter the appearance of the target's clothes and equipment, regardless of their original form.
                However, this effect is unable to alter the sound, smell, texture, or temperature of the target or its clothes and equipment.
            """, tags=['Attune (target)', 'Sensation', 'Visual']),
            Spell('Mirror Image', 2, """
                Choose a willing creature within \\rngclose range.
                Four illusory duplicates appear around the target that mirror its every move.
                The duplicates shift chaotically in its space, making it difficult to identify the real creature.

                All \\glossterm<targeted> \\glossterm<physical attacks> against the target have a 50\\% miss chance.
                When an attack misses in this way, it affects an image, destroying it.
                This ability provides no defensive benefit against creatures immune to \\glossterm<Visual> abilities.
            """, tags=['Attune (target)', 'Sensation', 'Visual']),
            Spell('Greater Mirror Image', 4, """
                This spell functions like the \\textit<mirror image> spell, except that destroyed images can reappear.
                At the end of each \\glossterm<action phase>, one destroyed image reappears, to a maximum of four images.
            """, tags=['Attune (target)', 'Sensation', 'Visual']),
            Spell('Shadow Mantle', 3, """
                This spell functions like the \\spell<blur> spell, except that the spell's deceptive nature extends beyond altering light to affect the nature of reality itself.
                The defense bonus it provides applies to all defenses.
                In addition, the spell loses the \\glossterm<Visual> tag, and can protect against attacks from creatures immune to Visual abilities.
            """, tags=['Attune (target)', 'Sensation', 'Visual']),
            Spell('Displacement', 6, """
                Choose a willing creature within \\rngmed range.
                The target's image appears to be two to three feet from its real location.
                \\glossterm<Targeted> \\glossterm<physical attacks> against the target suffer a 50\\% miss chance.
                This ability provides no defensive benefit against creatures immune to \\glossterm<Visual> abilities.
            """, tags=['Attune (target)', 'Sensation', 'Visual']),
        ],
        rituals=[
            Spell('Magic Mouth', 1, """
                Choose a Large or smaller willing creature or unattended object within \\rngclose range.
                In addition, choose a triggering condition and a message of twenty-five words or less.
                The condition must be something that a typical human in the target's place could detect.

                When the triggering condition occurs, the target appears to grow a magically animated mouth.
                The mouth speaks the chosen message aloud.
                After the message is spoken, this effect is \\glossterm<dismissed>.

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)', 'Sensation']),
        ],
        category='buff, defense',
    ))

    # Primary: damage
    # Secondary: buff
    # Tertiary: utility
    # None: debuff
    mystic_spheres.append(MysticSphere(
        name="Polymorph",
        short_description="Change the physical forms of objects and creatures",
        cantrips=[
            Effects('Twist Body', """
                Make an attack vs. Fortitude against a creature within \\rngmed range.
                \\hit The target takes physical \\glossterm<standard damage>.
            """, tags=['Shaping'], ap_cost=False),
            Effects('Alter Object', """
                Choose an unattended, nonmagical object you can touch.
                You make a Craft check to alter the target (see \\pcref<Craft>), except that you do not need any special tools to make the check (such as an anvil and furnace).
                The maximum hardness of a material you can affect with this ability is equal to your \\glossterm<power>.

                % too short?
                Each time you use this ability, you can accomplish work that would take up to five minutes with a normal Craft check.
            """, tags=['Shaping'], ap_cost=False),
        ],
        schools=['Transmutation'],
        lists=['Arcane', 'Nature', 'Pact'],
        spells=[
            Spell('Baleful Polymorph', 1, """
                Make an attack vs. Fortitude against a creature within \\rngmed range.
                \\hit The target takes physical \\glossterm<standard damage> +2d.
            """, tags=['Shaping']),
            Spell('Greater Baleful Polymorph', 4, """
                This spell functions like the \\spell<baleful polymorph> spell, except that you gain a +1 bonus to \\glossterm<accuracy> and a struck target is \\glossterm<sickened> as a \\glossterm<condition>.
            """, tags=['Shaping']),
            Spell('Supreme Baleful Polymorph', 7, """
                This spell functions like the \\spell<baleful polymorph> spell, except that you gain a +2 bonus to \\glossterm<accuracy> and a struck target is \\glossterm<nauseated> as a \\glossterm<condition>.
            """, tags=['Shaping']),
            Spell('Shrink', 1, """
                Choose a willing creature within \\rngclose range.
                The target's size decreases by one size category, to a minimum of Tiny.
                This decreases its Strength by 2 and usually decreases its \\glossterm<reach> (see \\pcref<Size in Combat>).

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Shaping', 'Sizing']),
            Spell('Greater Shrink', 4, """
                This spell functions like the \\spell<shrink> spell, except that the target's size decreases by two size categories, to a minimum of Diminuitive.
            """, tags=['Attune (target)', 'Shaping', 'Sizing']),
            Spell('Spider Climb', 1, """
                Choose a willing creature within \\rngclose range.
                The target gains a \\glossterm<climb speed> equal to its \\glossterm<base speed>.
                In addition, it gains a +5 bonus to Climb checks to climb on ceilings and similar surfaces.
            """, tags=['Attune (target)']),
            Spell('Barkskin', 2, """
                Choose a willing creature within \\rngclose range.
                The target gains a \\glossterm<magic bonus> equal to your \\glossterm<power> to \\glossterm<damage reduction> against damage dealt by \\glossterm<physical attacks>.
                In addition, it is \\glossterm<vulnerable> to fire damage.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Regeneration', 4, """
                Choose a willing creature within \\rngclose range.
                A the end of each round, the target heals hit points equal to your \\glossterm<power>.
            """, tags=['Attune (target)']),
            Spell('Greater Regeneration', 7, """
                This spell functions like the \\textit<regeneration> spell, except that the healing is equal to twice your \\glossterm<power>.
            """, tags=['Attune (target)']),
            # Should this also/instead be under Terramancy?
            Spell('Stoneskin', 3, """
                Choose a willing creature within \\rngclose range.
                The target gains a \\glossterm<magic bonus> equal to your \\glossterm<power> to \\glossterm<damage reduction> against damage dealt by \\glossterm<physical attacks>, except for damage from adamantine weapons.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Ironskin', 6, """
                This spell functions like the \\textit<stoneskin> spell, except that the bonus is equal to twice your \\glossterm<power>.
            """, tags=['Attune (target)']),
            Spell('Enlarge', 3, """
                Choose a Large or smaller willing creature within \\rngclose range.
                The target's size increases by one size category.
                This increases its \\glossterm<overwhelm value>, \\glossterm<overwhelm resistance>, and usually increases its \\glossterm<reach> (see \\pcref<Size in Combat>).
                However, the target's muscles are not increased fully to match its new size, and its Strength is unchanged.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Shaping', 'Sizing']),
            Spell('Enlarge, Greater', 5, """
                This spell functions like the \\textit<enlarge> spell, except that the target gains a +2 \\glossterm<magic bonus> to Strength to match its new size.
            """, tags=['Attune (target)', 'Shaping', 'Sizing']),
            Spell('Enlarge, Supreme', 7, """
                This spell functions like the \\spell<enlarge> spell, except that the target's size is increased by two size categories.
                It gains a +2 \\glossterm<magic bonus> to Strength to partially match its new size.
            """, tags=['Attune (target)', 'Shaping', 'Sizing']),
            Spell('Alter Appearance', 2, """
                Choose a Large or smaller willing creature within \\rngclose range.
                You make a Disguise check to alter the target's appearance (see \\pcref<Disguise Creature>).
                You gain a +5 bonus on the check, and you ignore penalties for changing the target's gender, species, subtype, or age.
                However, this effect is unable to alter the target's clothes or equipment in any way.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Shaping']),
            Spell('Craft Object', 3, """
                Choose any number of unattended, nonmagical objects within \\rngclose range.
                You make a Craft check to transform the targets into a new item (or items) made of the same materials.
                You require none of the tools or time expenditure that would normally be necessary.
                The total size of all targets combined must be Large size or smaller.

                You can apply the Giant \\glossterm<augment> to this spell.
                If you do, it increases the maximum size of all targets combined.
            """, tags=['Shaping']),
            Spell('Disintegrate', 5, """
                Make an attack vs. Fortitude against a creature within \\rngmed range.
                \\hit The target takes physical \\glossterm<standard damage> +4d.
                In addition, if the target has no hit points remaining, it dies.
                Its body is completely disintegrated, leaving behind only a pinch of fine dust.
                Its equipment is unaffected.
            """, tags=['Shaping']),
        ],
        rituals=[
            # Should this also be a spell? Incredibly niche, but golem makers
            # would want it...
            Spell('Mending', 1, """
                % TODO: unattended or attended by a willing creature
                Choose an unattended object within \\rngclose range.
                The target is healed for hit points equal to \\glossterm<standard damage> +2d.

                This ritual takes one minute to perform.
            """, tags=['Shaping']),
            Spell('Fortify', 1, """
                Choose an unattended, nonmagical object or part of an object of up to Large size.
                Unlike most abilities, this ritual can affect individual parts of a whole object.

                % How should this affect Strength break DRs?
                The target gains a +5 \\glossterm<magic bonus> to \\glossterm<hardness>.
                If the target is moved, this effect ends.
                Otherwise, it lasts for one year.

                This ritual takes one hour to perform.
            """, tags=['Attune (ritual)']),
            Spell('Enduring Fortify', 3, """
                This ritual functions like the \\spell<fortify> ritual, except that the effect lasts for one hundred years.
            """, tags=[]),
            Spell('Greater Enduring Fortify', 5, """
                This ritual functions like the \\spell<greater fortify> ritual, except that the effect lasts for one hundred years.
            """, tags=[]),
            Spell('Greater Fortify', 3, """
                This ritual functions like the \\spell<fortify> ritual, except that the \\glossterm<hardness> bonus increases to 10.
            """, tags=['Attune (ritual)']),
            Spell('Supreme Fortify', 6, """
                This ritual functions like the \\spell<fortify> ritual, except that the \\glossterm<hardness> bonus increases to 15.
            """, tags=['Attune (ritual)']),
            Spell('Awaken', 5, """
                Choose a Large or smaller willing animal within \\rngclose range.
                The target becomes sentient.
                Its Intelligence becomes 1d6 - 5.
                Its type changes from animal to magical beast.
                It gains the ability to speak and understand one language that you know of your choice.
                Its maximum age increases to that of a human (rolled secretly).
                This effect is permanent.

                This ritual takes 24 hours to perform, and requires 50 action points from its participants.
                It can only be learned with the nature \\glossterm<magic source>.
            """, tags=[]),
            Spell('Ironwood', 3, """
                Choose a Small or smaller unattended, nonmagical wooden object within \\rngclose range.
                The target is transformed into ironwood.
                While remaining natural wood in almost every way, ironwood is as strong, heavy, and resistant to fire as iron.
                Metallic armor and weapons, such as full plate, can be crafted from ironwood.

                % Should this have an action point cost? May be too rare...
                This ritual takes 24 hours to perform.
            """, tags=['Shaping']),
            Spell('Purify Sustenance', 1, """
                All food and water in a single square within \\rngclose range is purified.
                Spoiled, rotten, poisonous, or otherwise contaminated food and water becomes pure and suitable for eating and drinking.
                This does not prevent subsequent natural decay or spoiling.

                This ritual takes one hour to perform.
            """, tags=['Shaping']),
        ],
        category='damage',
    ))

    # Too narrow?
    # Primary: debuff
    # Secondary: utility
    # None: buff, damage
    mystic_spheres.append(MysticSphere(
        name="Photomancy",
        short_description="Create bright light to blind foes and illuminate your surroundings",
        cantrips=[
            Effects('Flash', """
                Make an attack vs. Fortitude against one creature, object, or location within \\rngmed range.
                Bright light illuminates a 100 foot radius around the target until the end of the round.
                \\hit The target is \\dazzled as a \\glossterm<condition>.
                \\crit As above, and target is also \\dazed as an additional \\glossterm<condition>.
            """, tags=['Light', 'Sensation', 'Visual'], ap_cost=False),
            Effects('Illuminate', """
                Choose a location within \\rngmed range.
                A glowing light appears in midair in the chosen location.
                It casts bright light in a 20 foot radius and dim light in a 40 foot radius.
                This effect lasts until you use it again or until you \\glossterm<dismiss> it as a \\glossterm<free action>.
            """, tags=['Light', 'Sensation', 'Visual'], ap_cost=False),
        ],
        schools=['Illusion'],
        lists=['Arcane', 'Divine', 'Nature', 'Pact'],
        spells=[
            Spell('Flare', 1, """
                A burst of light light fills a \\areasmall radius within \\rngmed range of you.
                Bright light illuminates a 100 foot radius around the area until the end of the round.
                Make an attack vs. Fortitude against all creatures in the source area.
                \\hit Each target is \\dazzled as a \\glossterm<condition>.
                \\crit As above, and target is also \\dazed as an additional \\glossterm<condition>.
            """, tags=['Light', 'Sensation', 'Visual']),
            Spell('Kaleidoscopic Pattern', 4, """
                This spell creates a brilliant, rapidly shifting rainbow of lights in a \\areasmall radius within \\rngmed range of you.
                They illuminate a 100 foot radius around the area with bright light until the end of the round.
                Make an attack vs. Mental against all creatures in the source area.
                \\hit Each target is \\disoriented as a \\glossterm<condition>.
                \\crit Each target is \\confused as a \\glossterm<condition>.
            """, tags=['Light', 'Mind', 'Sensation', 'Visual']),
            Spell('Faerie Fire', 2, """
                This spell functions like the \\spell<flare> spell, except that each struck target is surrounded with a pale glow made of hundreds of ephemeral points of light.
                This causes the struck target to radiate bright light in a 5 foot radius, as a candle.
                The lights impose a -10 penalty to the Stealth skill.
                In addition, they reveal the outline of the creatures if they become \\glossterm<invisible>.
                This allows observers to see their location, though not to see them perfectly.
            """, tags=['Light', 'Sensation', 'Visual']),
            Spell('Illuminating', 2, """
                This spell functions like the \\spell<flare> spell, except that it gains the \\glossterm<Sustain> (minor) tag.
                The area affected by the spell becomes an illuminated \\glossterm<zone>.
                At the end of each \\glossterm<action phase> in subsequent rounds, the attack is repeated in that area.
            """, tags=['Light', 'Sensation', 'Visual']),
            Spell('Flashbang', 3, """
                This spell functions like the \\spell<flare> spell, except that an intense sound accompanies the flash of light caused by the spell.
                Each struck target is also \\glossterm<deafened> as an additional \\glossterm<condition>.
                This spell gains the \\glossterm<Auditory> tag in addition to the tags from the \\spell<flare> spell.
            """, tags=['Light', 'Sensation', 'Visual']),
            Spell('Blinding', 4, """
                This spell functions like the \\spell<flare> spell, except that each struck target is \\glossterm<blinded> instead of \\glossterm<dazzled>.
            """, tags=['Light', 'Sensation', 'Visual']),
            Spell('Pillars of Light', 3, """
                This spell functions like the \\spell<flare> spell, except that you gain a +1 bonus to \\glossterm<accuracy>.
                In addition, it affects up to five different \\areasmall radius, 50 ft. tall cylinders within range.
                The areas can overlap, but targets in the overlapping area are only affected once.
            """, tags=['Light', 'Sensation', 'Visual']),
            Spell('Solar Flare', 4, """
                This spell functions like the \\spell<flare> spell, except that you gain a +2 bonus to \\glossterm<accuracy>.
                In addition, the light is treated as being natural sunlight for the purpose of abilities.
                This can allow it to destroy vampires and have similar effects.
            """, tags=['Light', 'Sensation', 'Visual']),
            Spell('Greater Solar Flare', 7, """
                This spell functions like the \\spell<solar flare> spell, except that the accuracy bonus is increased to +4.
            """, tags=['Light', 'Sensation', 'Visual']),
        ],
        rituals=[
            Spell('Mobile Light', 1, """
                Choose a Medium or smaller willing creature or unattended object within \\rngclose range.
                The target glows like a torch, shedding bright light in a \\areamed radius (and dim light for an additional 20 feet).

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)', 'Light', 'Sensation']),
            Spell('Permanent Light', 2, """
                This ritual functions like the \\spell<light> ritual, except that it loses the \\glossterm<Attune> (ritual) tag and the effect lasts permanently.
                This ritual takes 24 hours to perform, and it requires 8 action points from its participants.
            """, tags=['Light', 'Sensation']),
        ],
        category='debuff, combat',
    ))

    # Primary: damage
    # Tertiary: buff, debuff
    # None: utility
    mystic_spheres.append(MysticSphere(
        name='Pyromancy',
        short_description="Create fire to incinerate foes",
        cantrips=[
            Effects('Personal Torch', """
                You create a flame in your hand.
                You can create it at any intensity, up to a maximum heat equivalent to a burning torch.
                At it most intense, it sheds bright light in a 20 foot radius and dim light in an 40 foot radius.
                If you touch a creature or object with it, the target takes fire \\glossterm<standard damage> -2d.
                This effect lasts until you use it again or until you \\glossterm<dismiss> it as a \\glossterm<free action>.
            """, tags=['Fire'], ap_cost=False),
            Effects('Scorch', """
                Make an attack vs. Armor against one creature or object within \\rngmed range.
                \\hit The target takes fire \\glossterm<standard damage>.
            """, tags=['Fire'], ap_cost=False),
        ],
        schools=['Evocation'],
        lists=['Arcane', 'Fire', 'Nature', 'Pact'],
        spells=[
            Spell('Fireburst', 1, """
                Make an attack vs. Armor against everything in a \\areasmall radius within \\rngmed range.
                \\hit Each target takes fire \\glossterm<standard damage>.
            """, tags=['Fire']),
            Spell('Firebolt', 1, """
                Make an attack vs. Armor against one creature within \\rngmed range.
                \\hit The target takes fire \\glossterm<standard damage> +2d.
            """, tags=['Fire']),
            Spell('Burning Hands', 2, f"""
                Make an attack vs. Armor against everything in a \\arealarge cone from you.
                \\hit Each target takes fire \\glossterm<standard damage>.
            """, tags=['Fire']),
            Spell('Blast Furnace', 2, f"""
                This spell functions like the \\spell<fireburst> spell, except that it gains the \\glossterm<Sustain> (standard) tag.
                The area affected by the spell becomes a \\glossterm<zone> that is continuously engulfed in flames.
                At the end of each \\glossterm<action phase> in subsequent rounds, the attack is repeated in that area.
            """, tags=['Fire']),
            Spell('Fireball', 3, """
                Make an attack vs. Armor against everything in a \\areamed radius within \\rnglong range.
                \\hit Each target takes fire \\glossterm<standard damage>.
            """, tags=['Fire']),
            Spell('Greater Fireball', 6, """
                This spell functions like the \\spell<fireball> spell, except that it affects everything in a \\arealarge radius and you gain a +1d bonus to damage.
            """, tags=['Fire']),
            Spell('Greater Blast Furnace', 3, f"""
                This spell functions like the \\spell<blast furnace> spell, except that the spell gains the \\glossterm<Sustain> (minor) tag instead of the \\glossterm<Sustain> (standard) tag.
            """, tags=['Fire']),
            Spell('Ignition', 2, f"""
                This spell functions like the \\spell<fireburst> spell, except that each struck target is also \\glossterm<ignited> as a \\glossterm<condition>.
                This condition can be removed if the target makes a \\glossterm<DR> 10 Dexterity check as a \\glossterm<move action> to put out the flames.
                Dropping \\glossterm<prone> as part of this action gives a +5 bonus to this check.
            """, tags=['Fire']),
            Spell('Greater Ignition', 4, f"""
                This spell functions like the \\spell<fireburst> spell, except that each target hit is also \\glossterm<ignited> as a \\glossterm<condition>.
                In addition, the ignited effect deals fire \\glossterm<standard damage> -2d instead of the normal 1d6 fire damage each round.
            """, tags=['Fire']),
            Spell('Supreme Ignition', 6, f"""
                This spell functions like the \\textit<greater ignition> spell, except that the condition must be removed twice before the effect ends.
            """, tags=['Fire']),
            Spell('Inferno', 3, """
                Make an attack vs. Armor against everything in a \\arealarge radius from you.
                \\hit Each target takes fire \\glossterm<standard damage>.
            """, tags=['Fire']),
            Spell('Greater Inferno', 5, """
                This spell functions like the \\textit<inferno> spell, except that it affects everything in a 200 ft.\\ radius from you.
            """, tags=['Fire']),
            Spell('Superheated Fireburst', 3, """
                This spell functions like the \\spell<fireburst> spell, except that it attacks Reflex defense instead of Armor defense.
            """, tags=['Fire']),
            Spell('Fearsome Flame', 2, f"""
                This spell functions like the \\spell<fireburst> spell, except that the attack result is also compared to each target's Mental defense.
                \\hit Each target is \\glossterm<shaken> by you as a \\glossterm<condition>.
            """, tags=['Emotion', 'Fire', 'Mind']),
            Spell('Flame Serpent', 3, f"""
                Make an attack vs. Armor against everything in a \\arealarge, 5 ft.\\ wide shapeable line within \\rngmed range.
                \\hit Each target takes fire \\glossterm<standard damage>.
            """, tags=['Fire']),
            Spell('Flame Aura', 4, """
                Choose a willing creature within \\rngclose range.
                Heat constantly radiates in a \\areamed radius emanation from the target.
                At the end of each \\glossterm<action phase>, make an attack vs. Armor against everything in the area.
                \\hit Each target takes fire \\glossterm<standard damage> -2d.

                You can cast this spell as a \\glossterm<minor action>.
                In addition, you can apply the Widened \\glossterm<augment> to this spell.
                If you do, it increases the area of the emanation.
            """, tags=['Attune (target)', 'Fire']),
            Spell('Flame Blade', 2, """
                Choose a willing creature within \\rngclose range.
                % Is this clear enough at not stacking with magic bonuses intrinsic to the creature?
                Weapons wielded by the target gain a +1d \\glossterm<magic bonus> to damage with \\glossterm<strikes>.
                In addition, all damage dealt with strikes using its weapons becomes fire damage in addition to the attack's normal damage types.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)', 'Fire']),
            Spell('Wall of Fire', 2, """
                You create a wall of fire in a 10 ft.\\ high, \\arealarge line within \\rngmed range.
                The flames and heat make it diffcult to see through the wall, granting \\glossterm<concealment> to targets on the opposite side of the wall.
                When a creature passes through the wall, you make an attack vs. Armor against that creature.
                You can only make an attack in this way against a given creature once per \\glossterm<phase>.
                \\hit The target takes fire \\glossterm<standard damage>.

                Each five-foot square of wall has hit points equal to twice your \\glossterm<power>, and all of its defenses are 0.
                It is immune to most forms of attack, but it can be destroyed by \\glossterm<cold damage> and similar effects that can destroy water.
            """, tags=['Attune (self)', 'Fire']),
        ],
        category='damage',
    ))

    # Primary: buff
    # Secondary: utility
    # None: damage, debuff
    mystic_spheres.append(MysticSphere(
        name="Revelation",
        short_description="Share visions of the present and future, granting insight or combat prowess",
        cantrips=[
            Effects('Precognitive Strike', """
                You can only cast this spell during the \\glossterm<action phase>.
                Choose a willing creature within \\rngclose range.
                On the next \\glossterm<strike> the target makes, it rolls twice and takes the higher result.
                If you cast this spell on another creature, the effect ends at the end of the current round if the target has not made a strike by that time.
                If you cast this spell on yourself, it lasts until the end of the next round.
            """, ap_cost=False),
        ],
        schools=['Divination'],
        lists=['Arcane', 'Divine', 'Nature'],
        spells=[
            Spell('True Strike', 1, """
                Choose a willing creature within \\rngclose range.
                On the next \\glossterm<strike> the target makes, it gains a +4 bonus to \\glossterm<accuracy> and rolls twice and takes the higher result.
                This effect ends at the end of the next round if the target has not made a strike by that time.
            """, tags=[]),
            Spell('Greater True Strike', 3, """
                This spell functions like the \\textit<true strike> spell, except that the bonus is increased to +6.
            """, tags=[]),
            Spell('Supreme True Strike', 5, """
                This spell functions like the \\textit<true strike> spell, except that the bonus is increased to +8.
            """, tags=[]),
            Spell('Precognitive Offense', 2, """
                Choose a willing creature within \\rngclose range.
                The target gains a +1 \\glossterm<magic bonus> to \\glossterm<accuracy> with all attacks.

                You can cast this spell as a \\glossterm<minor action>.
            """, tags=['Attune (target)']),
            Spell('Greater Precognitive Offense', 5, """
                This spell functions like the \\spell<precognitive offense> spell, except that the bonus is increased to +2.
            """, tags=['Attune (target)']),
            Spell('Precognitive Defense', 1, """
                Choose a willing creature within \\rngclose range.
                The target gains a +1 \\glossterm<magic bonus> to Armor defense and Reflex defense.
            """, tags=['Attune (target)']),
            Spell('Greater Precognitive Defense', 4, """
                This spell functions like the \\spell<precognitive defense> spell, except that the bonus is increased to +2.
            """, tags=['Attune (target)']),
            Spell('Supreme Precognitive Defense', 7, """
                This spell functions like the \\spell<precognitive defense> spell, except that bonus is increased to +3.
            """, tags=['Attune (target)']),
            Spell('Discern Lies', 2, """
                Make an attack vs. Mental against a creature within \\rngmed range.
                \\hit You know when the target deliberately and knowingly speaks a lie.
                This ability does not reveal the truth, uncover unintentional inaccuracies, or necessarily reveal evasions.
            """, tags=['Attune (self)', 'Detection']),
            Spell('Boon of Mastery', 1, """
                Choose a willing creature within \\rngclose range.
                The target gains a +2 \\glossterm<magic bonus> to all skills.
            """, tags=['Attune (target)']),
            Spell('Greater Boon of Mastery', 4, """
                This spell functions like the \\spell<boon of mastery> spell, except that the bonus is increased to +4.
            """, tags=['Attune (target)']),
            Spell('Boon of Many Eyes', 2, """
                Choose a willing creature within \\rngclose range.
                The target gains a +1 \\glossterm<magic bonus> to \\glossterm<overwhelm resistance>.
            """, tags=['Attune (target)']),
            Spell('Boon of Knowledge', 2, """
                Choose a willing creature within \\rngclose range.
                The target gains a +4 \\glossterm<magic bonus> to all Knowledge skills (see \\pcref<Knowledge>).
            """, tags=['Attune (target)']),
            Spell('Third Eye', 3, """
                Choose a willing creature within \\rngclose range.
                The target gains \\glossterm<blindsight> with a 50 foot range.
                This can allow it to see perfectly without any light, regardless of concealment or invisibility.
            """, tags=['Attune (target)']),
        ],
        rituals=[
            Spell('Read Magic', 1, """
                You gain the ability to decipher magical inscriptions that would otherwise be unintelligible.
                This can allow you to read ritual books and similar objects created by other creatures.
                After you have read an inscription in this way, you are able to read that particular writing without the use of this ritual.

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual)']),
            Spell('Discern Location', 4, """
                Choose a creature or object on the same plane as you.
                You do not need \\glossterm<line of sight> or \\glossterm<line of effect> to the target.
                However, you must specify your target with a precise mental image of its appearance.
                The image does not have to be perfect, but it must unambiguously identify the target.
                You learn the location (place, name, business name, or the like), community, country, and continent where the target lies.
                % Wording?
                If there is no corresponding information about an aspect of the target's location, such as if the target is in a location which is not part of a recognized country,
                    you learn only that that that aspect of the information is missing.

                This ritual takes 24 hours to perform, and it requires 32 action points from its participants.
            """, tags=[]),
            Spell('Interplanar Discern Location', 6, """
                This ritual functions like the \\ritual<discern location> ritual, except that the target does not have to be on the same plane as you.
                It gains the \\glossterm<Planar> tag in addition to the tags from the \\ritual<discern location> ritual.

                This ritual takes 24 hours to perform, and it requires 72 action points from its participants.
            """, tags=[]),
            Spell('Sending', 3, """
                Choose a creature on the same plane as you.
                You do not need \\glossterm<line of sight> or \\glossterm<line of effect> to the target.
                However,  must specify your target with a precise mental image of its appearance.
                The image does not have to be perfect, but it must unambiguously identify the target.
                If you specify its appearance incorrectly, or if the target has changed its appearance, you may accidentally target a different creature, or the ritual may simply fail.

                You send the target a short verbal message.
                The message must be twenty-five words or less, and speaking the message must not take longer than five rounds.

                After the the target receives the message, it may reply with a message of the same length as long as the ritual's effect continues.
                Once it speaks twenty-five words, or you stop sustaining the effect, the ritual is \\glossterm<dismissed>.

                This ritual takes one hour to perform.
            """, tags=['Sustain (standard)']),
            Spell('Interplanar Sending', 6, """
                This ritual functions like the \\ritual<sending> ritual, except that the target does not have to be on the same plane as you.
                It gains the \\glossterm<Planar> tag in addition to the tags from the \\ritual<sending> ritual.
            """, tags=['Sustain (standard)']),
            Spell('Telepathic Bond', 3, """
                Choose up to five willing ritual participants.
                Each target can communicate mentally through telepathy with each other target.
                This communication is instantaneous, though it cannot reach more than 100 miles or across planes.

                % Is this grammatically correct?
                Each target must attune to this ritual independently.
                If a target breaks its attunement, it stops being able to send and receive mental messages with other targets.
                However, the effect continues as long as at least one target attunes to it.
                If you \\glossterm<dismiss> the ritual, the effect ends for all targets.

                This ritual takes one minute to perform.
            """, tags=['Attune (ritual; see text)']),
            Spell('Long-Distance Bond', 5, """
                This ritual functions like the \\ritual<telepathic bond> ritual, except that the effect works at any distance.
                The communication still does not function across planes.
            """, tags=['Attune (ritual; see text)']),
            Spell('Planar Bond', 7, """
                This ritual functions like the \\ritual<telepathic bond> ritual, except that the effect works at any distance and across planes.
                It gains the \\glossterm<Planar> tag in addition to the tags from the \\ritual<telepathic bond> ritual.
            """, tags=['Attune (ritual; see text)']),
            Spell('Seek Legacy', 2, """
                Choose a willing ritual participant.
                The target learns the precise distance and direction to their \\glossterm<legacy item>, if it is on the same plane.

                This ritual takes 24 hours to perform, and requires 8 action points from its ritual participants.
            """, tags=[]),
        ],
        category='buff, offense',
    ))

    # This spell is problematic
    # Primary: utility
    # None: buff, damage, debuff
    mystic_spheres.append(MysticSphere(
        name="Scry",
        short_description="See and hear at great distances",
        # TODO: this shouldn't reference the spell effect.
        cantrips=[Effects('Remote Sensing', """
            This cantrip functions like the \\textit<arcane eye> spell, except that it gains the \\glossterm<Sustain> (minor) tag in place of the \\glossterm<Attune> (self) tag.",
            In addition, the sensor cannot be moved after it is originally created.
        """, tags=['Scrying', 'Sustain (minor)'], ap_cost=False)],
        schools=['Divination'],
        lists=['Arcane', 'Divine', 'Nature'],
        spells=[
            Spell('Alarm', 1, """
                A \\glossterm<scrying sensor> appears floating in the air in an unoccupied square within \\rngmed range.
                The sensor passively observes its surroundings.
                If it sees a creature or object of Tiny size or larger moving within 50 feet of it, it will trigger a mental "ping" that only you can notice.
                You must be within 1 mile of the sensor to receive this mental alarm.
                This mental sensation is strong enough to wake you from normal sleep, but does not otherwise disturb concentration.
            """, tags=['Attune (self)', 'Scrying']),
            Spell('Arcane Eye', 1, """
                A \\glossterm<scrying sensor> appears floating in the air in an unoccupied square within \\rngmed range.
                At the start of each round, you choose whether you see from this sensor or from your body.

                While viewing through the sensor, your visual acuity is the same as your normal body, except that it does not share the benefits of any \\glossterm<magical> effects that improve your vision.
                You otherwise act normally, though you may have difficulty moving or taking actions if the sensor cannot see your body or your intended targets, effectively making you \\blinded.

                If undisturbed, the sensor floats in the air in its position.
                As a \\glossterm<minor action>, you can concentrate to move the sensor up to 30 feet in any direction, even vertically.
                At the end of each round, if the sensor is does not have \\glossterm<line of effect> from you, it is destroyed.
            """, tags=['Attune (self)', 'Scrying']),
            Spell('Greater Alarm', 2, """
                This spell functions like the \\textit<alarm> spell, except that the sensor gains 100 ft.\\ \\glossterm<darkvision> and its Awareness bonus is equal to your \\glossterm<power>.
            """, tags=['Attune (self)', 'Scrying']),
            Spell('Auditory Eye', 2, """
                This spell functions like the \\spell<arcane eye> spell, except that you can you can also hear through the sensor.
                At the start of each round, you can choose whether you hear from the sensor or from your body.
                This choice is made independently from your sight.
                The sensor's auditory acuity is the same as your own, except that it does not share the benefits of any \\glossterm<magical> effects that improve your hearing.
            """, tags=['Attune (self)', 'Scrying']),
            Spell('Accelerated Eye', 2, """
                This spell functions like the \\spell<arcane eye> spell, except that the sensor moves up to 100 feet when moved instead of up to 30 feet.
            """, tags=['Attune (self)', 'Scrying']),
            Spell('Autonomous Eye', 3, """
                This spell functions like the \\spell<arcane eye> spell, except that the sensor is not destroyed when it loses \\glossterm<line of effect> to you.
            """, tags=['Attune (self)', 'Scrying']),
            Spell('Penetrating Eye', 4, """
                This spell functions like the \\spell<autonomous eye> spell, except that you do not need \\glossterm<line of sight> or \\glossterm<line of effect> to target a location.
                You must specify a distance and direction to target a location you cannot see.
                This can allow you to cast the spell beyond walls and similar obstacles.
                As normal, if the intended location is occupied or otherwise impossible, the spell is \\glossterm<miscast>.
            """, tags=['Attune (self)', 'Scrying']),
            Spell('Twin Eye', 3, """
                This spell functions like the \\spell<arcane eye> spell, except that you constantly receive sensory input from both your body and the sensor.
                This allows you to see simultaneously from your body and from the sensor.
            """, tags=['Attune (self)', 'Scrying']),
            Spell('Reverse Scrying', 2, """
                Choose a magical sensor within \\rngmed range.
                A new scrying sensor appears at the location of the source of the the ability that created the target sensor.
                This sensor functions like the sensor created by the \\spell<autonomous eye> spell, except that the sensor cannot move.
            """, tags=['Attune (self)', 'Scrying']),
            # spell to cast spells from the eye instead of from your body?
        ],
        rituals=[
            Spell('Scry Creature', 4, """
                Make an attack vs. Mental against a creature on the same plane as you.
                You do not need \\glossterm<line of sight> or \\glossterm<line of effect> to the target.
                However,  must specify your target with a precise mental image of its appearance.
                The image does not have to be perfect, but it must unambiguously identify the target.
                If you specify its appearance incorrectly, or if the target has changed its appearance, you may accidentally target a different creature, or the spell may simply be \\glossterm<miscast>.
                This attack roll cannot \\glossterm<explode>.
                \\hit A scrying sensor appears in the target's space.
                This sensor functions like the sensor created by the \\spell<arcane eye> spell, except that you cannot move the sensor manually.
                Instead, it automatically tries to follow the target to stay in its space.
                At the end of each phase, if the sensor is not in the target's space, this effect is \\glossterm<dismissed>.

                This ritual takes one hour to perform.
            """, tags=['Scrying']),
            Spell('Interplanar Scry Creature', 7, """
                This ritual functions like the \\ritual<scry creature> ritual, except that the target does not have to be on the same plane as you.
                It gains the \\glossterm<Planar> tag in addition to the tags from the \\ritual<scry creature> ritual.
            """, tags=['Scrying']),
        ],
        category='narrative',
    ))

    # Should this allow you to summon two monsters at once? I think that is
    # okay maybe?

    # This seems weird?
    # Secondary: buff, damage, debuff, utility
    mystic_spheres.append(MysticSphere(
        name="Summon",
        short_description="Summon creatures to fight with you",
        # TODO: this shouldn't reference the spell effect
        cantrips=[
            Effects('Sustained Summoning', """
                This cantrip functions like the \\spell<summon monster> spell, except that it has the \\glossterm<Sustain> (standard) tag instead of the \\glossterm<Attune> (self) tag.
            """, tags=["Manifestation", 'Sustain (standard)'], ap_cost=False),
        ],
        schools=['Conjuration'],
        lists=['Arcane', 'Divine', 'Nature'],
        spells=[
            # TODO: this needs more spell
            Spell('Summon Monster', 1, """
                You summon a creature in an unoccupied square on stable ground within \\rngmed range.
                It visually appears to be a common Small or Medium animal of your choice, though in reality it is a manifestation of magical energy.
                Regardless of the appearance and size chosen, the creature's statistics are unchanged.
                It has hit points equal to twice your \\glossterm<power>.
                % Has to be level instead of power because power can't scale directly with d10s ever
                All of its defenses are equal to your 4 \\add your level, and its \\glossterm<land speed> is equal to 30 feet.
                It does not have any \\glossterm<action points>.

                Each round, you can choose the creature's actions by mentally commanding it.
                There are only two actions it can take.
                As a \\glossterm<move action>, it can move as you direct.
                As a standard action, it can make a melee \\glossterm{strike} against a creature it threatens.
                Its accuracy is equal to your \\glossterm<accuracy>.
                If it hits, it deals \\glossterm<standard damage> -1d.
                The type of damage dealt by this attack depends on the creature's appearance.
                Most animals bite or claw their foes, which deals bludgeoning and slashing damage.

                If you do not command the creature's actions, it will continue to obey its last instructions if possible or do nothing otherwise.
            """, tags=['Attune (self)', 'Manifestation']),
            Spell('Summon Bear', 2, """
                This spell functions like the \\spell<summon monster> spell, except that the creature appears to be a Medium bear.
                As a standard action, it can make a \\glossterm<grapple> attack against a creature it threatens.
                Its accuracy is the same as its accuracy with \\glossterm<strikes>.
                While grappling, the manifested creature can either make a strike or attempt to escape the grapple.
            """, tags=['Attune (self)', 'Manifestation']),
            Spell('Summon Mount', 2, """
                This spell functions like the \\spell<summon monster> spell, except that you must also choose a willing creature within \\rngmed range to ride the summoned creature.
                In addition, the summoned creature appears to be either a Large horse or a Medium pony.
                It comes with a bit and bridle and a riding saddle, and will only accept the target as a rider.
                It has the same statistics as a creature from the \\spell<summon monster> spell, except that it follows its rider's directions to the extent that a well-trained horse would and it cannot attack.
            """, tags=['Attune (target)', 'Manifestation']),
            Spell('Summon Bird', 3, """
                This spell functions like the \\spell<summon monster> spell, except that the creature appears to be a bird.
                It has a 30 foot \\glossterm<fly speed>.
            """, tags=['Attune (self)', 'Manifestation']),
            Spell('Summon Wolfpack', 4, """
                This spell functions like the \\spell<summon monster> spell, except that it summons a pack of four wolf-shaped creatures instead of a single creature.
                Each creature has a -2 penalty to \\glossterm<accuracy> and \\glossterm<defenses> compared to a normal summoned creature.
                % TODO: wording?
                You must command the creatures as a group, rather than as individuals.
                Each creature obeys your command to the extent it can.
            """, tags=['Attune (self)', 'Manifestation']),
            Spell('Summon Flying Mount', 4, """
                This spell functions like the \\spell<summon mount> spell, except that the summoned creature appears to be either a Large or Medium pegasus.
                It has a 30 foot \\glossterm<fly speed>.
            """, tags=['Attune (target)', 'Manifestation']),
        ],
        rituals=[
            # weird to have a spell and a ritual but both are useful
            Spell('Ritual Mount', 2, """
                Choose a willing creature within \\rngclose range.
                This ritual summons your choice of a Large light horse or a Medium pony to serve as a mount.
                The creature appears in an unoccupied location within \\rngclose range.
                It comes with a bit and bridle and a riding saddle, and will only accept the target as a rider.
                It has the same statistics as a creature from the \\spell<summon monster> spell, except that it follows its rider's directions to the extent that a well-trained horse would and it cannot attack.
            """, tags=['Attune (ritual)', 'Manifestation']),
        ],
        # What category does this belong to?
        category='buff, offense',
    ))

    # Primary: damage
    # Secondary: utility
    # Tertiary: debuff
    # None: buff
    mystic_spheres.append(MysticSphere(
        name="Telekinesis",
        short_description="Manipulate creatures and objects at a distance",
        cantrips=[
            Effects('Distant Hand', """
                Choose a Medium or smaller unattended object within \\rngclose range.
                You can move it up to five feet in any direction within range, using your \\glossterm<power> instead of your Strength to determine your maximum carrying capacity.

                In addition, you can manipulate the target as if you were holding it in your hands.
                Any attacks you make with the object or checks you make to manipulate the object have a maximum bonus equal to your \\glossterm<power>.
            """, tags=['Sustain (standard)'], ap_cost=False),
            Effects('Telekinetic Compression', """
                Make an attack vs. Mental against one creature or object within \\rngmed range.
                \\hit The target takes bludgeoning \\glossterm<standard damage>.
            """, tags=[], ap_cost=False),
        ],
        schools=['Evocation'],
        lists=['Arcane', 'Pact'],
        spells=[
            Spell('Telekinetic Crush', 1, """
                Make an attack vs. Mental against one creature or object within \\rngmed range.
                \\hit The target takes bludgeoning \\glossterm<standard damage> +2d.
            """, tags=[]),
            Spell('Telekinetic Throw', 1, """
                Make an attack vs. Mental against a Medium or smaller creature or object within \\rngmed range.
                \\hit You move the target up to 30 feet in any direction.
                    You can change direction partway through the movement.
                    Moving the target upwards costs twice the normal movement cost.

                % Wording?
                If the target is willing, you can move it up to 100 feet.
            """, tags=[]),
            Spell('Greater Telekinetic Throw', 3, """
                This spell functions like the \\textit<telekinetic throw> spell, except that you can move the target up to 100 feet.
                If the target is willing, you can move it up to 200 feet.
            """, tags=[]),
            Spell('Telekinetic Lift', 1, """
                Choose a Medium or smaller willing creature or unattended object within \\rngclose range.
                The target is reduced to half of its normal weight.
                This gives it a +4 bonus to the Jump skill, if applicable, and makes it easier to lift and move.
            """, tags=['Attune (target)']),
            Spell('Greater Telekinetic Lift', 3, """
                This spell functions like the \\spell<telekinetic lift> spell, except that the target is reduced to one quarter of its normal weight.
                This increases the Jump bonus to +8.
            """, tags=['Attune (target)']),
            Spell('Binding Crush', 2, """
                This spell functions like the \\spell<telekinetic crush> spell, except that the struck creature is also \\glossterm<slowed> as a \\glossterm<condition> if it is Large or smaller.
            """, tags=[]),
            Spell('Greater Binding Crush', 5, """
                This spell functions like the \\spell<telekinetic crush> spell, except that the struck creature is also \\glossterm<decelerated> as a \\glossterm<condition> if it is Large or smaller.
            """, tags=[]),
            Spell('Levitate', 4, """
                Choose a Medium or smaller willing creature or unattended object within \\rngclose range.
                % TODO: Wording
                As long as the target remains within 50 feet above a surface that could support its weight, it floats in midair, unaffected by gravity.
                During the movement phase, you can move the target up to ten feet in any direction as a \\glossterm<free action>.
            """, tags=['Attune (self)']),
            Spell('Wall of Force', 3, """
                You create a wall of telekinetic force in a 10 ft.\\ high, \\arealarge line within \\rngmed range.
                The wall is transparent, but blocks physical passage and \\glossterm<line of effect>.
                Each five-foot square of wall has hit points equal to twice your \\glossterm<power>, and all of its defenses are 0.
            """, tags=['Attune (self)']),
            Spell('Forcecage', 7, """
                You create a 10 ft.\\ cube of telekinetic force within \\rngmed range.
                You can create the cube around a sufficiently small creature to trap it inside.
                Each wall is transparent, but blocks physical passage and \\glossterm<line of effect>.
                Each five-foot square of wall has hit points equal to twice your \\glossterm<power>, and all of its defenses are 0.
            """, tags=['Attune (self)']),
        ],
        category='debuff, combat',
    ))

    # Primary: damage
    # Secondary: utility
    # Tertiary: debuff
    # None: buff
    mystic_spheres.append(MysticSphere(
        name="Terramancy",
        short_description="Manipulate earth to crush foes",
        cantrips=[Effects('Minor Earthspike', """
            You create a spike of earth from the ground that quickly retracts, leaving the surface unchanged.
            Make an attack vs. Armor against a creature or object within \\rngmed range.
            The target must be within 5 feet of a Small or larger body of earth or stone.
            \\hit The target takes piercing \\glossterm<standard damage>.
        """, tags=['Earth', 'Physical'], ap_cost=False)],
        schools=['Conjuration', 'Transmutation'],
        lists=['Arcane', 'Nature'],
        spells=[
            Spell('Rock Throw', 1, """
                % TODO: define maximum hardness?
                You extract a Tiny chunk from a body of earth or unworked stone within 5 feet of you and throw it at a foe.
                If no such chunk can be extracted, this spell is \\glossterm<miscast>.
                Otherwise, make an attack vs. Armor against a creature or object within \\rngmed range.
                \\hit The target takes bludgeoning \\glossterm<standard damage> +2d.
            """, tags=['Earth', 'Physical']),
            Spell('Shrapnel Blast', 2, """
                You extract a Tiny chunk from a body of earth or unworked stone within 5 feet of you and blast it at your foes.
                If no such chunk can be extracted, this spell is \\glossterm<miscast>.
                Otherwise, make an attack vs. Armor against everything in a \\arealarge cone from you.
                \\hit Each target takes bludgeoning and piercing \\glossterm<standard damage>.
            """, tags=['Earth', 'Physical']),
            Spell('Earthcraft', 1, """
                You create a weapon or suit of armor from a body of earth or unworked stone within 5 feet of you.
                You can create any weapon, shield, or body armor that you are proficient with, and which would normally be made entirely from metal, except for heavy body armor.
                The body targeted must be at least as large as the item you create.

                The item functions like a normal item of its type, except that it is twice as heavy.
                If the item loses all of its hit points, this effect is \\glossterm<dismissed>.
            """, tags=['Attune (self)', 'Earth']),
            Spell('Reinforced Earthcraft', 2, """
                This spell functions like the \\spell<earthcraft> spell, except that the item is the same weight as a normal item of its type.
                In addition, you can create heavy body armor.
            """, tags=['Attune (self)', 'Earth']),
            Spell('Earthspike', 1, """
                You create a spike of earth from the ground.
                Make an attack vs. Armor against a creature or object within \\rngmed range.
                The target must be within 5 feet of a Small or larger body of earth or stone.
                \\hit The target takes piercing \\glossterm<standard damage> +1d and is \\glossterm<slowed> as a \\glossterm<condition>.
            """, tags=['Earth', 'Physical']),
            Spell('Impaling Earthspike', 4, """
                This spell functions like the \\spell<earthspike> spell, except that a struck target is \\glossterm<decelerated> instead of \\glossterm<slowed>.
            """, tags=['Earth', 'Physical']),
            Spell('Meld into Stone', 2, """
                Choose a stone object you can touch that is at least as large as your body.
                You and up to 100 pounds of nonliving equipment meld into the stone.
                If you try to bring excess equipment into the stone, the spell is \\glossterm<miscast>.

                As long as the spell lasts, you can move within the stone as if it was thick water.
                However, at least part of you must remain within one foot of the place you originally melded with the stone.
                You gain no special ability to breathe or see while embedded the stone, and you cannot speak if your mouth is within the stone.
                The stone muffles sound, but very loud noises may reach your ears within it.
                If you fully exit the stone, this spell ends.

                If this spell ends before you exit the stone, or if the stone stops being a valid target for the spell (such as if it is broken into pieces), you are forcibly expelled from the stone.
                When you are forcibly expelled from the stone, you take 4d10 bludgeoning damage and become \\glossterm<nauseated> as a \\glossterm<condition>.
            """, tags=['Attune (self)', 'Earth']),
            Spell('Tremor', 2, """
                You create an highly localized tremor that rips through the ground.
                Make an attack vs. Reflex against all Large or smaller creatures other than yourself standing on the ground in a \\areamed radius within \\rngmed range.
                \\hit Each target is knocked \\glossterm<prone>.
            """, tags=['Earth', 'Physical']),
            Spell('Earthquake', 5, """
                You create an intense but highly localized tremor that rips through the ground.
                Make an attack vs. Reflex against all creatures other than yourself standing on the ground in a \\arealarge radius within \\rnglong range.
                \\hit Each target takes bludgeoning \\glossterm<standard damage>.
                If a target is Huge or smaller, it is also knocked \\glossterm<prone>.
            """, tags=['Earth', 'Physical']),
            Spell('Fissure', 3, """
                You open up a rift in the ground that swallows and traps a foe.
                Make an attack vs. Reflex against a Large or smaller creature standing on earth or unworked stone within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\glossterm<immobilized>.
                As long as the target is immobilized in this way,
                    it takes bludgeoning \\glossterm<standard damage> -1d at the end of each \\glossterm<action phase> in subsequent rounds.
                This immobilization can be removed by climbing out of the fissure, which requires a \\glossterm<DR> 10 Climb check as a \\glossterm<move action>.
                Alternately, an ally that can reach the target can make a Strength check against the same DR to pull the target out.
                Special movement abilities such as teleportation can also remove the target from the fissure.
            """, tags=['Earth', 'Physical']),
            Spell('Fissure Swarm', 6, """
                This spell functions like the \\spell<fissure> spell, except that it affects all enemies in a \\areamed radius within \\rngmed range.
            """, tags=['Earth', 'Physical']),
            Spell('Earthbind', 2, """
                Make an attack vs. Fortitude against a creature within \\rngmed range that is within 50 feet of the ground.
                \\hit As a \\glossterm<condition>, the target is pulled towards the ground with great force, approximately quadrupling the gravity it experiences.
                This imposes a -4 penalty to \\glossterm<accuracy>, physical \\glossterm<checks>, and \\glossterm<defenses>.
                In addition, most flying creatures are unable to fly with this increased gravity and crash to the ground.
            """, tags=['Earth']),
            Spell('Quagmire', 2, """
                % TODO: define maximum hardness
                Choose a \\areamed radius within \\rngmed range.
                All earth and unworked stone within the area is softened into a thick sludge, creating a quagmire that is difficult to move through.
                The movement cost required to move out of each affected square within the area is quadrupled.
                This does not affect objects under significant structural stress, such as walls and support columns.
            """, tags=['Attune (self)', 'Earth', 'Physical']),
            Spell('Earthen Fortification', 2, """
                You construct a fortification made of packed earth within \\rngmed range.
                This takes the form of up to ten contiguous 5-foot squares, each of which is four inches thick.
                The squares can be placed at any angle and used to form any structure as long as that structure is stable.
                Since the fortifications are made of packed earth, their maximum weight is limited, and structures taller than ten feet high are usually impossible.
                % TODO: define hit points and hardness of earth

                The fortifications form slowly, rather than instantly.
                The structure becomes complete at the end of the action phase in the next round after this spell is cast.
                This makes it difficult to trap creatures within structures formed.
            """, tags=['Attune (self)', 'Earth', 'Manifestation']),
            Spell('Stone Fortification', 3, """
                This spell functions like the \\spell<earthen fortification> spell, except that the fortifications are made of stone instead of earth.
                This makes them more resistant to attack and allows the construction of more complex structures.
                % TODO: define hit points and hardness of stone
            """, tags=['Attune (self)', 'Earth', 'Manifestation']),
        ],
        rituals=[
        ],
    ))

    # Primary: utility
    # Secondary: debuff
    # Tertiary: buff
    # None: damage
    mystic_spheres.append(MysticSphere(
        name='Thaumaturgy',
        short_description="Suppress and manipulate magical effects",
        cantrips=[
            Effects('Minor Suppression', """
                Make an attack against one creature within \\rngmed range.
                The attack result is applied to every \\glossterm<magical> effect on the target.
                The DR for each effect is equal to the \\glossterm<power> of that effect.
                \\hit Each effect is \\glossterm<suppressed>.
            """, tags=['Mystic', 'Sustain (standard)'], ap_cost=False),
        ],
        schools=['Abjuration'],
        lists=['Arcane', 'Divine'],
        spells=[
            Spell('Suppress Magic', 1, """
                Make an attack against one creature, object, or magical effect within \\rngmed range.
                If you target a creature or object, the attack result is applied to every \\glossterm<magical> effect on the target.
                % Is this clear enough?
                This does not affect the passive effects of any magic items the target has equipped.
                If you target a magical effect directly, the attack result is applied against the effect itself.
                The DR for each effect is equal to the \\glossterm<power> of that effect.
                \\hit Each effect is \\glossterm<suppressed>.
            """, tags=['Mystic', 'Sustain (standard)']),
            Spell('Alter Magic Aura', 1, """
                Make an attack vs. Mental against one Large or smaller magical object in \\rngmed range.
                \\hit One of the target's magic auras is altered (see \pcref{Spellcraft}).
                You can change the school and descriptors of the aura.
                In addition, you can decrease the \\glossterm<power> of the aura by up to half your power, or increase the power of the aura up to a maximum of your power.
            """, tags=['Attune (self)', 'Mystic']),
            Spell('Suppress Item', 1, """
                Make an attack vs. Mental against one Large or smaller magical object in \\rngmed range.
                \\hit All magical properties the target has are \\glossterm<suppressed>.
            """, tags=['Mystic', 'Sustain (minor)']),
            Spell('Dismissal', 2, """
                Make an attack against one creature or object within \\rngmed range.
                If the target is an effect of an ongoing \\glossterm<magical> ability, such as a summoned monster or created object, the DR is equal to the \\glossterm<power> of the ability.
                Otherwise, this spell has no effect.
                \\hit The target is treated as if the ability that created it was \\glossterm<dismissed>.
                This usually causes the target to disappear.
            """, tags=['Mystic']),
            Spell('Dispel Magic', 2, """
                This spell functions like the \\spell<suppress magic> spell, except that a hit against an effect causes it to be \\glossterm<dismissed> instead of suppressed.
            """, tags=['Mystic', 'Sustain (standard)']),
            Spell('Malign Transferance', 2, """
                Choose a willing ally within \\rngmed range.
                The ally must be currently affected by a \\glossterm<magical> \\glossterm<condition>.
                In addition, make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit One magical condition of your choice is removed from the chosen ally and applied to the struck creature.
                \\crit As above, except that you can transfer any number of magical conditions in this way.
            """, tags=[]),
            Spell('Greater Malign Transferance', 5, """
                Choose any number of willing allies within \\rngmed range.
                Each ally must be currently affected by a \\glossterm<magical> \\glossterm<condition>.
                In addition, make an attack vs. Mental against a creature within \\rngmed range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit Up to two magical conditions of your choice are removed from the chosen allies and applied to the struck creature.
                \\crit As above, except that you can transfer any number of magical conditions in this way.
            """, tags=[]),
            Spell('Enhance Magic', 1, """
                Choose a willing creature within \\rngmed range.
                The target gains a +1 \\glossterm<magic bonus> to \\glossterm<power> with spells.
            """, tags=['Attune (target)', 'Mystic']),
            Spell('Greater Enhance Magic', 4, """
                This spell functions like the \\textit<enhance magic> spell, except that the bonus is increased to +2.
            """, tags=['Attune (target)', 'Mystic']),
            # Is this worth the complexity it adds to the system?
            Spell('Antimagic Field', 7, """
                All other magical abilities and objects are \\glossterm<suppressed> within a \\areamed radius emanation from you.
                % How much of this is redundant with suppression?
                Creatures within the area cannot activate, sustain, or dismiss magical abilities.
                % TODO: wording
                This does not affect aspects of creatures that cannot be suppressed, such as the knowledge of abilities.
                You cannot exclude yourself from this emanation.
                However, this spell does not prevent you from sustaining or dismissing this spell.
            """, tags=['Mystic', 'Sustain (minor)']),
            # Does having this be Swift break anything?
            Spell('Dimensional Anchor', 2, """
                Make an attack vs. Mental against a creature or object within \\rngmed range.
                \\hit The target is unable to travel extradimensionally.
                This prevents all \\glossterm<Manifestation>, \\glossterm<Planar>, and \\glossterm<Teleportation> effects.
            """, tags=['Mystic', 'Swift', 'Sustain (minor)']),
            Spell('Dimensional Lock', 4, """
                This spell creates a dimensional lock in a \\arealarge radius zone from your location.
                Extraplanar travel into or out of the area is impossible.
                This prevents all \\glossterm<Manifestation>, \\glossterm<Planar>, and \\glossterm<Teleportation> effects.
            """, tags=['Attune (self)', 'Mystic']),
        ],
        category='debuff, combat',
    ))

    # Primary: debuff
    # Secondary: utility
    # Tertiary: damage
    # None: buff
    mystic_spheres.append(MysticSphere(
        name="Verdamancy",
        short_description="Animate and manipulate plants",
        cantrips=[Effects('Minor Embedded Growth', """
            You throw a seed that embeds itself in a foe and grows painfully.
            Make an attack vs. Armor at a creature within \\rngclose range.
            \\hit As a \\glossterm<condition>, the target takes \\glossterm<standard damage> -1d at the end of each \\glossterm<action phase>.
            This condition can be removed if the target or a creature that can reach the target makes a \\glossterm<DR> 5 Heal check as a standard action to remove the seed.
        """, ap_cost=False)],
        schools=['Transmutation'],
        lists=['Nature'],
        spells=[
            Spell('Entangle', 1, """
                You cause plants to grow and trap a foe.
                Make an attack vs. Reflex against a Large or smaller creature within \\rngmed range.
                The target must be within 5 feet of earth or plants.
                You gain a +2 bonus to \\glossterm<accuracy> with this attack if the target is in standing in \\glossterm<undergrowth>.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit The target is \\glossterm<immobilized> as a \\glossterm<condition>.
                This condition can be removed if the target or a creature that can reach the target makes a \\glossterm<DR> 5 Strength check as a standard action to pull the target free of the plants.
            """, tags=[]),
            Spell('Embedded Growth', 1, """
                You throw a seed that embeds itself in a foe and grows painfully.
                Make an attack vs. Armor at a creature within \\rngclose range.
                \\miss You regain the \\glossterm<action point> spent to cast this spell.
                \\hit As a \\glossterm<condition>, the target takes \\glossterm<standard damage> +1d at the end of each \\glossterm<action phase>.
                This condition can be removed if the target or a creature that can reach the target makes a \\glossterm<DR> 5 Heal check as a standard action to remove the seed.
            """, tags=[]),
            Spell('Fire Seed', 2, """
                % Does "seed structure" make sense?
                You transform an unattended acorn or similar seed structure into a small bomb.
                As a standard action, you or another creature can throw the acorn with a \\glossterm<range increment> of 20 feet.
                On impact, the acorn detonates, and you make an attack vs. Armor against all creatures within a \\areasmall radius of the struck creature or object.
                \\hit Each target takes fire \\glossterm<standard damage>.
            """, tags=['Attune (self)', 'Fire']),
            Spell('Greater Fire Seed', 4, """
                This spell functions like the \\spell<fire seed> spell, except that you can transform up to four bombs.
                In addition, the detonation affects a \\areamed radius instead of an \\areasmall radius.
            """, tags=['Attune (self)', 'Fire']),
            Spell('Wall of Thorns', 2, """
                You create a wall of thorns in a 10 ft.\\ high, \\areamed line within \\rngmed range.
                The base of at least half of the wall must be in arable earth.
                The wall is four inches thick, but permeable.
                It provides \\glossterm<passive cover> to attacks made through the wall.
                Creatures can pass through the wall, though it costs five extra feet of movement to move through the wall.
                When a creature moves through the wall, make an attack vs. Armor against it.
                You can only make an attack in this way against a given creature once per \\glossterm<phase>.
                \\hit The target takes piercing \\glossterm<standard damage> -1d.

                Each five-foot square of wall has hit points equal to three times your \\glossterm<power>, and all of its defenses are 0.
                It is \\glossterm<vulnerable> to fire damage.
            """, tags=['Attune (self)']),
            Spell('Greater Wall of Thorns', 4, """
                This spell functions like the \\spell<wall of thorns> spell, except that the wall is an \\arealarge shapeable line.
            """, tags=['Attune (self)']),
            Spell('Plant Growth', 2, """
                Choose a \\arealarge radius within \\rnglong range.
                In addition, choose whether you want plants within the area to grow or diminish.

                If you choose for plants to grow, all arable earth within the area becomes \\glossterm<light undergrowth>.
                Light undergrowth within the area is increased in density to \\glossterm<heavy undergrowth>.
                If you choose for plants to diminish, all \\glossterm<heavy undergrowth> in the area is reduced to \\glossterm<light undergrowth>, and all \\glossterm<light undergrowth> is removed.

                When this spell's duration ends, the plants return to their natural size.
            """, tags=['Attune (self)']),
            Spell('Greater Plant Growth', 4, """
                This spell functions like the \\spell<plant growth> spell, except that its effects are intensified.
                If you choose for plants to grow, all arable earth within the area becomes \\glossterm<heavy undergrowth>.
                If you choose for plants to diminish, all \\glossterm<undergrowth> within the area is removed.
            """, tags=['Attune (self)']),
            Spell('Blight', 2, """
                Make an attack vs. Fortitude against a living creature or plant within \\rngmed range.
                \\hit The target takes life \\glossterm<standard damage> +1d.
                This damage is doubled if the target is a plant, including plant creatures.
            """, tags=['Life']),
        ],
        rituals=[
            Spell('Fertility', 2, """
                This ritual creates an area of bountiful growth in a one mile radius zone from your location.
                Normal plants within the area become twice as productive as normal for the next year.
                This ritual does not stack with itself.
                If the \\ritual<infertility> ritual is also applied to the same area, the most recently performed ritual takes precedence.

                This ritual takes 24 hours to perform, and requires 8 action points from its participants.
            """, tags=[]),
            Spell('Infertility', 2, """
                This ritual creates an area of death and decay in a one mile radius zone from your location.
                Normal plants within the area become half as productive as normal for the next year.
                This ritual does not stack with itself.
                If the \\ritual<fertility> ritual is also applied to the same area, the most recently performed ritual takes precedence.

                This ritual takes 24 hours to perform, and requires 8 action points from its participants.
            """, tags=[]),
            Spell('Lifeweb Transit', 4, """
                Choose up to five willing, Medium or smaller ritual participants and a living plant that all ritual participants touch during the ritual.
                The plant must be at least one size category larger than the largest target.
                In addition, choose a destination up to 100 miles away from you on your current plane.
                By walking through the chosen plant, each target is teleported to the closest plant to the destination that is at least one size category larger than the largest target.

                You must specify the destination with a precise mental image of its appearance.
                The image does not have to be perfect, but it must unambiguously identify the destination.
                If you specify its appearance incorrectly, or if the area has changed its appearance, the destination may be a different area than you intended.
                The new destination will be one that more closely resembles your mental image.
                If no such area exists, the ritual simply fails.
                % TODO: does this need more clarity about what teleportation works?

                This ritual takes 24 hours to perform and requires 32 action points from its ritual participants.
                It is from from the Conjuration school in addition to the Transmutation school.
            """, tags=['Teleportation']),
        ],
    ))

    # Primary: damage
    # Secondary: buff (healing)
    # Tertiary: debuff, utility
    mystic_spheres.append(MysticSphere(
        name="Vital Surge",
        short_description="Alter life energy to cure or inflict wounds",
        cantrips=[
            Effects('Cure Minor Wounds', """
                Choose a willing creature within \\rngmed range.
                The target heals hit points equal to \\glossterm<standard damage>.
            """, tags=['Life'], ap_cost=False),
            Effects('Inflict Minor Wounds', """
                Make an attack vs. Fortitude against a creature within \\rngmed range.
                \\hit The target takes life damage equal to \\glossterm<standard damage>.
            """, tags=['Life'], ap_cost=False),
        ],
        schools=['Vivimancy'],
        lists=['Divine', 'Nature'],
        spells=[
            Spell('Cure Wounds', 1, """
                Choose a willing creature within \\rngmed range.
                The target heals hit points equal to \\glossterm<standard damage> +2d.
            """, tags=['Life']),
            Spell('Inflict Wounds', 1, """
                Make an attack vs. Fortitude against a creature within \\rngmed range.
                \\hit The target takes life damage equal to \\glossterm<standard damage> +2d.
            """, tags=['Life']),
            Spell('Greater Inflict Wounds', 3, """
                This spell functions like the \\spell<inflict wounds> spell, except that you gain a +1 bonus to \\glossterm<accuracy>.
                In addition, a struck target takes a -2 penalty to Fortitude defense as a \\glossterm<condition>.
            """, tags=['Life']),
            Spell('Supreme Inflict Wounds', 5, """
                This spell functions like the \\spell<inflict wounds> spell, except that you gain a +2 bonus to \\glossterm<accuracy>.
                In addition, a struck target takes a -4 penalty to Fortitude defense as a \\glossterm<condition>.
            """, tags=['Life']),
            Spell('Greater Cure Wounds', 3, """
                This spell functions like the \\spell<cure wounds> spell, except that you gain a +1d bonus to healing.
                In addition, for every 5 points of healing you provide, you can instead heal one point of \\glossterm<vital damage>.
            """, tags=['Life']),
            Spell('Heal', 5, """
                This spell functions like the \\spell<cure wounds> spell, except that you gain a +2d bonus to healing.
                In addition, it heals \\glossterm<vital damage> as easily as it heals hit points.
            """, tags=['Life']),
            # TODO: make "Undead Bane" spell after figuring out undead / life
            # damage interaction
            Spell('Drain Life', 3, """
                This spell functions like the \\spell<inflict wounds> spell, except that you gain a +1d bonus to damage.
                In addition, you heal hit points equal to your \\glossterm<power> if you deal damage.
            """, tags=['Life']),
            Spell('Greater Drain Life', 5, """
                This spell functions like the \\spell<inflict wounds> spell, except that gain a +2d bonus to damage.
                In addition, you heal hit points equal to twice your \\glossterm<power> if you deal damage.
            """, tags=['Life']),
            Spell('Vital Persistence', 2, """
                Choose a willing creature within \\rngclose range.
                The target reduces its \\glossterm<vital damage penalties> by an amount equal to your \\glossterm<power>.
            """, tags=['Attune (target)', 'Life']),
            Spell('Greater Vital Persistence', 4, """
                This spell functions like the \\spell<vital persistence> spell, except that the penalty reduction increases to be equal to twice your \\glossterm<power>.
            """, tags=['Attune (target)', 'Life']),
            Spell('Life Exchange', 4, """
                Choose a willing ally within \\rngmed range.
                Make an attack vs. Fortitude against a creature within \\rngmed range.
                \\hit The target takes life damage equal to \\glossterm<standard damage> +3d.
                In addition, the chosen ally heals hit points equal to the damage dealt in this way.
                \\crit This spell does not deal additional damage on a critical hit.
            """, tags=['Life']),
            Spell('Death Knell', 2, """
                This spell functions like the \\spell<inflict wounds> spell, except that a struck target suffers a death knell as a \\glossterm<condition>.
                At the end of each round, if the target has 0 hit points, it immediately dies.

                % TODO: wording
                If the target dies while the condition is active, you heal hit points equal to twice your \\glossterm<power>.
            """, tags=['Life']),
            Spell('Circle of Death', 3, """
                You are surrounded by an aura of death in a \\areamed radius emanation from you.
                When this spell resolves, and the end of each \\glossterm<action phase> in subsequent rounds, make an attack vs. Fortitude against all enemies in the area.
                \\hit Each target takes life \\glossterm<standard damage> -2d.
            """, tags=['Attune (self)', 'Life']),
            Spell('Circle of Healing', 3, """
                You are surrounded by an aura of healing in a \\areamed radius emanation from you.
                When this spell resolves, and the end of each \\glossterm<action phase> in subsequent rounds, all allies in the area heal hit points equal to half your \\glossterm<power>.
            """, tags=['Attune (self)', 'Life']),
            Spell('Finger of Death', 5, """
                Make an attack vs. Fortitude against a living creature within \\rngclose range.
                \\hit The target takes life \\glossterm<standard damage> +4d.
                \\crit The target immediately dies.
            """, tags=['Life']),
        ],
        rituals=[
            Spell('Remove Disease', 2, """
                Choose a willing creature within \\rngmed range.
                All diseases affecting the target are removed.
            """, tags=['Life']),
            Spell('Restore Senses', 2, """
                Choose a willing creature within \\rngmed range.
                One of the target's physical senses, such as sight or hearing, is restored to full capacity.
                This can heal both magical and mundane effects, but it cannot completely replace missing body parts required for a sense to function (such as missing eyes).
            """, tags=['Life']),
            Spell('Reincarnation', 4, """
                Choose one Diminuitive or larger piece of a humanoid corpse.
                The target must have been part of the original creature's body at the time of death.
                The creature the target corpse belongs to returns to life in a new body.
                It must not have died due to old age.

                This ritual creates an entirely new body for the creature's soul to inhabit from the natural elements at hand.
                During the ritual, the body ages to match the age of the original creature at the time it died.
                The creature has 0 hit points when it returns to life.

                A reincarnated creature is identical to the original creature in all respects, except for its species.
                The creature's species is replaced with a random species from \\tref<Humanoid Reincarnations>.
                Its appearance changes as necessary to match its new species, though it retains the general shape and distinguishing features of its original appearance.
                The creature loses all attribute modifiers and abilities from its old species, and gains those of its new species.
                If its species bonus feat is invalid for its new species, it must choose a new species bonus feat.
                However, its languages are unchanged.

                Coming back from the dead is an ordeal.
                All of the creature's action points and other daily abilities are expended when it returns to life.
                In addition, its maximum action points are reduced by 1.
                This penalty lasts for thirty days, or until the creature gains a level.
                If this would reduce a creature's maximum action points below 0, the creature cannot be resurrected.

                This ritual takes 24 hours to perform, and requires 32 action points from its participants.
                It is from the Conjuration school in addition to the Vivimancy school.
                In addition, it can only be learned through the nature \\glossterm<magic source>.
            """, tags=['Creation', 'Flesh', 'Life'], extra_text="""
                \\begin{dtable}
                    \\lcaption{Humanoid Reincarnations}
                    \\begin{dtabularx}{\\columnwidth}{l X}
                        d\\% & Incarnation \\\\
                        \\bottomrule
                        01--13 & Dwarf \\\\
                        14--26 & Elf \\\\
                        27--40 & Gnome \\\\
                        41--52 & Half-elf \\\\
                        53--62 & Half-orc \\\\
                        63--74 & Halfling \\\\
                        75--100 & Human \\\\
                    \\end{dtabularx}
                \\end{dtable}
            """),
            Spell('Fated Reincarnation', 5, f"""
                This ritual functions like the \\ritual<reincarnation> ritual, except that the target is reincarnated as its original species instead of as a random species.

                This ritual takes 24 hours to perform, and requires 50 action points from its participants.
                It is from the Conjuration school in addition to the Vivimancy school.
                In addition, it can only be learned through the nature \\glossterm<magic source>.
            """, tags=['Creation', 'Flesh', 'Life']),
            Spell('Purge Curse', 2, """
                Choose a willing creature within \\rngclose range.
                All curses affecting the target are removed.
                This ritual cannot remove a curse that is part of the effect of an item the target has equipped.
                However, it can allow the target to remove any cursed items it has equipped.

                This ritual takes 24 hours to perform, and requires 8 action points from its participants.
            """, tags=['Mystic']),
            Spell('Restoration', 3, """
                Choose a willing creature within \\rngclose range.
                All of the target's hit points, \\glossterm<subdual damage>, and \\glossterm<vital damage> are healed.
                In addition, any of the target's severed body parts or missing organs grow back by the end of the next round.

                This ritual takes 24 hours to perform, and requires 18 action points from its participants.
            """, tags=['Flesh']),
            Spell('Resurrection', 3, """
                Choose one intact humanoid corpse within \\rngclose range.
                The target returns to life.
                It must not have died due to old age.

                The creature has 0 hit points when it returns to life.
                It is cured of all \\glossterm<vital damage> and other negative effects, but the body's shape is unchanged.
                Any missing or irreparably damaged limbs or organs remain missing or damaged.
                The creature may therefore die shortly after being resurrected if its body is excessively damaged.

                Coming back from the dead is an ordeal.
                All of the creature's action points and other daily abilities are expended when it returns to life.
                In addition, its maximum action points are reduced by 1.
                This penalty lasts for thirty days, or until the creature gains a level.
                If this would reduce a creature's maximum action points below 0, the creature cannot be resurrected.

                This ritual takes 24 hours to perform, and requires 18 action points from its participants.
                It is from the Conjuration school in addition to the Vivimancy school.
                In addition, it can only be learned through the divine \\glossterm<magic source>.
            """, tags=['Flesh', 'Life']),
            Spell('Complete Resurrection', 5, """
                This ritual functions like the \\ritual<resurrection> ritual, except that it does not have to target a fully intact corpse.
                Instead, it targets a Diminuitive or larger piece of a humanoid corpse.
                The target must have been part of the original creature's body at the time of death.
                The resurrected creature's body is fully restored to its healthy state before dying, including regenerating all missing or damaged body parts.

                This ritual takes 24 hours to perform, and requires 50 action points from its participants.
                It is from the Conjuration school in addition to the Vivimancy school.
                In addition, it can only be learned through the divine \\glossterm<magic source>.
            """, tags=['Creation', 'Flesh', 'Life']),
            Spell('True Resurrection', 7, """
                This ritual functions like the \\ritual<resurrection> ritual, except that it does not require any piece of the corpse.
                Instead, you must explicitly and unambiguously specify the identity of the creature being resurrected.
                The resurrected creature's body is fully restored to its healthy state before dying, including regenerating all missing or damaged body parts.

                This ritual takes 24 hours to perform, and requires 98 action points from its participants.
                It is from the Conjuration school in addition to the Vivimancy school.
                In addition, it can only be learned through the divine \\glossterm<magic source>.
            """, tags=['Creation', 'Flesh', 'Life']),
            Spell('Soul Bind', 5, """
                Choose one intact corpse within \\rngclose range.
                % Is this clear enough that you can't use the same gem for this ritual twice?
                In addition, choose a nonmagical gem you hold that is worth at least 1,000 gp.
                A fragment of the soul of the creature that the target corpse belongs to is imprisoned in the chosen gem.
                This does not remove the creature from its intended afterlife.
                However, it prevents the creature from being resurrected, and prevents the corpse from being used to create undead creatures, as long as the gem is intact.
                A creature holding the gem may still resurrect or reanimate the creature.
                If the gem is shattered, the fragment of the creature's soul returns to its body.

                This ritual takes one hour to perform.
            """, tags=['Life']),
        ],
        category='damage',
    ))

    # Weaponcraft can create and manipulate weapons of all varieties; all of it
    # spells should involve a mixture of creating a weapon and manipulating
    # it after it is created.

    # Primary: damage
    # Secondary: utility
    # None: buff, debuff
    mystic_spheres.append(MysticSphere(
        name="Weaponcraft",
        short_description="Create and manipulate weapons to attack foes",
        cantrips=[
            Effects('Fire Projectile', """
                Make an attack vs. Armor against one creature or object within \\rngmed range.
                \\hit The target takes piercing \\glossterm<standard damage>.
            """, tags=['Manifestation'], ap_cost=False),
            Effects('Personal Weapon', """
                Choose a type of weapon that you are proficient with.
                You create a normal item of that type in your hand.
                If the item stops touching you, it disappears, and this effect ends.

                If you create a projectile weapon, you can fire it without ammunition by creating projectiles as you fire.
                The projectiles disappear after the attack is complete.

                % Strange duration for a cantrip
                This spell lasts until you use it again, or until you \\glossterm<dismiss> it as a \\glossterm<free action>.
            """, tags=['Manifestation'], ap_cost=False),
        ],
        schools=['Conjuration', 'Transmutation'],
        lists=['Arcane', 'Divine', 'Pact'],
        spells=[
            Spell('Mystic Bow', 1, """
                Make an attack vs. Armor against one creature or object within \\rngmed range.
                \\hit The target takes piercing \\glossterm<standard damage> +2d.
            """, tags=['Manifestation']),
            Spell('Blade Barrier', 1, """
                A wall of whirling blades appears within \\rngmed range.
                The wall takes the form of a 10 ft.\\ high, \\arealarge line.
                The wall provides \\glossterm<active cover> (20\\% miss chance) against attacks made through it.
                Attacks that miss in this way harmlessly strike the wall.
                When a creature or object passes through the wall, make an attack vs. Armor against it.
                \\hit The target takes slashing \\glossterm<standard damage>.
            """, tags=['Sustain (minor)']),
            Spell('Summon Weapon', 1, """
                A melee weapon that you are proficient with appears in an unoccupied square within \\rngmed range.
                The weapon floats about three feet off the ground, and is sized appropriately for a creature of your size.
                The specific weapon you choose affects the type of damage it deals.
                Regardless of the weapon chosen, it has hit points equal to twice your \\glossterm<power>.
                All of its defenses are equal to 3 \\add your level, and it has a 30 foot fly speed with good maneuverability, though it cannot travel farther than five feet above the ground.

                Each round, the weapon automatically moves towards the creature closest to it during the \\glossterm<movement phase>.
                During the \\glossterm<action phase>, it makes a melee \\glossterm<strike> against a random creature adjacent to it.
                Its accuracy is equal to your \\glossterm<accuracy>.
                If it hits, it deals \\glossterm<standard damage>.
            """, tags=['Manifestation', 'Sustain (minor)']),
            Spell('Blade Perimeter', 2, """
                This spell functions like the \\spell<blade barrier> spell, except that the wall is an 20 ft.\\ high, \\areamed radius circle.
            """, tags=['Sustain (minor)']),
            Spell('Contracting Blade Perimeter', 3, """
                This spell functions like the \\spell<blade perimeter> spell, except that the wall's radius shrinks by 5 feet at the end of every \\glossterm<action phase>, dealing damage to everything it moves through.
                % Clarify interaction with solid obstacles that block contraction?
            """, tags=['Sustain (minor)']),
            Spell('Aerial Weapon', 2, """
                This spell functions like the \\spell<summon weapon> spell, except that the weapon's height above the ground is not limited.
                This allows the weapon to fly up to fight airborne foes.
            """, tags=['Manifestation', 'Sustain (minor)']),
            Spell('Blade Barrier, Dual', 3, """
                This spell functions like the \\spell<blade barrier> spell, except that the area must be a line.
                In addition, the spell creates two parallel walls of the same length, five feet apart.
            """, tags=['Sustain (minor)']),
            Spell('Create Ballista', 2, """
                This spell functions like the \\spell<summon weapon> spell, except that it creates a fully functional Large ballista instead of a weapon of your choice.
                The ballista functions like any other weapon, with the following exceptions.

                It cannot move, and makes ranged \\glossterm<strikes> instead of melee strikes.
                Its attacks have a maximum range of 100 feet.
                Its attacks deal piercing damage, and its hit points are equal to three times your \\glossterm<power>.
                In addition, the ballista attacks the creature farthest from it, instead of the creature closest to it.
            """, tags=['Manifestation', 'Sustain (minor)']),
            Spell('Create Ballista, Dual Track', 4, """
                This spell functions like the \\spell<create ballista> spell, except that the ballista is created with two separate bolt tracks.
                This allows it to fire at two different targets in the same round when you command it to fire.
                It cannot fire at the same target twice.
                Each round, it attacks the two creatures farthest from it.
            """, tags=['Manifestation', 'Sustain (minor)']),
            Spell('Giant Blade', 3, """
                This spell functions like the \\spell<summon weapon> spell, except that the weapon takes the form of a Large greatsword.
                The weapon's attacks hit everything in a \\areasmall cone from it.
                It aims the cone to hit as many creatures as possible.
            """, tags=['Manifestation', 'Sustain (minor)']),
            Spell('Titan Blade', 6, """
                This spell functions like the \\spell<summon weapon> spell, except that the weapon takes the form of a Gargantuan greatsword.
                The weapon's attacks hit everything in a \\areamed cone from it.
                It aims the cone to hit as many creatures as possible.
            """, tags=['Manifestation', 'Sustain (minor)']),
            Spell('Paired Weapons', 7, """
                This spell functions like the \\spell<summon weapon> spell, except that you summon two weapons instead of one.
                Each weapon attacks independently.
            """, tags=['Manifestation', 'Sustain (minor)']),
        ],
        category='buff, offense',
    ))

    return sorted(mystic_spheres, key=lambda m: m.name)


def sanity_check(spells):
    # Make sure that the right kinds of spells exist

    # Every spell source should have one spell of each category
    for category in rise_data.categories:
        has_spell = {source: False for source in rise_data.spell_sources}
        for spell in spells:
            if spell.category == category:
                for source in spell.lists:
                    if source in has_spell:
                        has_spell[source] = True
        for source in rise_data.spell_sources:
            if not has_spell[source]:
                warn(f"Source {source} has no spell for {category}")

    # Every spell source should have both single target and multi damage spells
    # that target every defense
    for defense in rise_data.defenses:
        has_damage = {source: False for source in rise_data.spell_sources}
        # Every source should also have debuffs against every defense
        has_debuff = {source: False for source in rise_data.spell_sources}
        for spell in spells:
            if spell.effects.attack and spell.effects.attack.defense == defense:
                if spell.category == 'damage':
                    for source in spell.lists:
                        if source in rise_data.spell_sources:
                            has_damage[source] = True
                elif spell.category[:6] == 'debuff':
                    for source in spell.lists:
                        if source in rise_data.spell_sources:
                            has_debuff[source] = True

        for source in rise_data.spell_sources:
            if not has_damage[source]:
                warn(f"Source {source} has no damage spell against {defense}")
            if not has_debuff[source]:
                warn(f"Source {source} has no debuff spell against {defense}")

    # Every spell school should have at least two unique categories of
    # spells
    categories_in_school = {school: {} for school in rise_data.schools}
    for spell in spells:
        for school in spell.schools:
            categories_in_school[school][spell.category] = True
    for school in rise_data.schools:
        if len(categories_in_school[school]) < 2:
            warn(f"School {school} has only {len(categories_in_school[school])} spell categories")


def generate_mystic_sphere_latex(check=False):
    mystic_spheres = generate_mystic_spheres()
    if check:
        sanity_check(mystic_spheres)
    mystic_sphere_texts = []
    for mystic_sphere in mystic_spheres:
        try:
            mystic_sphere_texts.append(mystic_sphere.to_latex())
        except Exception as e:
            raise Exception(f"Error converting mystic sphere '{mystic_sphere.name}' to LaTeX") from e
    return latexify('\n\\newpage'.join(mystic_sphere_texts))


def write_to_file(check=None):
    mystic_sphere_latex = generate_mystic_sphere_latex(check)
    with open(book_path('mystic_sphere_descriptions.tex'), 'w') as mystic_sphere_descriptions_file:
        mystic_sphere_descriptions_file.write(mystic_sphere_latex)


@click.command()
@click.option('-c', '--check/--no-check', default=False)
@click.option('-o', '--output/--no-output', default=False)
def main(output, check):
    if output:
        write_to_file(check)
    else:
        print(generate_mystic_sphere_latex(check))

if __name__ == "__main__":
    main()
