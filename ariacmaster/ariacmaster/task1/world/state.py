from datetime import datetime
from core.ARIAC import Report
from core.types import *
class WorldState:
    def __init__(self):
        self.tick_count=0 # Counts ticks, not needed for ARIAC

        self.Report: Report = Report(DefectType="None")
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

        self.AR1Location: ARLocations = "Assembly"
        self.AR1Attachment: ARAttachments = "VG2"

        self.shellSlots = [2, # Positive 
                           2 # Negative
        ]

        self.AGVs: list[list] = [
            [3, # Gives a bit of a quick start to demo 
             "Inspection"], # AGV 1
            [0, "Inspection"], #AGV 2
            [0, "Inspection"] # AGV 3
        ]

        self.SUBMITTED_MODULES: int = 0
        self.startTime: datetime = datetime.now()
        
    def __str__(self):
        return (
            f"AGV 1 (Location | Slots Filled): {self.AGVs[0][1]} | {self.AGVs[0][0]}\n"
            f"AGV 2 (Location | Slots Filled): {self.AGVs[1][1]} | {self.AGVs[1][0]}\n"
            f"AGV 3 (Location | Slots Filled): {self.AGVs[2][1]} | {self.AGVs[2][0]}\n"
            f"Inspection Robot 1 Location: {self.IR1Location}\n"
            f"Inspection Robot 2 Location: {self.IR2Location}\n"
            f"Cells Queued for Inspection: {self.cellsQueued}\n"
            f"Assembly Robot 1 Location: {self.AR1Location}\n"
            f"Assembly Robot 1 Attachment: {self.AR1Attachment}\n"
            f"-------------------------------------------\n"
            f"Cells Disposed: {self.cellsDisposed}\n"
            f"Cells Kitted: {self.cellsKitted}\n"
            f"Positive Module Shell Slots Filled: {2 - self.shellSlots[0]}\n"
            f"Negative Module Shell Slots Filled: {2 - self.shellSlots[1]}\n"
            f"-------------------------------------------\n"
            # f"Cells Submitted: {self.SUBMITTED_MODULES}\n"
        )



# Prevents imports from running this check
if __name__ == "__main__":
    _world = WorldState()
    print("World State Initialized:")
    print(_world)
