

class OperationStage:
    def __init__(self):
        self.turn = None

    def initiative_declaration_phase(self):
        pass

    def weather_determination_phase(self):
        pass

    def organization_phase(self):
        pass

    def naval_convoy_arrival_phase(self):
        pass

    def commonwealth_fleet_phase(self):
        pass

    def reserve_designation_phase(self):
        pass

    def movement_and_combat_phase(self):
        pass

    def truck_convoy_movement_phase(self):
        pass

    def commonwealth_rail_movement_phase(self):
        pass

    def repair_phase(self):
        pass

    def patrol_phase(self):
        pass
    
    def run(self):
        self.initiative_declaration_phase()
        self.weather_determination_phase()
        self.organization_phase()
        self.naval_convoy_arrival_phase()
        self.commonwealth_fleet_phase()
        self.reserver_designation_phase()
        self.movement_and_combat_phase()
        self.truck_convoy_movement_phase()
        self.commonwealth_rail_movement_phase()
        self.repair_phase()
        self.patrol_phase()
        
        


class GameTurn:

    # See §5.0 for a description of the phases comprising a turn and stage.
    
    def __init__(self):
        self.game = None
        self.stages = []
        self.turn_number: int = 0

    # Phases
    
    def naval_convoy_schedule_phase(self):
        pass

    def tactical_shipping_phase(self):
        pass
    

    # Stages
    
    def initiative_determination_stage(self):
        pass

    def naval_convoy_stage(self):
        self.naval_convoy_schedule_phase()
        self.tactical_shipping_phase()

    def operations_stage(self, number: int):
        pass

    def end_of_turn_stage(self):
        pass


    # Turn
    
    def run(self):
        self.initiative_determination_stage()
        self.naval_convoy_stage()
        self.operations_stage(1)
        self.operations_stage(2)
        self.operations_stage(3)
        self.end_of_turn_stage()
        
    
    

class Game:
    def __init__(self):
        self.turns = []

    def do_operation_stage(self):
        pass

    def do_turn(self):
        pass
    
