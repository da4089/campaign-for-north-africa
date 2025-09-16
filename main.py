import uuid


class Task:
    """A Task describes something that must be done by a player.
    Tasks are enqueued for a team, when a stage or phase is executed."""
    def __init__(self, task_id):
        self.task_id = task_id

class Action:
    """An Action is something a player does, usually in response to a Task.  The action records who, when, and what was done."""
    def __init__(self, player, task):
        self.player = player
        self.task = task


class Stage:
    def __init__(self, turn: "GameTurn"):
        self.turn = turn

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.log("stage complete")


class Phase:
    def __init__(self, stage: "Stage"):
        self.stage = stage

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class Segment:
    def __init__(self, phase: "Phase"):
        self.phase = phase

    def log(self, message: str):
        self.phase.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("segment start")
        self.log("segment complete")



class GameTurn:

    # See §5.0 for a description of the phases comprising a turn and stage.

    def __init__(self, game: "Game", turn: int):

        # Parent game.
        self.game = game
        assert self.game is not None

        # Turn index, 0-99 being weeks 1-100 of the campaign.
        self.turn = turn
        assert 0 <= self.turn < 100

        # Land game.
        self.initiative_determination_stage = LandGameInitiativeDeterminationStage(self)
        self.naval_convoy_stage = LandGameNavalConvoyStage(self)
        self.operations_stage1 = LandGameOperationsStage(self, 1)
        self.operations_stage2 = LandGameOperationsStage(self, 2)
        self.operations_stage3 = LandGameOperationsStage(self, 3)
        self.end_of_turn_stage = LandGameEndOfTurnStage(self)

    def log(self, message: str):
        self.game.log(f"[Turn {self.turn}] {message}")

    def play(self):
        self.initiative_determination_stage.play()
        self.naval_convoy_stage.play()
        self.operations_stage1.play()
        self.operations_stage2.play()
        self.operations_stage3.play()
        self.end_of_turn_stage.play()


################################################################
# Stages

class LandGameInitiativeDeterminationStage(Stage):
    pass

class LandGameNavalConvoyStage(Stage):
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)
        self.naval_convoy_schedule_phase = LandGameNavalConvoySchedulePhase(self)
        self.tactical_shipping_phase = LandGameTacticalShippingPhase(self)

    def play(self):
        self.log("stage start")
        self.naval_convoy_schedule_phase.play()
        self.tactical_shipping_phase.play()
        self.log("stage complete")


class LandGameOperationsStage(Stage):
    def __init__(self, turn: "GameTurn", number: int):
        super().__init__(turn)
        self.number = number

        self.initiative_declaration_phase = LangGameInitiativeDeclarationPhase(self)
        self.weather_determination_phase = LandGameWeatherDeterminationPhase(self)
        self.organization_phase = LandGameOrganizationPhase(self)
        self.naval_convoy_arrival_phase = LandGameNavalConvoyArrivalPhase(self)
        self.commonwealth_fleet_phase = LandGameCommonwealthFleetPhase(self)
        self.reserve_designation_phase = LandGaneReserveDesignationPhase(self)
        self.movement_and_combat_phase = LandGameMovementAndCombatPhase(self)
        self.truck_convoy_movement_phase = LandGameTruckConvoyMovementPhase(self)
        self.commonwealth_rail_movement_phase = LandGameCommonwealthRailMovementPhase(self)
        self.repair_phase = LandGameRepairPhase(self)
        self.patrol_phase = LandGamePatrolPhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__} {self.number}] {message}")

    def play(self):
        self.log("stage start")
        self.initiative_declaration_phase.play()
        self.weather_determination_phase.play()
        self.organization_phase.play()
        self.naval_convoy_arrival_phase.play()
        self.commonwealth_fleet_phase.play()
        self.reserve_designation_phase.play()
        self.movement_and_combat_phase.play()
        self.truck_convoy_movement_phase.play()
        self.commonwealth_rail_movement_phase.play()
        self.repair_phase.play()
        self.patrol_phase.play()
        self.log("stage complete")


class LandGameEndOfTurnStage(Stage):
    pass


class AirGameInitiativeDeterminationStage(Stage):
    pass

class AirGameStrategicAirPlanningStage(Stage):
    """Air game, §33.0 p3."""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

        self.designation_phase = AirGameDesignationPhase(self)
        self.axis_malta_availability_phase = AirGameAxisMaltaAvailabilityDeterminationPhase(self)
        self.strategic_mission_assignment_phase = AirGameStrategicMissionAssignmentPhase(self)
        self.malta_raid_phase = AirGameMaltaRaidPhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__} {message}")

    def play(self):
        self.log("stage start")
        self.designation_phase.play()
        self.axis_malta_availability_phase.play()
        self.strategic_mission_assignment_phase.play()
        self.malta_raid_phase.play()
        self.log("stage complete")


