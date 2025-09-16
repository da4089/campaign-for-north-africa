from enum import Enum


class TimeOfDay(Enum):
    Never = 'X'
    DayOnly = 'D'
    NightOnly = 'N'
    DayOrNight = 'DN'


class Aircraft:
    def __init__(self, aircraft_id):
        self.aircraft_id = aircraft_id

        # Maximum distance, in hexes, this plane can fly as a return mission.
        # For a (one-way) transfer mission, the maximum distance is twice this value.
        # §34.11
        self.range: int = 0

        # This is the aircraft's combat rating vis a vis other aircraft, based in the
        # number and type of armament carried by the plane.  A unit with a parenthesized
        # TacAir rating (3) may not initiate air-to-air combat.
        # §34.13
        self.tactical_air_combat: int = 0

        # This is the number of Bomb Points, called tonnage (but not actually in tons),
        # that a plane can carry.  Torpedoes are listed separately.
        # §34.14
        self.bombload_capacity: int = 0

        # This is the number of Bomb Points carried by the torpedoes on this plane.
        self.torpedo_capacity: int = 0

        # Transport capacity is measured in TOE Strength Points (for troops), or tons
        # (for supplies) (see case §54.5 for tonnage equivalents, §34.15, §4.44A)
        self.transport_strength: float = 0
        self.transport_tons: int = 0

        # This is a somewhat abstract rating that simulates the ability of a plane to
        # fly faster, higher, and with greater agility than other planes.  Maneuver
        # ratings are always considered in relation to other planes.  Maneuver ratings
        # are used to modify Basic TacAir Differentials.
        # §34.16
        self.maneuver: int = 0

        # This is the number of Fuel Points a plane requires to perform any mission
        # or emergency flight (see Case §37.3).  All Fuel Points are consumed during
        # a mission, regardless of the type or distance of the mission.
        # §34.17
        self.fuel_consumption: int = 0

        # These are the types of missions that the plane can undertake.  Planes may only
        # undertake.  Planes may only undertake missions for which they have capability.
        # For a more complete description, consult the Section on missions, §39.0
        # §34.18
        self.mission_capacity: int = 0

        self.is_flying_boat: bool = False

        # Fighter bombers can take either role, but not both on the same mission (§34.21)
        self.flying_as_fighter: bool = False
        self.flying_as_bomber: bool = False

        # Fighters can be daytime or nighttime (§4.44A)
        self.can_fight: TimeOfDay = TimeOfDay.Never

        # Bombers can be daytime or nighttime (§34.33)
        self.can_bomb: TimeOfDay = TimeOfDay.Never

        # Some planes can strafe (§34.22)
        self.can_strafe: bool = False

        # Some planes can strafe armour too.
        self.can_strafe_armour: bool = False

        # Some planes can do reconnaissance (§34.24)
        self.can_recce: TimeOfDay = TimeOfDay.Never

        # Some bombers can also transport troops or supplies (§34.26)
        self.can_transport: bool = False

        # Planes may remain on the ground, ready to scramble in case of enemy attack.
        # Not all planes are eligible for deployment as scramble forces.
        # Some planes can scramble only at night (§37.14, §40.3,  §40.4)
        self.can_scramble: TimeOfDay = TimeOfDay.Never

        # Bombers cannot initiate combat; fighters can (§4.44A)
        self.can_initiate_combat: bool = False


