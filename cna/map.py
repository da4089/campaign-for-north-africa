from enum import Enum
from typing import Optional


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

        # Map tile.
        # FIXME: one tile per hex?  Maybe that's excessive?
        self.tile = None

        # List of land units deployed in this hex.
        self.units = []

        # Trucks.
        # FIXME: are these individual trucks, or truck points (= 10 trucks)?
        self.light_trucks = []
        self.medium_trucks = []
        self.heavy_trucks = []

        # Supplies.
        # See §54.12 (p14 in common charts).  The capacity limits are set by the FeatureType.
        self.ammo_available: int = 0
        self.fuel_available: int = 0
        self.stores_available: int = 0
        self.water_available: int = 0

        # Does this hex host an air facility?
        self.has_air_facility: bool = False

        # If it is an air facility, is it for flying boats?
        self.is_flying_boat_facility: bool = False

        # Maximum number of air squadrons/SGSUs that can be hosted at this facility.
        self.max_squadron_capacity_level: int = 0

        # Current air squadron capacity level.
        self.squadron_capacity_level: int = 0

        # List of aircraft based at this facility.
        self.aircraft = []

        # List of abandoned vehicles in this hex (§53.32)
        self.abandoned_vehicles = []


    def set_terrain(self, terrain_type: TerrainType):
        self.terrain_type = terrain_type

    def add_feature(self,  feature_type: FeatureType, edges: Optional[list[HexEdge]] = None):
        hf = HexFeature(self, feature_type)
        if edges:
            hf.set_edges(edges)


class HexFeature:
    """A single feature of a game board hex."""
    def __init__(self, game_hex: Hex, feature_type: FeatureType):
        # The game board hex that has this feature.
        self.hex: Hex = game_hex

        # The type code for this feature.
        self.feature_type: FeatureType = feature_type

        # If the feature is an "edge" feature, which edges of the hex have it.
        self.edges: list[HexEdge] = []

    def set_edges(self, edges: list[HexEdge]):
        self.edges = edges


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

    def add_hex(self, ref: str, terrain: TerrainType):
        r = HexRef.from_string(ref)
        h = Hex(self, r)
        h.set_terrain(terrain)
        self.hexes[r] = h
        return h





