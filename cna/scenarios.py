from .units import Unit, Infantry2ndScotsGuards, Artillery31stFieldArtilleryUnit, Infantry1stCoyFrenchMotorMarines
from .map import HexRef

class Deployment:
    def __init__(self, board_hex: str, units: list[Unit], light_trucks: int, medium_trucks: int, heavy_trucks: int):
        self.hex: HexRef = HexRef.from_string(board_hex)
        self.unit: list[Unit] = units
        self.light_trucks: int = light_trucks
        self.medium_trucks: int = medium_trucks
        self.heavy_trucks: int = heavy_trucks


class Scenario:
    pass

class TheItaliansGrazianisOffensiveScenario(Scenario):
    """See §60.0"""
    pass

class TheItaliansItalianCampaignScenario(Scenario):
    """See §60.0"""
    pass

class TheDesertFoxArrivalScenario(Scenario):
    """See §61.0"""
    pass

class TheDesertFoxRaceForTobrukScenario(Scenario):
    """See §61.0"""
    pass

class OperationCrusaderScenario(Scenario):
    """See §62.0"""
    pass

class ElAlameinTheLastChanceScenario(Scenario):
    """See §63.0"""
    pass

class ElAlameinTheLongRetreatScenario(Scenario):
    """See §63.0"""
    pass

class CampaignForNorthAfricaScenario(Scenario):
    """See §64.0"""

    def __init__(self):
        self.commonwealth_deployments: list[Deployment] = [
            Deployment('C4131',
                       [Infantry2ndScotsGuards, Artillery31stFieldArtilleryUnit],
                       0, 10, 0),
            Deployment('C3926',
                       [Infantry1stCoyFrenchMotorMarines],
                       0, 2, 0),

        ]

        self.axis_deployments: list[Deployment] = [
            # TBD
        ]

        # Both commonwealth and axis
        self.pilots = None
        self.unassigned_trucks = None
        self.supplies = None

        # §60.45
        self.commonwealth_fleet = None

        # §60.46
        self.malta = None

        # §60.47 restrictions on reinforcements, replacements, and training.

        # §60.5 Air facilities
        self.air_facilities = None

        # §60.6 Initiative
        # §60.7 Construction
        # §60.8 Victory conditions