class AirGameNavalConvoyStage(Stage):
    """Air Game, §33.0 p3."""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

        self.naval_convoy_schedule_phase = AirGameNavalConvoySchedulePhase(self)
        self.convoy_resolution_phase = AirGameConvoyResolutionPhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.naval_convoy_schedule_phase.play()
        self.convoy_resolution_phase.play()
        self.log("stage complete")


class AirGameOperationsStage(Stage):
    """Air Game, §33.0 p3."""
    def __init__(self, turn: "GameTurn", number: int):
        super().__init__(turn)
        self.number = number

        self.initiative_declaration_phase = AirGameInitiativeDeclarationPhase(self)
        self.weather_determination_phase = AirGameWeatherDeterminationPhase(self)
        self.organization_phase = AirGameOrganizationPhase(self)
        self.naval_convoy_arrival_phase = AirGameNavalConvoyArrivalPhase(self)
        self.commonwealth_fleet_phase = AirGameCommonwealthFleetPhase(self)
        self.land_support_air_phase = AirGameLandSupportAirPhase(self)
        self.reserve_designation_phase = AirGameReserveDesignationPhase(self)
        self.movement_and_combat_phase = AirGameMovementAndCombatPhase(self)
        self.truck_convoy_movement_phase = AirGameTruckConvoyMovementPhase(self)
        self.commonwealth_rail_movement_phase = AirGameCommonwealthRailMovementPhase(self)
        self.repair_phase = AirGameRepairPhase(self)
        self.patrol_phase = AirGamePatrolPhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.initiative_declaration_phase.play()
        self.weather_determination_phase.play()
        self.organization_phase.play()
        self.naval_convoy_arrival_phase.play()
        self.commonwealth_fleet_phase.play()
        self.land_support_air_phase.play()
        self.reserve_designation_phase.play()
        self.movement_and_combat_phase.play()
        self.truck_convoy_movement_phase.play()
        self.commonwealth_rail_movement_phase.play()
        self.repair_phase.play()
        self.patrol_phase.play()
        self.log("stage complete")


class AirGameStrategicAirRecoveryStage(Stage):
    """Air Game, §33.0 p4."""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

        self.return_to_base_phase = AirGameReturnToBasePhase(self)
        self.aircraft_maintenance_phase = AirGameAircraftMaintenancePhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.return_to_base_phase.play()
        self.aircraft_maintenance_phase.play()
        self.log("stage complete")


class AirGameEndOfTurnStage(Stage):
    pass



################################################################
# Phases

class AirGameDesignationPhase(Phase):
    """Air Game, §33.0 p3.
    The Players assign their airplanes to fly Land Support or Strategic missions."""
    pass

class AirGameAxisMaltaAvailabilityDeterminationPhase(Phase):
    """Air Game, §33.0 p3.
    The Axis player determines the amount of support they will receive
    from their abstracted North African Theatre air force for Raids on Malta."""
    pass

class AirGameStrategicMissionAssignmentPhase(Phase):
    """Air Game, §33.0 p3.
    Planes designated as flying Strategic Missions are assigned.
    The Axis Player assigns their planes to Raids on Malta or naval convoy protection.
    The Commonwealth Player assigns their planes to Naval Recon missions or Bombing Reserve."""
    pass

class AirGameMaltaRaidPhase(Phase):
    """Air Game, §33.0 p3.
    The Axis Player resolves flak suppression, anti-aircraft fire and bombing missions
    against Maltese air facilities.  Note that Commonwealth warships stationed at Valetta
    may only be attacked by Land Support Missions."""
    pass

class AirGameNavalConvoySchedulePhase(Phase):
    """Air Game, §33.0 p3.
    The Axis Player refers to the Axis Naval Convoy Level Chart and then to the Axis Convoy
    Capacity Table and rolls one die to determine the total tonnage available for the _next_
    Game Turn.  They then plan what specific cargoes the convoys will carry and their routes."""
    pass

class AirGameInitiativeDeclarationPhase(Phase):
    pass

class AirGameWeatherDeterminationPhase(Phase):
    pass

class AirGameOrganizationPhase(Phase):
    pass

class AirGameNavalConvoyArrivalPhase(Phase):
    pass

class AirGameCommonwealthFleetPhase(Phase):
    pass

class AirGameLandSupportAirPhase(Phase):
    pass

class AirGameReserveDesignationPhase(Phase):
    pass

class AirGameMovementAndCombatPhase(Phase):
    pass

class AirGameTruckConvoyMovementPhase(Phase):
    pass

class AirGameCommonwealthRailMovementPhase(Phase):
    pass

class AirGameRepairPhase(Phase):
    pass

class AirGamePatrolPhase(Phase):
    pass

class AirGameReturnToBasePhase(Phase):
    """Air Game, §33.0 p4.
    All surviving planes from missions flown in Stage II (Strategic Air Planning Stage)
    are returned to their base or origin, if possible."""
    pass

class AirGameAircraftMaintenancePhase(Phase):
    """Air Game, §33.0 p4.
    Both players may attempt to ready planes that have flown missions during the Strategic Air Stage."""
    pass



