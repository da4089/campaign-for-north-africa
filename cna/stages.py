


class Stage:
    def __init__(self, turn):
        self.turn = turn

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.log("stage complete")


class Phase:
    def __init__(self, stage: Stage):
        self.stage = stage

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class Segment:
    def __init__(self, phase: Phase):
        self.phase = phase

    def log(self, message: str):
        self.phase.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("segment start")
        self.log("segment complete")


class Step:
    def __init__(self, segment: Segment):
        self.segment = segment

    def log(self, message: str):
        self.segment.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("step start")
        self.log("step complete")


class Setup:
    def __init__(self, game: "Game"):
        self.game = game

    def log(self, message: str):
        self.game.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("start")
        self.log("complete")


################################################################
# Stages

class InitiativeDeterminationStage(Stage):
    """§48.0 I, p19"""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.log("stage complete")


class StrategicAirPlanningStage(Stage):
    """§48.0 II, p19"""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

        self.designation_phase = DesignationPhase(self)
        self.axis_malta_availability_phase = AxisMaltaAvailabilityDeterminationPhase(self)
        self.strategic_mission_assignment_phase = StrategicMissionAssignmentPhase(self)
        self.malta_raid_phase = MaltaRaidPhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__} {message}")

    def play(self):
        self.log("stage start")
        self.designation_phase.play()
        self.axis_malta_availability_phase.play()
        self.strategic_mission_assignment_phase.play()
        self.malta_raid_phase.play()
        self.log("stage complete")


class DesignationPhase(Phase):
    """§48.0 II-A, p19.
    The Players assign their airplanes to fly Land Support or Strategic missions."""
    pass

class AxisMaltaAvailabilityDeterminationPhase(Phase):
    """§48.0 II-B, p19.
    The Axis player determines the amount of support they will receive
    from their abstracted North African Theatre air force for Raids on Malta."""
    pass

class StrategicMissionAssignmentPhase(Phase):
    """§48.0 II-C, p19.
    Planes designated as flying Strategic Missions are assigned.
    The Axis Player assigns their planes to Raids on Malta or naval convoy protection.
    The Commonwealth Player assigns their planes to Naval Recon missions or Bombing Reserve."""
    pass

class MaltaRaidPhase(Phase):
    """§48.0 II-D, p10.
    The Axis Player resolves flak suppression, anti-aircraft fire and bombing missions
    against Maltese air facilities.  Note that Commonwealth warships stationed at Valetta
    may only be attacked by Land Support Missions."""
    pass


class NavalConvoyStage(Stage):
    """§48.0 III, p19."""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

        self.naval_convoy_schedule_phase = NavalConvoySchedulePhase(self)
        self.convoy_resolution_phase = ConvoyResolutionPhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.naval_convoy_schedule_phase.play()
        self.convoy_resolution_phase.play()
        self.log("stage complete")


class NavalConvoySchedulePhase(Phase):
    """§48.0 III-A, p19.
    The Axis Player refers to the Axis Naval Convoy Level Chart and then to the Axis Convoy
    Capacity Table and rolls one die to determine the total tonnage available for the _next_
    Game Turn.  They then plan what specific cargoes the convoys will carry and their routes."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class ConvoyResolutionPhase(Phase):
    """§48.0 III-B, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

        self.naval_convoy_reconnaissance_segment = NavalConvoyReconnaissanceSegment(self)
        self.convoy_lane_assignment_segment = ConvoyLanAssignmentSegment(self)
        self.convoy_bombing_segment = ConvoyBombingSegment(self)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.naval_convoy_reconnaissance_segment.play()
        self.convoy_lane_assignment_segment.play()
        self.convoy_bombing_segment.play()
        self.log("phase complete")


class NavalConvoyReconnaissanceSegment(Segment):
    """§48.0 III-B-1, p19.
    The Commonwealth Player resolves Strategic Convoy Reconnaissance missions."""
    def __init__(self, phase: Phase):
        super().__init__(phase)

    def log(self, message: str):
        self.phase.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("segment start")
        self.log("segment complete")


class ConvoyLanAssignmentSegment(Segment):
    """§48.0 III-B-2, p19.
    Axis convoy protection aircraft are assigned CAP missions in specific
    convoy lanes.  Commonwealth Bombing Reserve aircraft are assigned CAP,
    Flak Suppression, or Convoy Bombing missions in specific convoy lanes."""
    def __init__(self, phase: Phase):
        super().__init__(phase)

    def log(self, message: str):
        self.phase.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("segment start")
        self.log("segment complete")

