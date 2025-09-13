from enum import Enum


class PlaneType(Enum):
    pass

class TimeOfDay(Enum):
    Unset = 'X'
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
        # that a Plane can carry torpedoes that face is listed along with the bombload
        # capacity.
        # §34.14
        self.bombload_capacity: int = 0

        # This is the capacity of the plane, given in TOE Strength Points (infantry)
        # and/or tons of supplies (see case §54.5 for tonnage equivalents).
        # §34.15
        self.transport_capacity: int = 0

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


        self.is_fighter: bool = False
        self.is_bomber: bool = False
        self.is_flying_boat: bool = False
        self.is_transport: bool = False

        # Fighter bombers can take either role, but not both on the same mission (§34.21)
        self.flying_as_fighter: bool = False
        self.flying_as_bomber: bool = False

        self.can_bomb: bool = False

        # Some planes can strafe (§34.22)
        self.can_strafe: bool = False

        self.can_strafe_armour: bool = False

        # Some planes can do reconnaissance (§34.24)
        self.can_recce: bool = False   # FIXME: is this a mission property?  Or a plane property?

        # Some bombers can also transport troops or supplies (§34.26)
        self.can_transport: bool = False

        # Planes may remain on the ground, ready to scramble in case of enemy attack.
        # Not all planes are eligible for deployment as scramble forces.
        # Some planes can scramble only at night (§37.14, §40.3,  §40.4)
        self.can_scramble: TimeOfDay = TimeOfDay.Unset

        # Different types of bombers (§34.33)
        self.is_night_bomber: bool = False
        self.is_dive_bomber: bool = False
        self.is_torpedo_bomber: bool = False

        # Can function at night (ie. night-fighter or night-bomber) (§4.44A)
        self.night_capable: bool = False


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
        self.is_fighter = True
        self.night_capable = True
        self.can_scramble = TimeOfDay.DayOnly


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
        self.is_fighter = True
        self.night_capable = True
        self.can_scramble = TimeOfDay.DayOnly


class  BlenheimMaark4F(Aircraft):
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
        self.is_fighter = True
        self.night_capable = True
        self.can_scramble = TimeOfDay.NightOnly


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
        self.is_fighter = True
        self.night_capable = True
        self.can_scramble = TimeOfDay.DayOnly


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
        self.is_fighter = True
        self.can_scramble = TimeOfDay.DayOnly


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
        self.is_fighter = True
        self.can_scramble = TimeOfDay.DayOnly


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
        self.is_fighter = True
        self.can_scramble = TimeOfDay.DayOnly

    def add_droptank(self):
        """Add a drop-tank for additional range."""
        self.range = 88
        self.maneuver = 25
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Unset

    def add_bombs(self):
        """Add bombload capacity."""
        self.range = 39
        self.maneuver = 33
        self.bombload_capacity = 2
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Unset
        self.can_bomb = True
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
        self.is_fighter = True
        self.can_scramble = TimeOfDay.DayOnly

    def add_droptank(self):
        """Add a drop-tank for additional range."""
        self.range = 88
        self.maneuver = 25
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Unset

    def add_bombs(self):
        """Add bombload capacity."""
        self.range = 39
        self.maneuver = 32
        self.bombload_capacity = 4
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Unset
        self.can_bomb = True
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
        self.is_fighter = True
        self.can_scramble = TimeOfDay.DayOnly

    def add_droptank(self):
        """Add a drop-tank for additional range."""
        self.range = 86
        self.maneuver = 25
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Unset

    def add_bombs(self):
        """Add bombload capacity."""
        self.range = 38
        self.maneuver = 30
        self.bombload_capacity = 6
        self.fuel_consumption = 1
        self.can_scramble = TimeOfDay.Unset
        self.can_bomb = True
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
        self.is_fighter = True
        self.can_scramble = TimeOfDay.DayOnly
        self.can_strafe_armour = True

    def add_droptank(self):
        """Add a drop-tank for additional range."""
        self.range = 90
        self.maneuver = 25
        self.fuel_consumption = 2
        self.can_scramble = TimeOfDay.Unset