class AirGameConvoyResolutionPhase(Phase):
    """Air Game, §33.0 p3."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

        self.naval_convoy_reconnaissance_segment = AirGameNavalConvoyReconnaissanceSegment(self)
        self.convoy_lane_assignment_segment = AirGameConvoyLanAssignmentSegment(self)
        self.convoy_bombing_segment = AirGameConvoyBombingSegment(self)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__} {message}")

    def play(self):
        self.log("segment start")
        self.naval_convoy_reconnaissance_segment.play()
        self.convoy_lane_assignment_segment.play()
        self.convoy_bombing_segment.play()
        self.log("segment complete")


class LandGameNavalConvoySchedulePhase(Phase):
    """Land game (§5.2, p11), Naval Convoy Stage."""
    pass

class AirGameNavalConvoySchedulePhase(Phase):
    """Air game (§33.0, p3), Naval Convoy Stage."""
    pass

class LandGameTacticalShippingPhase(Phase):
    """Land game, Naval Convoy Stage, §5.2, p12"""
    pass

class AirGameConvoyResolutionPhase(Phase):
    """Air game."""
    pass


class LangGameInitiativeDeclarationPhase(Phase):
    pass

class LandGameWeatherDeterminationPhase(Phase):
    pass

class LandGameOrganizationPhase(Phase):
    pass

class LandGameNavalConvoyArrivalPhase(Phase):
    pass

class LandGameCommonwealthFleetPhase(Phase):
    pass

class LandGaneReserveDesignationPhase(Phase):
    pass

class LandGameMovementAndCombatPhase(Phase):
    pass

class LandGameTruckConvoyMovementPhase(Phase):
    pass

class LandGameCommonwealthRailMovementPhase(Phase):
    pass

class LandGameRepairPhase(Phase):
    pass

class LandGamePatrolPhase(Phase):
    pass



################################################################
# Segments (Air game)

class AirGameNavalConvoyReconnaissanceSegment(Segment):
    """Air game."""
    pass

class AirGameConvoyLanAssignmentSegment(Segment):
    """Air game."""
    pass

class AirGameConvoyBombingSegment(Segment):
    """Air game."""
    pass



class Queue:
    
    # Each team has a queue of tasks to be performed, populated by the
    # game.  Initially, I think I'll just make this a single queue,
    # but it might be nice to have a policy that automatically assigns
    # tasks to different player roles, based on the type of task, the
    # location, etc.
    
    def __init__(self):
        self.tasks = []


class Player:
    def __init__(self, login: str, name: str):
        self.login: str = login
        self.name: str = name


class Team:
    def __init__(self, game: "Game"):
        self.game = game
        self.players = []
        self.queue = Queue()

    def add_player(self, player: "Player"):
        self.players.append(player)


class Scenario:
    """There are multiple starting scenarios described by the rules in §59-64.

    The final scenario is the complete campaign.  The others focus on a
    specific part of the campaign, a location, or an historical figure.

    Each scenario defines starting forces, deployments, supplies, special
    rules/variations, and victory conditions."""

    def __init__(self, game: "Game"):
        self.game = game

    def check_victory(self) -> str|None:
        """Check if either team has won.

        Returns: None for no result, otherwise a string team name."""
        return None


class Game:
    def __init__(self, server: "Server"):
        self.server = server
        self.axis = Team(self)
        self.commonwealth = Team(self)

        # A game consists of 100 turns, roughly two years of battle.
        self.turn_index = 0
        self.turns = []
        for i in range(100):
            self.turns.append(GameTurn(self, i))

    @staticmethod
    def log(message: str):
        print(message)

    def get_axis(self):
        return self.axis

    def get_commonwealth(self):
        return self.commonwealth

    def get_next_stage(self):
        # Get current turn
        # Get next stage from turn
        # if no next stage, advance to next turn, and get first stage

        turn = self.turns[self.turn_index]
        stage = turn.get_next_stage()
        if not stage:
            self.turn_index += 1
            if self.turn_index >= 100:
                return None
            turn = self.turns[self.turn_index]
            stage = turn.get_first_stage()

        return stage

    def do_turn(self, number: int):
        self.turns[number].play()

    def play(self):
        for turn_number in range(1, 6):  # FIXME:  101):
            self.do_turn(turn_number)


class Server:

    # A server can host zero-or-more games.
    # A server has zero-or-more players.
    # Games are created.
    # Players join a team in a game.
    
    def __init__(self):
        self.players = []
        self.games = []


    # Create server

    # Create players
    def add_player(self, login: str, name: str):
        player = Player(login, name)
        self.players.append(player)
        return player

    # New Game
    def add_game(self):
        game = Game(self)
        self.games.append(game)
        return game

    # Add players to game
    # Start game turn
    # Pause game
    # Concede
    
    

if __name__ == "__main__":

    s = Server()

    p1 = s.add_player("p1", "p1")
    p2 = s.add_player("p2", "p2")

    g = s.add_game()
    g.get_commonwealth().add_player(p1)
    g.get_axis().add_player(p2)

    g.play()

