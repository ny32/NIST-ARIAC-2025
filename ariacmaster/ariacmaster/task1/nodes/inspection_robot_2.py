import py_trees
import time
from world.context import WORLD

class Wait1Sec(py_trees.behaviour.Behaviour):
    def __init__(self, name="Wait 1 Second"):
        super().__init__(name)
    def update(self):
        time.sleep(1)
        self.feedback_message = "Done!"
        return py_trees.common.Status.SUCCESS
    
class setTargetCellTo1(py_trees.behaviour.Behaviour):
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
    
class setTargetCellTo2(py_trees.behaviour.Behaviour):
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
    
class MoveToCurrentCell(py_trees.behaviour.Behaviour):
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
            time.sleep(2)  # Simulate movement time
            WORLD.IR2Location = "Tester 1"
            self.feedback_message = "IR2 reached Tester 1"
        elif WORLD.IR2TargetCell == "Cell 2":
            time.sleep(2)  # Simulate movement time
            WORLD.IR2Location = "Tester 2"
            self.feedback_message = "IR2 reached Tester 2"
        WORLD.IR2Free = True
        return py_trees.common.Status.SUCCESS

class GraspCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR2 Grasp Cell"):
        super().__init__(name)

    def update(self):
        if WORLD.IR2Free and (WORLD.IR2Location == "Tester 1" or WORLD.IR2Location == "Tester 2"):
            WORLD.IR2Free = False
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



class MoveToAGVSlot(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move IR2 to free AGV Slot"):
        super().__init__(name)
    def update(self):
        if not WORLD.IR2Grasping or WORLD.IR2Location not in ("Tester 1", "Tester 2"):
            return py_trees.common.Status.FAILURE
        time.sleep(2)  # Simulate movement time
        for x in range(0, 3):
            if WORLD.AGVs[x][1] == "Inspection" and WORLD.AGVs[x][0] < 4:
                WORLD.IR2Location = f"AGV {x+1}"
                self.feedback_message = f"IR2 reached AGV {x+1}"
                return py_trees.common.Status.SUCCESS
        self.feedback_message = "No AGV slot available at Inspection Station"
        return py_trees.common.Status.FAILURE

class PlaceInSlot(py_trees.behaviour.Behaviour):
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

class MoveToRecycling(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR2 moving to recycling"):
        super().__init__(name)
    def update(self):
        if WORLD.IR2Grasping and WORLD.IR2Location != "Recycling Bin":
            time.sleep(2) # Simulate movement time
            WORLD.IR2Location = "Recycling Bin"
            self.feedback_message = "IR2 reached the recycling bin"
            WORLD.cellsDisposed += 1
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class ReleaseCell(py_trees.behaviour.Behaviour):
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