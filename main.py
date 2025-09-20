import uuid
from datetime import datetime

from cna.map import Map, init_map
from cna.stages import *


class Task:
    """A Task describes something that must be done by a player.
    Tasks are enqueued for a team, when a turn/stage/phase/segment is executed."""
    def __init__(self, task_id):
        self.task_id = task_id

class Action:
    """An Action is something a player does, usually in response to a Task.  The action records who, when, and what was done."""
    def __init__(self, task: Task, player: "Player"):
        self.task = task
        self.player = playerphase
        self.sent_time = datetime.fromordinal(0)
        self.completed_time = datetime.fromordinal(0)


class DeployTrucks(Action):
    def __init__(self, task, player, light_trucks: int, medium_trucks: int, heavy_trucks: int):
        super().__init__(task, player)
        self.task = task
        self.player = player
        self.light_trucks = light_trucks
        self.medium_trucks = medium_trucks
        self.heavy_trucks = heavy_trucks



class GameTurn:

    # See §5.0 for a description of the phases comprising a turn and stage.

    def __init__(self, game: "Game", turn: int):

        # Parent game.
        self.game = game
        assert self.game is not None

        # Turn index.
        self.turn = turn
        assert 0 <= self.turn < 100

        self.initiative_determination_stage = InitiativeDeterminationStage(self)
        self.strategic_air_planning_stage = StrategicAirPlanningStage(self)
        self.naval_convoy_stage = NavalConvoyStage(self)
        self.stores_expenditure_stage = StoresExpenditureStage(self)
        self.operations_stage1 = OperationsStage(self, 1)
        self.operations_stage2 = OperationsStage(self, 2)
        self.operations_stage3 = OperationsStage(self, 3)
        self.strategic_air_recovery_stage = StrategicAirRecoveryStage(self)
        self.end_of_turn_stage = EndOfTurnStage(self)

    def log(self, message: str):
        self.game.log(f"[Turn {self.turn}] {message}")

    def play(self):
        self.initiative_determination_stage.play()
        self.strategic_air_planning_stage.play()
        self.naval_convoy_stage.play()
        self.stores_expenditure_stage.play()
        self.operations_stage1.play()
        self.operations_stage2.play()
        self.operations_stage3.play()
        self.strategic_air_recovery_stage.play()
        self.end_of_turn_stage.play()



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

    def notify_start(self):
        """Notify the team that a turn/stage/phase/segment is starting."""
        pass

    def confirm_end(self):
        """Confirm the completion of the turn/stage/phase/segment."""
        pass

    def notify_task(self):
        """Inform team of a task to be completed in this turn/stage/phase/segment."""
        pass


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

        self.map = Map()
        init_map(self.map)

        self.setup = Setup(self)

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
        self.setup.play()
        for turn_number in range(1, 6):  # FIXME:  101):
            self.do_turn(turn_number)


    def complete_task(self):
        """Notify game engine that all actions for an assigned task are complete."""
        pass


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
    def new_player(self, login: str, name: str):
        player = Player(login, name)
        self.players.append(player)
        return player

    # New Game
    def new_game(self, scenario: str):

        # FIXME:  Look up scenario
        game = Game(self)
        self.games.append(game)
        return game

    # Add players to game
    # game.get_axis().add_player(p1)

    # Start game turn
    # play()

    # Pause game
    # Concede
    
    

if __name__ == "__main__":

    s = Server()

    p1 = s.new_player("p1", "p1")
    p2 = s.new_player("p2", "p2")

    g = s.new_game("cna")
    g.get_commonwealth().add_player(p1)
    g.get_axis().add_player(p2)

    g.play()

