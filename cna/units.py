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
    def __init__(self, name: str, unit_type: UnitType):

        self.name: str = name
        self.unit_type: UnitType =  unit_type

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

class HeadquartersUnit(Unit):
    def __init__(self):
        self.attached_units = []

    def get_capability_point_allowance(self):
        # Return the "slowest" CPA of any attached units
        # FIXME: what if there are none?
        return None

        

Artillery31stFieldArtilleryUnit = u = Unit("31st Field Artillery Unit", UnitType.ArtilleryUnitType)
u.basic_morale_rating = +1  # FIXME: shown at "+1(0)" ?
u.capability_point_allowance = 20
u.anti_aircraft_rating = 0
u.barrage_rating = 0
u.anti_armour_strength = 0
u.vulnerability = 0
u.armour_protection_rating = 0
u.offensive_close_assault_rating = 0
u.defensive_assault_rating = 0
u.maximum_toe_strength = 6  # FIXME: comment "May assign up to 5 artillery TOE strength points" ?
u.arrival_date = "D"

Infantry2ndScotsGuards = u = Unit("2nd Scots Guard", UnitType.InfantryUnitType)
u.basic_morale_rating = +1
u.capability_point_allowance = 10
u.anti_aircraft_rating = 0
u.barrage_rating = 0
u.anti_armour_strength = 0
u.vulnerability = 0
u.armour_protection_rating = 0
u.offensive_close_assault_rating = 1
u.defensive_assault_rating = 2
u.maximum_toe_strength = 6
u.arrival_date = "D"

Infantry1stCoyFrenchMotorMarines = u = Unit("1st Coy French Motor Marines", UnitType.InfantryUnitType)
u.basic_morale_rating = +1
u.capability_point_allowance = 10  # FIXME: shown as "10+" ?
u.anti_aircraft_rating = 0
u.barrage_rating = 0
u.anti_armour_strength = 0
u.vulnerability = 0
u.armour_protection_rating = 0
u.offensive_close_assault_rating = 1
u.defensive_assault_rating = 1
u.maximum_toe_strength = 1
u.arrival_date = "D"   # See Errata, §4.44b, #3: '3/65' is incorrect, it should be 'D'.
