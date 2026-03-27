import py_trees
from world.context import WORLD
from core.constants import COMPETITION_DURATION, NORMAL_CELL_VOLTAGE, ALLOWED_VOLTAGE_TOLERANCE
from datetime import datetime, timedelta

class DefectFound(py_trees.behaviour.Behaviour):
    # Checks if a defect was found in the report
    def __init__(self, name="Defect Found"):
        super().__init__(name)
    def update(self):
        if WORLD.Report.DefectType != "None":
            self.feedback_message = f"Defect Found: {WORLD.Report.DefectType}"
            WORLD.cellsDisposed += 1
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "No Defect Found"
            return py_trees.common.Status.FAILURE

class QueuedCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="Queued Cell"):
        super().__init__(name)
    def update(self):
        if WORLD.cellsQueued > 0:
            self.feedback_message = f"Cells Queued: {WORLD.cellsQueued}"
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "No Cells Queued"
            return py_trees.common.Status.FAILURE

class VoltageTester1Free(py_trees.behaviour.Behaviour):
    #Checks if Voltage Tester 1 is free
    def __init__(self, name="Check to see if Voltage tester 1 is Free"):
        super().__init__(name)
    def update(self):
        if WORLD.FreeTesters == "Both" or WORLD.FreeTesters == "Tester 1":
            self.feedback_message = "Voltage Tester 1 is Free"
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "Voltage Tester 1 is Busy"
            return py_trees.common.Status.FAILURE
        
class VoltageTester2Free(py_trees.behaviour.Behaviour):
    #Checks if Voltage Tester 1 is free
    def __init__(self, name="Check to see if Voltage tester 2 is Free"):
        super().__init__(name)
    def update(self):
        if WORLD.FreeTesters == "Both" or WORLD.FreeTesters == "Tester 2":
            self.feedback_message = "Voltage Tester 2 is Free"
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "Voltage Tester 2 is Busy"
            return py_trees.common.Status.FAILURE
class CurrentCellTolerable(py_trees.behaviour.Behaviour):
    # Check if the Voltage reading of the current cell is within NIST ARIAC tolerances
    def __init__(self, name="Check cell voltage acceptability"):
        super().__init__(name)
    def update(self):
        if round(abs(WORLD.voltageReading - NORMAL_CELL_VOLTAGE), 1) <= ALLOWED_VOLTAGE_TOLERANCE:
            self.feedback_message = f"Cell voltage {WORLD.voltageReading}V is within acceptable range."
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = f"Cell voltage {WORLD.voltageReading}V is out of acceptable range."
            return py_trees.common.Status.FAILURE
        
class AGVAtAssembly(py_trees.behaviour.Behaviour):
    # Check if any AGV is at the Assembly Station
    def __init__(self, name="Check if any AGV is at Assembly Station"):
        super().__init__(name)
    def update(self):
        if (WORLD.AGVs[0][1] == "Assembly" or
            WORLD.AGVs[1][1] == "Assembly" or
            WORLD.AGVs[2][1] == "Assembly"):
            self.feedback_message = "An AGV is at the Assembly Station."
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "No AGV is at the Assembly Station."
            return py_trees.common.Status.FAILURE

class AssemblyAGVSlotsEmpty(py_trees.behaviour.Behaviour):
    # Check if any AGV at the Assembly Station has empty slots
    def __init__(self, name="Check for empty slots in AGVs at Assembly Station"):
        super().__init__(name)
    def update(self):
        for x in range(0,3):
            if WORLD.AGVs[x][1] == "Assembly":
                if WORLD.AGVs[x][0] != 0:
                    self.feedback_message = f"AGV {x+1} at Assembly is not empty."
                    return py_trees.common.Status.FAILURE
                self.feedback_message = f"AGV {x+1} at Assembly has all slots empty."
                return py_trees.common.Status.SUCCESS
        # No AGV found at the Assembly station
        self.feedback_message = "No AGV is currently at the Assembly Station."
        return py_trees.common.Status.FAILURE
            
class CompetitionEnded(py_trees.behaviour.Behaviour):
    # Check if the competition has ended (for example, after a certain time limit)
    def __init__(self, name="Check if Competition Ended"):
        super().__init__(name)
    def update(self):
        if datetime.now() - WORLD.startTime >= timedelta(minutes=COMPETITION_DURATION):
            self.feedback_message = "Competition has ended."
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class FreePositiveCells(py_trees.behaviour.Behaviour):
    # Check if there are free slots for positive cells in the shell
    def __init__(self, name="Check for free positive cell slots in shell"):
        super().__init__(name)
    def update(self):
        if WORLD.shellSlots[0] > 0:
            self.feedback_message = f"Free positive cell slots available: {WORLD.shellSlots[0]}"
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "No free positive cell slots available."
            return py_trees.common.Status.FAILURE