class ConvoyBombingSegment(Segment):
    """§48.0 III-B-3, p19.
    All air-to-air combat, flak suppression, anti-aircraft, and convoy
    bombing is carried out."""
    def __init__(self, phase: Phase):
        super().__init__(phase)

    def log(self, message: str):
        self.phase.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("segment start")
        self.log("segment complete")


class StoresExpenditureStage(Stage):
    """§48.0 IV, p19."""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.log("stage complete")


class OperationsStage(Stage):
    """§48.0 V / VI / VII, p19."""
    def __init__(self, turn: "GameTurn", number: int):
        super().__init__(turn)
        self.number = number

        self.initiative_declaration_phase = InitiativeDeclarationPhase(self)
        self.weather_determination_phase = WeatherDeterminationPhase(self)
        self.organization_phase = OrganizationPhase(self)
        self.naval_convoy_arrival_phase = NavalConvoyArrivalPhase(self)
        self.commonwealth_fleet_phase = CommonwealthFleetPhase(self)
        self.land_support_air_phase = LandSupportAirPhase(self)
        self.reserve_designation_phase = ReserveDesignationPhase(self)
        self.movement_and_combat_phase = MovementAndCombatPhase(self)
        self.truck_convoy_movement_phase = TruckConvoyMovementPhase(self)
        self.commonwealth_rail_movement_phase = CommonwealthRailMovementPhase(self)
        self.repair_phase = RepairPhase(self)
        self.patrol_phase = PatrolPhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}-{self.number}] {message}")

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


class InitiativeDeclarationPhase(Phase):
    """§48.0 V-A, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class WeatherDeterminationPhase(Phase):
    """§48.0 V-B, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class OrganizationPhase(Phase):
    """§48.0 V-C, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

        self.water_distribution_segment = WaterDistributionSegment(self)
        self.reorganization_segment = ReorganizationSegment(self)
        self.attrition_segment = AttritionSegment(self)
        self.construction_segment = ConstructionSegment(self)
        self.training_segment = TrainingSegment(self)
        self.supply_distribution_segment = SupplyDistributionSegment(self)
        self.tactical_shipping_segment = TacticalShippingSegment(self)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.water_distribution_segment.play()
        self.reorganization_segment.play()
        self.attrition_segment.play()
        self.construction_segment.play()
        self.training_segment.play()
        self.supply_distribution_segment.play()
        self.tactical_shipping_segment.play()
        self.log("phase complete")


class WaterDistributionSegment(Segment):
    pass

class ReorganizationSegment(Segment):
    pass

class AttritionSegment(Segment):
    pass

class ConstructionSegment(Segment):
    def __init__(self, phase: Phase):
        super().__init__(phase)
        self.construction_completion_step = ConstructionCompletionStep(self)
        self.construction_initiation_continuation_step = ConstructionInitiationContinuationStep(self)

    def log(self, message: str):
        self.phase.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("segment start")
        self.construction_completion_step.play()
        self.construction_initiation_continuation_step.play()
        self.log("segment complete")

class ConstructionCompletionStep(Step):
    pass

class ConstructionInitiationContinuationStep(Step):
    pass

class TrainingSegment(Segment):
    pass

class SupplyDistributionSegment(Segment):
    pass

class TacticalShippingSegment(Segment):
    pass


class NavalConvoyArrivalPhase(Phase):
    """§48.0 V-D, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class CommonwealthFleetPhase(Phase):
    """§48.0 V-E, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)
        self.fleet_assignments_segment = FleetAssignmentsSegment(self)
        self.fleet_repair_segment = FleetRepairSegment(self)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.fleet_assignments_segment.play()
        self.fleet_repair_segment.play()
        self.log("phase complete")

class FleetAssignmentsSegment(Segment):
    pass

class FleetRepairSegment(Segment):
    pass


class LandSupportAirPhase(Phase):
    """§48.0 V-F, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)
        self.mission_assignment_segment = MissionAssignmentSegment(self)
        self.mission_deployment_segment = MissionDeploymentSegment(self)
        self.air_to_air_combat_resolution_segment = AirToAirCombatResolutionSegment(self)
        self.flak_resolution_segment = FlakResolutionSegment(self)
        self.mission_completion_segment = MissionCompletionSegment(self)
        self.return_to_base_segment = ReturnToBaseSegment(self)
        self.tactical_maintenance_segment = TacticalMaintenanceSegment(self)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.mission_assignment_segment.play()
        self.mission_deployment_segment.play()
        self.air_to_air_combat_resolution_segment.play()
        self.flak_resolution_segment.play()
        self.mission_completion_segment.play()
        self.return_to_base_segment.play()
        self.tactical_maintenance_segment.play()
        self.log("phase complete")

