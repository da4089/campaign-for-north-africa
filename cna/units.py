
class UnitType(Enum):
    pass

class UnitClass(Enum):
    pass


class Unit:
    def __init__(self):

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

class HeadquartersUnit(Unit):
    def __init__(self):
        self.attached_units = []

    def get_capability_point_allowance(self):
        # Return the "slowest" CPA of any attached units
        # FIXME: what if there are none?
        return None

        