def init_map(m: Map) -> Map:
    """Initialize the game map."""

    # Hexes (56 x 34 x 5 = 9520!)
    # Roads, tracks, borders (all the chained features)

    m.add_hex("A0101", TerrainType.RockGravel)
    m.add_hex("A0102", TerrainType.RockGravel)
    m.add_hex("A0103", TerrainType.RockGravel)
    m.add_hex("A0104", TerrainType.RockGravel)
    m.add_hex("A0105", TerrainType.RockGravel)
    m.add_hex("A0106", TerrainType.RockGravel)
    m.add_hex("A0107", TerrainType.RockGravel)
    m.add_hex("A0108", TerrainType.RockGravel)
    m.add_hex("A0109", TerrainType.RockGravel)
    m.add_hex("A0110", TerrainType.RockGravel)
    m.add_hex("A0111", TerrainType.RockGravel)
    m.add_hex("A0112", TerrainType.RockGravel)
    m.add_hex("A0113", TerrainType.RockGravel)
    m.add_hex("A0114", TerrainType.RockGravel)
    m.add_hex("A0115", TerrainType.SaltMarsh)
    m.add_hex("A0116", TerrainType.SaltMarsh)
    m.add_hex("A0117", TerrainType.SaltMarsh)
    m.add_hex("A0118", TerrainType.SaltMarsh)
    m.add_hex("A0119", TerrainType.Clear)
    m.add_hex("A0120", TerrainType.Clear)
    m.add_hex("A0121", TerrainType.Clear)
    m.add_hex("A0122", TerrainType.Clear)
    m.add_hex("A0123", TerrainType.Clear)
    m.add_hex("A0124", TerrainType.Clear)
    m.add_hex("A0125", TerrainType.Clear)
    m.add_hex("A0126", TerrainType.Clear)
    m.add_hex("A0127", TerrainType.Clear)
    m.add_hex("A0128", TerrainType.Desert)
    m.add_hex("A0129", TerrainType.Desert)
    m.add_hex("A0131", TerrainType.Desert)
    m.add_hex("A0132", TerrainType.Desert)
    m.add_hex("A0133", TerrainType.Desert)
    m.add_hex("A0134", TerrainType.Desert)

    m.add_hex("A0201", TerrainType.RockGravel)
    m.add_hex("A0202", TerrainType.RockGravel)
    m.add_hex("A0203", TerrainType.RockGravel)
    m.add_hex("A0204", TerrainType.RockGravel)
    m.add_hex("A0205", TerrainType.RockGravel)
    m.add_hex("A0206", TerrainType.RockGravel)
    m.add_hex("A0207", TerrainType.RockGravel)
    m.add_hex("A0208", TerrainType.RockGravel)
    m.add_hex("A0209", TerrainType.RockGravel)
    m.add_hex("A0210", TerrainType.RockGravel)
    m.add_hex("A0211", TerrainType.RockGravel)
    m.add_hex("A0212", TerrainType.RockGravel)
    m.add_hex("A0213", TerrainType.RockGravel)
    m.add_hex("A0214", TerrainType.SaltMarsh)
    m.add_hex("A0215", TerrainType.Clear)
    m.add_hex("A0216", TerrainType.SaltMarsh)
    m.add_hex("A0217", TerrainType.SaltMarsh)
    m.add_hex("A0218", TerrainType.Clear)
    m.add_hex("A0219", TerrainType.Clear)
    m.add_hex("A0220", TerrainType.Clear)
    m.add_hex("A0221", TerrainType.Clear)
    m.add_hex("A0222", TerrainType.Clear)
    m.add_hex("A0223", TerrainType.Clear)
    m.add_hex("A0224", TerrainType.Clear)
    m.add_hex("A0225", TerrainType.Clear)
    m.add_hex("A0226", TerrainType.Clear)
    m.add_hex("A0227", TerrainType.Clear)
    m.add_hex("A0228", TerrainType.Clear)
    m.add_hex("A0229", TerrainType.Desert)
    m.add_hex("A0230", TerrainType.Desert)
    m.add_hex("A0231", TerrainType.Desert)
    m.add_hex("A0232", TerrainType.Desert)
    m.add_hex("A0233", TerrainType.Desert)

    m.add_hex("A0301", TerrainType.RockGravel)
    m.add_hex("A0302", TerrainType.RockGravel)
    m.add_hex("A0303", TerrainType.RockGravel)
    m.add_hex("A0304", TerrainType.RockGravel)
    m.add_hex("A0305", TerrainType.RockGravel)
    m.add_hex("A0306", TerrainType.RockGravel)
    m.add_hex("A0307", TerrainType.RockGravel)
    m.add_hex("A0308", TerrainType.RockGravel)
    m.add_hex("A0309", TerrainType.RockGravel)
    m.add_hex("A0310", TerrainType.RockGravel)
    m.add_hex("A0311", TerrainType.RockGravel)
    m.add_hex("A0312", TerrainType.Rough)
    m.add_hex("A0313", TerrainType.Rough)
    m.add_hex("A0314", TerrainType.Clear)
    m.add_hex("A0315", TerrainType.Clear)
    m.add_hex("A0316", TerrainType.Clear)
    m.add_hex("A0317", TerrainType.Clear)
    m.add_hex("A0318", TerrainType.Clear)
    m.add_hex("A0319", TerrainType.Clear)
    m.add_hex("A0320", TerrainType.Clear)
    m.add_hex("A0321", TerrainType.Clear)
    m.add_hex("A0322", TerrainType.Clear)
    m.add_hex("A0323", TerrainType.Clear)
    m.add_hex("A0324", TerrainType.Clear)
    m.add_hex("A0325", TerrainType.Clear)
    m.add_hex("A0326", TerrainType.Clear)
    m.add_hex("A0327", TerrainType.Clear)
    m.add_hex("A0328", TerrainType.Desert)
    m.add_hex("A0329", TerrainType.Desert)
    m.add_hex("A0330", TerrainType.Desert)
    m.add_hex("A0331", TerrainType.Desert)
    m.add_hex("A0332", TerrainType.Desert)
    m.add_hex("A0333", TerrainType.Desert)
    m.add_hex("A0334", TerrainType.Desert)

    return m




