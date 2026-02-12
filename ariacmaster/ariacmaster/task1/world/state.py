from datetime import datetime
from core.ARIAC import Report
from core.types import DoorStates, IRLocations, Testers, AGVs, AGVLocations, Cells, Slots

class WorldState:
    def __init__(self):
        self.tick_count=0 # Counts ticks, not needed for ARIAC

        self.Report: Report = Report(DefectType="None")
        self.InspectionDoor: DoorStates = "Closed"

        self.IR1Free: bool = True
        self.IR1Grasping: bool = False
        self.IR1Location: IRLocations = "Conveyor"

        self.IR2Free: bool = True
        self.IR2Grasping: bool = False
        # self.IR2Location: IRLocations = "Conveyor"
        self.IR2Location = "Conveyor"
        self.IR2TargetCell: Cells = "None"

        self.FreeTesters: Testers = "Both"
        self.cellsDisposed: int = 0
        self.cellsKitted: int = 0
        self.cellsQueued: int = 0
        self.voltageReading: float = 0.0
        self.filledAGV: int = -1
        self.AGVAtIntersection: int = -1

        self.AGVs: list[list] = [
            [3, "Inspection"], # AGV 1
            [0, "Inspection"], #AGV 2
            [0, "Inspection"] # AGV 3
        ]

        self.startTime: datetime = datetime.now()
        
    def __str__(self):
        return (
            f"AGV 1 Location: {self.AGVs[0][1]}\n"
            f"AGV 2 Location: {self.AGVs[1][1]}\n"
            f"AGV 3 Location: {self.AGVs[2][1]}\n"
            f"Inspection Robot 1 Location: {self.IR1Location}\n"
            f"Inspection Robot 2 Location: {self.IR2Location}\n"
            f"Cells Queued for Inspection: {self.cellsQueued}\n"
            f"-------------------------------------------\n"
            f"Cells Disposed: {self.cellsDisposed}\n"
            f"Cells Kitted: {self.cellsKitted}\n"
        )



# Prevents imports from running this check
if __name__ == "__main__":
    _world = WorldState()
    print("World State Initialized:")
    print(_world)
