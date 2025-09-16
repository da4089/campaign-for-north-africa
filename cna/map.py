from enum import Enum


class TerrainType(Enum):
    """Types of game board hex terrain."""
    Clear = "Clear"
    SaltMarsh = "SaltMarsh"
    Desert = "Desert"
    RockGravel = "RockGravel"
    Rough = "Rough"
    Mountain = "Mountain"
    HeavyVegetation = "HeavyVegetation"
    Delta = "Delta"
    Swamp = "Swamp"
    Sea = "Sea"
    Coast = "Coast"
    Port = "Port"
    MajorCity = "MajorCity"
    VillageBir = "VillageBir"
    Oasis = "Oasis"


class FeatureType(Enum):
    """Types of features inhabiting game board hexes."""
    Road = "Road"
    UnfinishedRoad = "UnfinishedRoad"
    Track = "Track"
    Railroad = "Railroad"
    UnfinishedRailroad = "UnfinishedRailroad"
    Ridge = "Ridge"
    Escarpment = "Escarpment"
    Slope = "Slope"
    Wadi = "Wadi"
    Border = "Border"
    Airfield = "Airfield"
    FlyingBoatBasin = "FlyingBoatBasin"
    FlyingBoatAlightingArea = "FlyingBoatAlightingArea"
    MajorRiver = "MajorRiver"
    MinorRiver = "MinorRiver"
    TrainingArea = "TrainingArea"


class HexEdge(Enum):
    """The six edges of a hex."""
    NorthEast = "NE"
    East = "E"
    SouthEast = "SE"
    SouthWest = "SW"
    West = "W"
    NorthWest = "NW"


class HexRef:
    """A reference to a specific hex, like 'A1234'."""
    def __init__(self, map_letter, column, row):
        self.map: str = map_letter
        self.column: int = column
        self.row: int = row

    @staticmethod
    def from_string(s: str) -> "HexRef":
        board_hex = HexRef(s[0], int(s[1:2]), int(s[3:4]))
        return board_hex


class Hex:
    """A single hex in the game map."""
    def __init__(self, game_map: "Map", hex_ref: HexRef):
        self.map: Map = game_map
        self.ref = hex_ref

        # The basic type of terrain for this hex.
        self.terrain_type: TerrainType = TerrainType.Clear

        # A set of features of this hex.
        self.features: set[HexFeature] = set()


class HexFeature:
    """A single feature of a game board hex."""
    def __init__(self, game_hex: Hex, feature_type: FeatureType):
        # The game board hex that has this feature.
        self.hex: Hex = game_hex

        # The type code for this feature.
        self.feature_type: FeatureType = feature_type

        # If the feature is an "edge" feature, which edges of the hex have it.
        self.edges: list[HexEdge] = []


class FeatureChain:
    """A linear chain of features, eg. a river, road, or track."""
    def __init__(self, features: list[HexFeature]):
        # An ordered list of the HexFeatures comprising the chain.
        self.features = features


class Map:
    """The entire game map; a collection of hexes."""
    def __init__(self):
        self.hexes: dict[HexRef, Hex] = dict()

        # Each map page has coordinates 0101 to 6134.
        # FIXME: check overlap -- is it really 34?
