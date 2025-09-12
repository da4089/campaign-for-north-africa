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


class NavalConvoySchedulePhase(Phase):
    pass

class TacticalShippingPhase(Phase):
    pass

class InitiativeDeclarationPhase(Phase):
    pass

class WeatherDeterminationPhase(Phase):
    pass

class OrganizationPhase(Phase):
    pass

class NavalConvoyArrivalPhase(Phase):
    pass

class CommonwealthFleetPhase(Phase):
    pass

class ReserveDesignationPhase(Phase):
    pass

class MovementAndCombatPhase(Phase):
    pass

class TruckConvoyMovementPhase(Phase):
    pass

class CommonwealthRailMovementPhase(Phase):
    pass

class RepairPhase(Phase):
    pass

class PatrolPhase(Phase):
    pass


class GameTurn:

    # See §5.0 for a description of the phases comprising a turn and stage.

    def __init__(self, game: "Game", turn: int):

        # Parent game.
        self.game = game
        assert self.game is not None

        # Turn index, 0-99 being weeks 1-100 of the campaign.
        self.turn = turn
        assert 0 <= self.turn < 100

        self.initiative_determination_stage = InitiativeDeterminationStage(self)
        self.naval_convoy_stage = NavalConvoyStage(self)
        self.operations_stage1 = OperationsStage(self, 1)
        self.operations_stage2 = OperationsStage(self, 2)
        self.operations_stage3 = OperationsStage(self, 3)
        self.end_of_turn_stage = EndOfTurnStage(self)

    def log(self, message: str):
        self.game.log(f"[Turn {self.turn}] {message}")

    def play(self):
        self.initiative_determination_stage.play()
        self.naval_convoy_stage.play()
        self.operations_stage1.play()
        self.operations_stage2.play()
        self.operations_stage3.play()
        self.end_of_turn_stage.play()


class InitiativeDeterminationStage(Stage):
    pass

class NavalConvoyStage(Stage):
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)
        self.naval_convoy_schedule_phase = NavalConvoySchedulePhase(self)
        self.tactical_shipping_phase = TacticalShippingPhase(self)

    def play(self):
        self.log("stage start")
        self.naval_convoy_schedule_phase.play()
        self.tactical_shipping_phase.play()
        self.log("stage complete")


class OperationsStage(Stage):
    def __init__(self, turn: "GameTurn", number: int):
        super().__init__(turn)
        self.number = number

        self.initiative_declaration_phase = InitiativeDeclarationPhase(self)
        self.weather_determination_phase = WeatherDeterminationPhase(self)
        self.organization_phase = OrganizationPhase(self)
        self.naval_convoy_arrival_phase = NavalConvoyArrivalPhase(self)
        self.commonwealth_fleet_phase = CommonwealthFleetPhase(self)
        self.reserve_designation_phase = ReserveDesignationPhase(self)
        self.movement_and_combat_phase = MovementAndCombatPhase(self)
        self.truck_convoy_movement_phase = TruckConvoyMovementPhase(self)
        self.commonwealth_rail_movement_phase = CommonwealthRailMovementPhase(self)
        self.repair_phase = RepairPhase(self)
        self.patrol_phase = PatrolPhase(self)

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


class EndOfTurnStage(Stage):
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
    pass



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

