import py_trees
import time
import random
from world.context import WORLD

class IR1MoveToPickup(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR1MoveToPickup"):
        super().__init__(name)

    def update(self):
        if WORLD.IR1Location != "Conveyor":
            WORLD.IR1Free = False
            self.feedback_message = "IR1 moving to Conveyor"
            time.sleep(2)  # Simulate movement time
            WORLD.IR1Location = "Conveyor"
            WORLD.IR1Free = True
            self.feedback_message = "IR1 reached Conveyor"
        return py_trees.common.Status.SUCCESS
    
class IR1GraspCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR1GraspCell"):
        super().__init__(name)

    def update(self):
        if WORLD.IR1Free and WORLD.IR1Location == "Conveyor":
            WORLD.IR1Free = False
            if WORLD.cellsQueued > 0:
                WORLD.cellsQueued -= 1
                self.feedback_message = "IR1 grasping cell"
                time.sleep(0.5)  # Simulate grasping time
                WORLD.IR1Grasping = True
                self.feedback_message = "IR1 grasped cell"
                return py_trees.common.Status.SUCCESS
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.FAILURE

class IR1MoveToTester1(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move IR1 to Tester 1"):
        super().__init__(name)
    def update(self):
        if not WORLD.IR1Grasping:
            return py_trees.common.Status.FAILURE
        if WORLD.IR1Location == "Tester 1":
            self.feedback_message = "IR1 already at Tester 1"
            return py_trees.common.Status.SUCCESS
        self.feedback_message = "IR1 moving to Tester 1"
        time.sleep(2)  # Simulate movement time
        WORLD.IR1Location = "Tester 1"
        self.feedback_message = "IR1 reached Tester 1"
        return py_trees.common.Status.SUCCESS

class IR1MoveToTester2(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move IR1 to Tester 2"):
        super().__init__(name)
    def update(self):
        if not WORLD.IR1Grasping:
            return py_trees.common.Status.FAILURE
        if WORLD.IR1Location == "Tester 2":
            self.feedback_message = "IR1 already at Tester 2"
            return py_trees.common.Status.SUCCESS
        self.feedback_message = "IR1 moving to Tester 2"
        time.sleep(2)  # Simulate movement time
        WORLD.IR1Location = "Tester 2"
        self.feedback_message = "IR1 reached Tester 2"
        return py_trees.common.Status.SUCCESS

class IR1PlaceInTester(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR1PlaceInTester"):
        super().__init__(name)

    def update(self):
        if WORLD.IR1Grasping and (WORLD.IR1Location == "Tester 1" or WORLD.IR1Location == "Tester 2"):
            self.feedback_message = f"IR1 placing cell in {WORLD.IR1Location}"
            time.sleep(0.5)  # Simulate placing time
            WORLD.IR1Grasping = False
            WORLD.IR1Free = True
            # Mark the other tester as free (this one is now occupied)
            if WORLD.IR1Location == "Tester 1":
                WORLD.FreeTesters = "Tester 2"
            else:
                WORLD.FreeTesters = "Tester 1"
            self.feedback_message = f"IR1 placed cell in {WORLD.IR1Location}"
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class setIR2TargetCellTo1(py_trees.behaviour.Behaviour):
    def __init__(self, name="Set IR2 Target Cell to Cell 1"):
        super().__init__(name)

    def update(self):
        if WORLD.IR2TargetCell == "None":
            WORLD.IR2TargetCell = "Cell 1"
            self.feedback_message = "Set IR2 to target Cell 1"
            return py_trees.common.Status.SUCCESS
        elif WORLD.IR2TargetCell == "Cell 1":
            self.feedback_message = "IR2 target already set to Cell 1"
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE
    
class setIR2TargetCellTo2(py_trees.behaviour.Behaviour):
    def __init__(self, name="Set IR2 Target Cell to Cell 2"):
        super().__init__(name)

    def update(self):
        if WORLD.IR2TargetCell == "None":
            WORLD.IR2TargetCell = "Cell 2"
            self.feedback_message = "Set IR2 to target Cell 2"
            return py_trees.common.Status.SUCCESS
        elif WORLD.IR2TargetCell == "Cell 2":
            self.feedback_message = "IR2 target already set to Cell 2"
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class TakeCurrentCellVoltage(py_trees.behaviour.Behaviour):
    # Takes Voltage reading of the cell in the tester
    def __init__ (self, name="Take Voltage Reading"):
        super().__init__(name)
    def update(self):
        if WORLD.IR2TargetCell != "None":
            time.sleep(1) # Time delay for taking voltage reading
            self.feedback_message = f"Voltage reading taken for {WORLD.IR2TargetCell}"
            WORLD.voltageReading = ( random.randint(124, 129) ) / 10 
            """
            Possible Values: 12.4, 12.5, 12.6, 12.7, 12.8, 12.9
            Not Allowed: 12.4V (16.7% probability of occurence)
            """
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE
    
class IR2MoveToCurrentCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move IR2 to Current Cell"):
        super().__init__(name)
    def update(self):
        if not WORLD.IR2Free:
            return py_trees.common.Status.FAILURE
        if WORLD.IR2TargetCell != "Cell 1" and WORLD.IR2TargetCell != "Cell 2":
            self.feedback_message = "IR2 target cell not set"
            return py_trees.common.Status.FAILURE
        WORLD.IR2Free = False
        if WORLD.IR2TargetCell == "Cell 1":
            self.feedback_message = "IR2 moving to Tester 1"
            time.sleep(2)  # Simulate movement time
            WORLD.IR2Location = "Tester 1"
            self.feedback_message = "IR2 reached Tester 1"
        elif WORLD.IR2TargetCell == "Cell 2":
            self.feedback_message = "IR2 moving to Tester 2"
            time.sleep(2)  # Simulate movement time
            WORLD.IR2Location = "Tester 2"
            self.feedback_message = "IR2 reached Tester 2"
        WORLD.IR2Free = True
        return py_trees.common.Status.SUCCESS

class IR2GraspCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR2 Grasp Cell"):
        super().__init__(name)

    def update(self):
        if WORLD.IR2Free and (WORLD.IR2Location == "Tester 1" or WORLD.IR2Location == "Tester 2"):
            WORLD.IR2Free = False
            self.feedback_message = "IR2 grasping cell"
            time.sleep(0.5)  # Simulate grasping time
            WORLD.IR2Grasping = True
            # Mark this tester as free again
            if WORLD.IR2Location == "Tester 1":
                WORLD.FreeTesters = "Tester 1"
            else:
                WORLD.FreeTesters = "Tester 2"
            self.feedback_message = "IR2 grasped cell"
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE



class IR2MoveToAGVSlot(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move IR2 to free AGV Slot"):
        super().__init__(name)
    def update(self):
        if not WORLD.IR2Grasping or WORLD.IR2Location not in ("Tester 1", "Tester 2"):
            return py_trees.common.Status.FAILURE
        self.feedback_message = "IR2 moving to empty AGV"
        time.sleep(2)  # Simulate movement time
        for x in range(0, 3):
            if WORLD.AGVs[x][1] == "Inspection" and WORLD.AGVs[x][0] < 4:
                WORLD.IR2Location = f"AGV {x+1}"
                self.feedback_message = f"IR2 reached AGV {x+1}"
                return py_trees.common.Status.SUCCESS
        self.feedback_message = "No AGV slot available at Inspection Station"
        return py_trees.common.Status.FAILURE

class IR2PlaceInSlot(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR2 places cell into slot"):
        super().__init__(name)
    def update(self):
        if WORLD.IR2Grasping:
            if WORLD.IR2Location == "AGV 1":
                self.feedback_message = "Placing into AGV 1"
                time.sleep(0.5) # Simulate placing into slot
                WORLD.AGVs[0][0] += 1 # Increment slot count for AGV 1
                WORLD.IR2Grasping = False # Releases Cell
                WORLD.IR2Free = True #IR2 is done with step
                WORLD.IR2TargetCell = "None"  # Reset for next voltage inspection cycle
                return py_trees.common.Status.SUCCESS
            elif WORLD.IR2Location == "AGV 2":
                self.feedback_message = "Placing into AGV 2"
                time.sleep(0.5) # Simulate placing into slot
                WORLD.AGVs[1][0] += 1 # Increment slot count for AGV 2
                WORLD.IR2Grasping = False # Releases Cell
                WORLD.IR2Free = True #IR2 is done with step
                WORLD.IR2TargetCell = "None"  # Reset for next voltage inspection cycle
                return py_trees.common.Status.SUCCESS
            elif WORLD.IR2Location == "AGV 3":
                self.feedback_message = "Placing into AGV 3"
                time.sleep(0.5) # Simulate placing into slot
                WORLD.AGVs[2][0] += 1 # Increment slot count for AGV 3
                WORLD.IR2Grasping = False # Releases Cell
                WORLD.IR2Free = True #IR2 is done with step
                WORLD.IR2TargetCell = "None"  # Reset for next voltage inspection cycle
                return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class IR2MoveToRecycling(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR2 moving to recycling"):
        super().__init__(name)
    def update(self):
        if WORLD.IR2Grasping and WORLD.IR2Location != "Recycling Bin":
            self.feedback_message = "Moving over to recycling"
            time.sleep(2) # Simulate movement time
            WORLD.IR2Location = "Recycling Bin"
            self.feedback_message = "IR2 reached the recycling bin"
            WORLD.cellsDisposed += 1
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class IR2ReleaseCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR2 releases the cell to drop it"):
        super().__init__(name)
    def update(self):
        if WORLD.IR2Grasping:
            self.feedback_message = "IR2 is releasing the cell"
            time.sleep(0.5) # Simulate release time
            WORLD.IR2Grasping = False
            WORLD.IR2Free = True
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE
    
# Added for clarity (already exists in agv behaviors)
class Wait1Sec(py_trees.behaviour.Behaviour):
    def __init__(self, name="Wait 1 Second"):
        super().__init__(name)
    def update(self):
        self.feedback_message = "Waiting 1 second"
        time.sleep(1)
        self.feedback_message = "Done!"
        return py_trees.common.Status.SUCCESS