class MissionAssignmentSegment(Segment):
    pass

class MissionDeploymentSegment(Segment):
    pass

class AirToAirCombatResolutionSegment(Segment):
    pass

class FlakResolutionSegment(Segment):
    pass

class MissionCompletionSegment(Segment):
    pass

class ReturnToBaseSegment(Segment):
    pass

class TacticalMaintenanceSegment(Segment):
    pass


class ReserveDesignationPhase(Phase):
    """§48.0 V-G, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class MovementAndCombatPhase(Phase):
    """§48.0 V-H, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)
        self.movement_segment = MovementSegment(self)
        self.breakdown_determination_segment = BreakdownDeterminationSegment(self)
        self.combat_segment = CombatSegment(self)
        self.reserve_release_segment = ReserveReleaseSegment(self)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.movement_segment.play()
        self.breakdown_determination_segment.play()
        self.combat_segment.play()
        self.reserve_release_segment.play()
        self.log("phase complete")

class MovementSegment(Segment):
    pass

class BreakdownDeterminationSegment(Segment):
    pass

class CombatSegment(Segment):
    def __init__(self, phase: Phase):
        super().__init__(phase)
        self.position_determination_step = PositionDeterminationStep(self)
        self.barrage_step = BarrageStep(self)
        self.retreat_before_assault_step = RetreatBeforeAssaultStep(self)
        self.force_assignment_step = ForceAssignmentStep(self)
        self.anti_armour_step = AntiArmourStep(self)
        self.close_assault_step = CloseAssaultStep(self)

    def log(self, message: str):
        self.phase.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("segment start")
        self.position_determination_step.play()
        self.barrage_step.play()
        self.retreat_before_assault_step.play()
        self.force_assignment_step.play()
        self.anti_armour_step.play()
        self.close_assault_step.play()
        self.log("segment complete")

class PositionDeterminationStep(Step):
    pass

class BarrageStep(Step):
    pass

class RetreatBeforeAssaultStep(Step):
    pass

class ForceAssignmentStep(Step):
    pass

class AntiArmourStep(Step):
    pass

class CloseAssaultStep(Step):
    pass

class ReserveReleaseSegment(Segment):
    pass


class TruckConvoyMovementPhase(Phase):
    """§48.0 V-J, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class CommonwealthRailMovementPhase(Phase):
    """§48.0 V-K, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class RepairPhase(Phase):
    """§48.0 V-L, p19."""
    def __init__(self, stage: Stage):
        super().__init__(stage)
        self.towing_segment = TowingSegment(self)
        self.maintenance_segment = MaintenanceSegment(self)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.towing_segment.play()
        self.maintenance_segment.play()
        self.log("phase complete")

class TowingSegment(Segment):
    pass

class MaintenanceSegment(Segment):
    pass


class PatrolPhase(Phase):
    """§48.0 V-M, p20."""
    def __init__(self, stage: Stage):
        super().__init__(stage)

    def log(self, message: str):
        self.stage.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("phase start")
        self.log("phase complete")


class StrategicAirRecoveryStage(Stage):
    """§48.0 VIII, p20."""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

        self.return_to_base_phase = ReturnToBasePhase(self)
        self.aircraft_maintenance_phase = AircraftMaintenancePhase(self)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.return_to_base_phase.play()
        self.aircraft_maintenance_phase.play()
        self.log("stage complete")


class ReturnToBasePhase(Phase):
    """§48.0 VIII-A, p20.
    All surviving planes from missions flown in Stage II (Strategic Air Planning Stage)
    are returned to their base or origin, if possible."""
    pass

class AircraftMaintenancePhase(Phase):
    """§48.0 VIII-B, p20.
    Both players may attempt to ready planes that have flown missions during the Strategic Air Stage."""
    pass


class EndOfTurnStage(Stage):
    """§48.0 IX, p20."""
    def __init__(self, turn: "GameTurn"):
        super().__init__(turn)

    def log(self, message: str):
        self.turn.log(f"[{self.__class__.__name__}] {message}")

    def play(self):
        self.log("stage start")
        self.log("stage complete")
