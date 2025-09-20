from .units import U_1KRRC

from .units import Unit, U_2SctGds, U_1FMM, U_31Fld, U_3CldGds, U_4RHA, U_1KRRC, U_7Med
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
        # Axis forces §60.3
        self.axis_deployments: list[Deployment] = [
            # TBD
        ]

        # Commonwealth forces §60.4
        self.commonwealth_deployments: list[Deployment] = [
            Deployment('C4131',
                       [U_2SctGds, U_31Fld],
                       0, 10, 0),
            Deployment('C3926',
                       [U_1FMM],
                       0, 2, 0),
            Deployment('C2926',
                       [U_3CldGds, U_1KRRC, U_4RHA, U_7Med],
                       0, 15, 5),
            Deployment('C3721', [],
                       5, 5, 0),
            Deployment('C3520', [],
                       0, 5, 0),
            Deployment('C3320', [],
                       0, 10, 0),
            Deployment('C3020', [],
                       0, 3, 0),
            Deployment('D3714', [],
                       5, 15, 5),
            Deployment('D3612', [],
                       5, 5, 5),
            Deployment('D3615', [],
                       5, 20, 2),
            Deployment('E1929', [],
                       0, 20, 0),
            Deployment('E3613', [], # Rules say: E3613 or 3714 (Alexandria)
                       10, 15, 3),
            Deployment('E1430', [],  # Rules say: "Cairo and/or Helwan" (E1430 is Helwan)
                       0, 0, 0),
            Deployment('E1730', [],  # Rules say: "Cario", which is 5 hexes around E1730
                       0, 0, 0),
            Deployment('E1830', [],
                       0, 0, 0),
            # FIXME: there's then an "Anywhere on map D or E deployment.  So that will need a user choice.
        ]

        # §60.42 Commonwealth North African Air Force
        # Can be placed at any facility subject to capacity
        # Plane / Available / Refitted
        # Lysanders / 12 / 8
        # Bombays / 15 / 12
        # Sunderlands / 18 / 11
        # Blenheim I / 26 / 18
        # Blenheim IV / 12 / 12
        # Blenheim IVF / 9 / 5
        # Gladiators / 36 / 30
        # Hurricane I / 6 / 4
        # Morane 406 / 4 / 2
        # Potez 63/11 / 2 / 2
        # Valencia / 3 / 1
        # Pilots available: 1 three, 5 two, 8 one
        # SGSU available: 14

        # §60.43 Commonwealth Second/Third-line Trucks
        # any hex in Cairo: 40m 10h
        # Alexandria: 10l 10m
        # Anywhere: 15l 40m 5h
        # Any air facility: 5l 30m 20h

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

        # Setup actions.

        # Deploy trucks to Cairo: 40m 10h
        # Deploy tricks to Alexandria: 10l 10m
        # Deploy trucks to anywhere: 15l 40m 5h
        # Deploy trucks to air facilities: 5l 30m 20h