class BeaufighterMark1F(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Bristol"
        self.model = "Beaufighter"
        self.mark = "IF"

        self.range = 117
        self.tactical_air_combat = 11
        self.maneuver = 30
        self.bombload_capacity = 0
        self.fuel_consumption = 3
        self.can_fight = TimeOfDay.DayOrNight
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True


class BeaufighterMark6F(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Bristol"
        self.model = "Beaufighter"
        self.mark = "VIF"

        self.range = 135
        self.tactical_air_combat = 12
        self.maneuver = 31
        self.bombload_capacity = 0
        self.fuel_consumption = 3
        self.can_fight = TimeOfDay.DayOrNight
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True


class  BlenheimMark4F(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Bristol"
        self.model = "Blenheim"
        self.mark = "IVF"

        self.range = 146
        self.tactical_air_combat = 5
        self.maneuver = 30
        self.bombload_capacity = 0
        self.fuel_consumption = 3
        self.can_fight = TimeOfDay.DayOrNight
        self.can_scramble = TimeOfDay.NightOnly
        self.can_initiate_combat = True


class FulmarMark2(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Fairey"
        self.model = "Fulmar"
        self.mark = "II"

        self.range = 74
        self.tactical_air_combat = 4
        self.maneuver = 29
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOrNight
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True


class GladiatorMark2(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Gloster"
        self.model = "Gladiator"
        self.mark = "II"

        self.range = 44
        self.tactical_air_combat = 2
        self.maneuver = 27
        self.bombload_capacity = 0
        self.fuel_consumption = 1  # FIXME: assumed, table column looks empty?!?
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True


class HurricaneMark1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Hawker"
        self.model = "Hurricane"
        self.mark = "I"

        self.range = 52
        self.tactical_air_combat = 4
        self.maneuver = 32
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True


class HurricaneMark2A(Aircraft):
    def __init__(self, aircraft_id):
        """Defauilt configuraation."""
        super().__init__(aircraft_id)

        self.manufacturer = "Hawker"
        self.model = "Hurricane"
        self.mark = "IIA"

        self.range = 44
        self.tactical_air_combat = 4
        self.maneuver = 36
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True

    def add_droptank(self):
        """Add a drop-tank for additional range."""
        self.range = 88
        self.maneuver = 25
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never

    def add_bombs(self):
        """Add bombload capacity."""
        self.range = 39
        self.maneuver = 33
        self.bombload_capacity = 2
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Never
        self.can_bomb = TimeOfDay.DayOnly
        self.can_bomb = TimeOfDay.DayOnly
        self.can_strafe = True


class HurricaneMark2B(Aircraft):
    def __init__(self, aircraft_id):
        """Defauilt configuraation."""
        super().__init__(aircraft_id)

        self.manufacturer = "Hawker"
        self.model = "Hurricane"
        self.mark = "IIB"

        self.range = 44
        self.tactical_air_combat = 6
        self.maneuver = 36
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True

    def add_droptank(self):
        """Add a drop-tank for additional range."""
        self.range = 88
        self.maneuver = 25
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never

    def add_bombs(self):
        """Add bombload capacity."""
        self.range = 39
        self.maneuver = 32
        self.bombload_capacity = 4
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Never
        self.can_bomb = TimeOfDay.DayOnly
        self.can_strafe = True


class HurricaneMark2C(Aircraft):
    def __init__(self, aircraft_id):
        """Defauilt configuraation."""
        super().__init__(aircraft_id)

        self.manufacturer = "Hawker"
        self.model = "Hurricane"
        self.mark = "IIC"

        self.range = 43
        self.tactical_air_combat = 8
        self.maneuver = 36
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True

    def add_droptank(self):
        """Add a drop-tank for additional range."""
        self.range = 86
        self.maneuver = 25
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never

    def add_bombs(self):
        """Add bombload capacity."""
        self.range = 38
        self.maneuver = 30
        self.bombload_capacity = 6
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Never
        self.can_bomb = TimeOfDay.DayOnly
        self.can_strafe = True


class HurricaneMark2D(Aircraft):
    def __init__(self, aircraft_id):
        """Defauilt configuraation."""
        super().__init__(aircraft_id)

        self.manufacturer = "Hawker"
        self.model = "Hurricane"
        self.mark = "IID"

        self.range = 45
        self.tactical_air_combat = 8
        self.maneuver = 33
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_strafe_armour = True
        self.can_initiate_combat = True

    def add_droptank(self):
        """Add a drop-tank for additional range."""
        self.range = 90
        self.maneuver = 25
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never


class Kittyhawk1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Curtis"
        self.model = "P-40 Kittyhawk"
        self.mark = "I"

        self.range = 71
        self.tactical_air_combat = 4
        self.maneuver = 33
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True

    def add_droptank(self):
        self.range = 94
        self.maneuver = 31
        self.bombload_capacity = 2
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never

    def add_bombs(self):
        self.range = 60
        self.maneuver = 29
        self.bombload_capacity = 2
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Never
        self.can_bomb = TimeOfDay.DayOnly
        self.can_strafe = True


class Kittyhawk2(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Curtis"
        self.model = "P-40 Kittyhawk"
        self.mark = "II"

        self.range = 72
        self.tactical_air_combat = 6
        self.maneuver = 33
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True

    def add_droptank(self):
        self.range = 95
        self.maneuver = 31
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never

    def add_bombs(self):
        self.range = 63
        self.maneuver = 30
        self.bombload_capacity = 2
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Never
        self.can_bomb = TimeOfDay.DayOnly
        self.can_strafe = True


class Kittyhawk3(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Curtis"
        self.model = "P-40 Kittyhawk"
        self.mark = "III"

        self.range = 68
        self.tactical_air_combat = 6
        self.maneuver = 32
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True

    def add_droptank(self):
        self.range = 92
        self.maneuver = 30
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never

    def add_bombs(self):
        self.range = 60
        self.maneuver = 29
        self.bombload_capacity = 2
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Never
        self.can_bomb = TimeOfDay.DayOnly
        self.can_strafe = True


class SeaGladiator(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Gloster"
        self.model = "Sea Gladiator"
        self.mark = ""

        self.range = 38
        self.tactical_air_combat = 2
        self.maneuver = 27
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True


class Skua2(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Blackburn"
        self.model = "Skua"
        self.mark = "II"

        self.range = 76
        self.tactical_air_combat = 3
        self.maneuver = 18
        self.bombload_capacity = 4
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.Never
        self.can_initiate_combat = True


class Spitfire5B(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Supermarine"
        self.model = "Spitfire"
        self.mark = "VB"

        self.range = 39
        self.tactical_air_combat = 6
        self.maneuver = 40
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True


class Spitfire5C(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Supermarine"
        self.model = "Spitfire"
        self.mark = "VC"

        self.range = 43
        self.tactical_air_combat = 8
        self.maneuver = 42
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True

    def add_droptank(self):
        self.range = 59
        self.maneuver = 37
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never


class Tomahawk(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Curtis"
        self.model = "Tomahawk"
        self.mark = ""

        self.range = 62
        self.tactical_air_combat = 2
        self.maneuver = 32
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True

    def add_droptank(self):
        self.range = 75
        self.maneuver = 27
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Never


class Marlet1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Grumman"
        self.model = "Marlet"
        self.mark = "I"

        self.range = 70
        self.tactical_air_combat = 8
        self.maneuver = 34
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.Never
        self.can_initiate_combat = True


class C714(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Caudron"
        self.model = "C.714"
        self.mark = ""

        self.range = 49
        self.tactical_air_combat = 2
        self.maneuver = 30
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.Never
        self.can_initiate_combat = True


class D520(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Dewoitine"
        self.model = "D.520"
        self.mark = ""

        self.range = 56
        self.tactical_air_combat = 4
        self.maneuver = 3
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.Never
        self.can_initiate_combat = True


class MS406(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Morane-Saulnier"
        self.model = "MS406"
        self.mark = ""

        self.range = 45
        self.tactical_air_combat = 4
        self.maneuver = 32
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_fight = TimeOfDay.DayOnly
        self.can_scramble = TimeOfDay.DayOnly
        self.can_initiate_combat = True


# Commonwealth Bombers

class Albacore(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Fairey"
        self.model = "Albacore"
        self.mark = ""

        self.range = 71
        self.tactical_air_combat = 2
        self.maneuver = 6
        self.bombload_capacity = 8
        self.torpedo_capacity = 8
        self.fuel_consumption = 1
        self.can_bomb = TimeOfDay.NightOnly
        self.can_initiate_combat = False


class Anson1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Avro"
        self.model = "Anson"
        self.mark = "I"

        self.range = 71
        self.tactical_air_combat = 2
        self.maneuver = 20
        self.bombload_capacity = 2
        self.fuel_consumption = 2
        self.can_recce = TimeOfDay.DayOnly
        self.can_bomb = TimeOfDay.DayOnly
        self.can_initiate_combat = False


class FlyingFortress(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Boeing"
        self.model = "B-17 Flying Fortress"
        self.mark = "D"

        self.tactical_air_combat = 5
        self.can_initiate_combat = False
        self.configure_for_bombing()

    def configure_for_transfer(self):
        self.range = 275
        self.maneuver = 29
        self.bombload_capacity = 0
        self.fuel_consumption = 5

    def configure_for_bombing(self):
        self.range = 186
        self.maneuver = 27
        self.bombload_capacity = 37
        self.fuel_consumption = 4
        self.can_bomb = TimeOfDay.DayOnly


class Liberator(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Consolidated"
        self.model = "B-24/PB4y Liberator"
        self.mark = "III"

        self.range = 208
        self.tactical_air_combat = 5
        self.can_initiate_combat = False
        self.maneuver = 23
        self.bombload_capacity = 64
        self.fuel_consumption = 7
        self.can_bomb = TimeOfDay.DayOnly


class Mitchell(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "North American"
        self.model = "B-25 Mitchell"
        self.mark = "II"

        self.range = 125
        self.tactical_air_combat = 6
        self.can_initiate_combat = False
        self.maneuver = 25
        self.bombload_capacity = 14
        self.fuel_consumption = 4
        self.can_bomb = TimeOfDay.DayOnly


class Marauder(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Martin"
        self.model = "B-26 Marauder"
        self.mark = ""

        self.tactical_air_combat = 4
        self.can_initiate_combat = False
        self.fuel_consumption = 5
        self.configure_for_bombing()

    def configure_for_bombing(self):
        self.range = 46
        self.maneuver = 25
        self.bombload_capacity = 25
        self.can_bomb = TimeOfDay.DayOnly

    def configure_for_transfer(self):
        self.range = 170
        self.maneuver = 28
        self.bombload_capacity = 0


class Baltimore(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Glenn Martin"
        self.model = "A-30 Baltimore"
        self.mark = "I"

        self.range = 101
        self.tactical_air_combat = 6
        self.can_initiate_combat = False
        self.maneuver = 22
        self.bombload_capacity = 10
        self.fuel_consumption = 3
        self.can_bomb = TimeOfDay.DayOnly


class Beaufort1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Bristol"
        self.model = "Beaufort"
        self.mark = "I"

        self.range = 144
        self.tactical_air_combat = 2
        self.can_initiate_combat = False
        self.maneuver = 24
        self.bombload_capacity = 0
        self.torpedo_capacity = 8
        self.fuel_consumption = 1
        self.can_bomb = TimeOfDay.DayOnly


class Blenheim1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Bristol"
        self.model = "Blenheim"
        self.mark = "I"

        self.range = 101
        self.tactical_air_combat = 1
        self.can_initiate_combat = False
        self.maneuver = 22
        self.bombload_capacity = 5
        self.fuel_consumption = 2
        self.can_bomb = TimeOfDay.DayOnly


class Blenheim4(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Bristol"
        self.model = "Blenheim"
        self.mark = "IV"

        self.range = 131
        self.tactical_air_combat = 3
        self.can_initiate_combat = False
        self.maneuver = 21
        self.bombload_capacity = 6
        self.fuel_consumption = 3
        self.can_bomb = TimeOfDay.DayOnly


class Bombay1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Bristol"
        self.model = "Bombay"
        self.mark = "I"

        self.tactical_air_combat = 1
        self.can_initiate_combat = False
        self.can_transport = True
        self.transport_strength = 1
        self.transport_tons = 10

    def configure_for_transfer(self):
        self.range = 203
        self.maneuver = 6
        self.bombload_capacity = 0
        self.fuel_consumption = 2
        self.can_bomb = TimeOfDay.Never

    def configure_for_bombing(self):
        self.range = 88
        self.maneuver = 5
        self.bombload_capacity = 10
        self.fuel_consumption = 2
        self.can_bomb = TimeOfDay.DayOnly


class Boston3(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Douglas"
        self.model = "Boston"
        self.mark = "III"

        self.range = 102
        self.tactical_air_combat = 5
        self.can_initiate_combat = False
        self.maneuver = 23
        self.bombload_capacity = 10
        self.fuel_consumption = 3
        self.can_bomb = TimeOfDay.DayOnly


class Halifax2(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Handley-Page"
        self.model = "Halifax"
        self.mark = "II"

        self.tactical_air_combat = 5
        self.can_initiate_combat = False
        self.fuel_consumption = 6
        self.can_bomb = TimeOfDay.DayOnly

    def configure_for_long_range(self):
        self.range = 194
        self.maneuver = 27
        self.bombload_capacity = 7

    def configure_for_short_range(self):
        self.range = 62
        self.maneuver = 26
        self.bombload_capacity = 65


class Hudson(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Lockheed"
        self.model = "A-28 Hudson"
        self.mark = ""

        self.range = 145
        self.tactical_air_combat = 3
        self.can_initiate_combat = False
        self.maneuver = 25
        self.bombload_capacity = 0
        self.fuel_consumption = 2
        self.can_transport = True
        self.transport_strength = 1
        self.transport_tons = 10


class Lysander(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Westland"
        self.model = "Lysander"
        self.mark = "I"

        self.range = 60
        self.tactical_air_combat = 2
        self.can_initiate_combat = False
        self.maneuver = 20
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_strafe = True
        self.can_recce = TimeOfDay.DayOnly


class Maryland(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Glenn Martin"
        self.model = "167 Maryland"
        self.mark = ""

        self.range = 76
        self.tactical_air_combat = 3
        self.can_initiate_combat = False
        self.maneuver = 20
        self.bombload_capacity = 9
        self.fuel_consumption = 3
        self.can_bomb = TimeOfDay.DayOnly
        self.can_recce = TimeOfDay.DayOnly


class Potez6311(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Potez"
        self.model = "63.11"
        self.mark = ""

        self.range = 75
        self.tactical_air_combat = 5
        self.can_initiate_combat = False
        self.maneuver = 26
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_recce = TimeOfDay.DayOnly


class Sunderland(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Short"
        self.model = "Sunderland"
        self.mark = ""

        self.tactical_air_combat = 5
        self.can_initiate_combat = False
        self.fuel_consumption = 4

    def configure_for_recce(self):
        self.range = 238
        self.maneuver = 7
        self.bombload_capacity = 0
        self.can_recce = TimeOfDay.DayOnly
        self.can_bomb = TimeOfDay.Never

    def configure_for_bombing(self):
        self.range = 176
        self.maneuver = 11
        self.bombload_capacity = 9
        self.can_recce = TimeOfDay.Never
        self.can_bomb = TimeOfDay.DayOnly


class Swordfish1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Fairey"
        self.model = "Swordfish"
        self.mark = "I"

        self.range = 48
        self.tactical_air_combat = 1
        self.can_initiate_combat = False
        self.maneuver = 7
        self.bombload_capacity = 0
        self.torpedo_capacity = 8
        self.fuel_consumption = 2
        self.can_bomb = TimeOfDay.DayOnly


class TigerMoth2(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "de Haviland"
        self.model = "Tiger Moth"
        self.mark = "II"

        self.range = 27
        self.tactical_air_combat = 0
        self.can_initiate_combat = False
        self.maneuver = 14
        self.bombload_capacity = 0
        self.fuel_consumption = 1
        self.can_recce = TimeOfDay.DayOnly


class Valentia(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = ""
        self.model = ""
        self.mark = ""

        self.range = 32
        self.tactical_air_combat = 0
        self.can_initiate_combat = False
        self.maneuver = 1
        self.bombload_capacity = 10
        self.fuel_consumption = 1
        self.can_bomb = TimeOfDay.DayOnly
        self.can_transport = True
        self.transport_strength = 0.25
        self.transport_tons = 5


class Wellington1(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Vickers"
        self.model = "Wellington"
        self.mark = "I"

        self.tactical_air_combat = 3
        self.can_initiate_combat = False
        self.fuel_consumption = 4
        self.can_bomb = TimeOfDay.DayOrNight   # FIXME: or night only?

    def configure_for_long_range(self):
        self.range = 229
        self.maneuver = 20
        self.bombload_capacity = 5

    def configure_for_short_range(self):
        self.range = 108
        self.maneuver = 18
        self.bombload_capacity = 23


class Wellington4(Aircraft):
    def __init__(self, aircraft_id):
        super().__init__(aircraft_id)

        self.manufacturer = "Vickers"
        self.model = "Wellington"
        self.mark = "IV"

        self.tactical_air_combat = 3
        self.can_initiate_combat = False
        self.fuel_consumption = 5
        self.can_bomb = TimeOfDay.DayOrNight  # FIXME: or night only?

    def configure_for_long_range(self):
        self.range = 220
        self.maneuver = 23
        self.bombload_capacity = 6

    def configure_for_medium_range(self):
        self.range = 157
        self.maneuver = 19
        self.bombload_capacity = 17

    def configure_for_short_range(self):
        self.range = 126
        self.maneuver = 18
        self.bombload_capacity = 23

