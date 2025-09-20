from enum import Enum

class UnitType(Enum):
    InfantryUnitType = "I"
    TankUnitType = "TK"
    RecceUnitType = "R"
    ArtilleryUnitType = "A"
    AntiTankUnitType = "AT"
    AntiAircraftUnitType = "AA"
    HeadquartersUnitType = "HQ"
    EngineersUnitType = "E"
    TankRecoveryUnitType = "R"
    SquadronGroundSupportUnitType = "SGSU"
    TruckUnitType = "TR"


class UnitClass(Enum):
    pass


class Unit:
    def __init__(self, name: str, unit_type: UnitType, abbreviation: str):

        self.name: str = name
        self.unit_type: UnitType =  unit_type
        self.abbreviation: str = abbreviation

        # See §3.5 for these definitions.

        # Unit's training, combat experience, and esprit d'corps.  Range: -3 (bad) to +3 (good).
        self.basic_morale_rating: int = 0

        # Unit's ability to withstand anti-armour fire.
        self.armour_protection_rating: int = 0

        # Ability to engage enemy forces in "hand-to-hand" (close) combat.
        self.offensive_close_assault_rating: int = 0

        # Ability to defend against close assault.
        self.defensive_assault_rating: int = 0

        # Ability to shoot down aircraft.
        self.anti_aircraft_rating: int = 0

        # Manpower, tank platoon, or battery count for the unit (see §4.46)
        self.maximum_toe_strength: int = 0

        # A combat strength expressing the unit's ability to inflict damage when firing as an artillery piece.
        self.barrage_rating: int = 0

        # The unit's ability to execute movement and combat
        self.capability_point_allowance: int = 0

        # A gun's susceptibility to being destroyed or captured when in a Forward Position (§12.1)
        self.vulnerability: int = 0

        # Unit's ability to destroy armoured vehicles.
        self.anti_armour_strength: int = 0

        # A vehicle's fuel efficiency.
        self.fuel_rate: int = 0

        # Construction quality, ease of maintenance, and unit mechanical competence.
        self.breakdown_adjustment_rating: int = 0

        # Arrival date, according to order of battle, (turn/stage, or "D" for initial deployment).
        self.arrival_date = "D"

    @staticmethod
    def create(unit_name: str,
               unit_type: UnitType,
               abbreviation: str,
               basic_morale_rating: int,
               capability_point_allowance: int,
               anti_aircraft_rating: int,
               barrage_rating: int,
               anti_armour_strength: int,
               vulnerability: int,
               armour_protection_rating: int,
               offensive_close_assault_rating: int,
               defensive_assault_rating: int,
               maximum_toe_strength: int,
               arrival_date: str):
        u = Unit(unit_name, unit_type, abbreviation)
        u.basic_morale_rating = basic_morale_rating
        u.capability_point_allowance = capability_point_allowance
        u.anti_aircraft_rating = anti_aircraft_rating
        u.barrage_rating = barrage_rating
        u.anti_armour_strength = anti_armour_strength
        u.vulnerability = vulnerability
        u.armour_protection_rating = armour_protection_rating
        u.offensive_close_assault_rating = offensive_close_assault_rating
        u.defensive_assault_rating = defensive_assault_rating
        u.maximum_toe_strength = maximum_toe_strength
        u.arrival_date = arrival_date
        return u

class HeadquartersUnit(Unit):
    def __init__(self):
        self.attached_units = []

    def get_capability_point_allowance(self):
        # Return the "slowest" CPA of any attached units
        # FIXME: what if there are none?
        return None

        
# 31st Field Artillery Unit, 4th Indian Division (withdrawn mid-December 1940, returned April 1941)
U_31Fld = Unit.create(
    "31st Field Artillery Unit", UnitType.ArtilleryUnitType, "31Fld",
    1, 20, 0, 0,
    0, 0, 0, 0,
    0, 0, 6,  "D")

# 2nd Scots Guard, unassigned British, infantry-type units.  Served under 22nd Guards Brigade.
U_2SctGds = Unit.create(
    "2nd Scots Guard", UnitType.InfantryUnitType, "2SctGds",
    1, 10, 0, 0,
    0, 0, 0, 1,
    2, 6, "D")

# 1st Company French Motor Marine Battalion, unassigned Allied units.
# FIXME: CPA shown as "10+" ?
# See Errata, §4.44b, #3: '3/65' is incorrect, it should be 'D'.
U_1FMM = Unit.create(
    "1st Coy French Motor Marines", UnitType.InfantryUnitType, "1FMM",
    1, 10, 0, 0,
    0, 0, 0, 1,
    1,  1, "D")

# 1st Kings Royal Rifle Corps, 7th Armoured Division.
U_1KRRC = Unit.create(
    "1st Kings Royal Rifle Corps", UnitType.ArtilleryUnitType, "1KRRC",
    2, 10, 0, 0,
    0, 0, 0, 1,
    2, 6, "D")

# 3rd Coldstream Guards, Unassigned British, infantry-type units.
U_3CldGds = Unit.create(
    "3rd Coldstream Guards", UnitType.InfantryUnitType, "3CldGds",
    1, 10, 0, 0,
    0, 0, 0, 1,
    2, 6, "D")

# 4th Royal Horse Artillery, 7th Armoured Division.
U_4RHA = Unit.create(
    "4th Royal Horse Artillery", UnitType.ArtilleryUnitType, "4RHA",
    2, 20, 0, 0,
    0, 0, 0, 0,
    0, 6, "D")

U_7Med = Unit.create(
    "7th Medium  Artillery Regiment", UnitType.ArtilleryUnitType, "7Med",
    1, 20, 0, 0,
    0, 0, 0, 0,
    0, 6, "D")
