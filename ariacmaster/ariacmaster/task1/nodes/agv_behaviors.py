import py_trees
import time
from world.context import WORLD


class FindNearestFreeAGVSlot(py_trees.behaviour.Behaviour):
    def __init__(self, name="Locate Nearest Cell"):
        super().__init__(name)
    
    def update(self):
        self.feedback_message = f"Found available slot on AGV {WORLD.filledAGV}."
        return py_trees.common.Status.SUCCESS

class LocateFilledInspectionAGVs(py_trees.behaviour.Behaviour):
    def __init__(self, name="Check if Inspection AGVs have filled slots"):
        super().__init__(name)
    def update(self):
        for x in range(0, 3):
            if WORLD.AGVs[x][0] == 4:
                self.feedback_message = f"AGV {x+1} has all slots filled."
                WORLD.filledAGV = x + 1
                return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class MoveAGVsToIntersection(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move filled AGVs to intersection"):
        super().__init__(name)
    def update(self):
        if WORLD.filledAGV != -1:
            self.feedback_message = f"Moving AGV {WORLD.filledAGV} to Intersection"
            time.sleep(2) # Simulate movement time
            self.feedback_message = f"AGV {WORLD.filledAGV} reached Intersection"
            WORLD.AGVAtIntersection = WORLD.filledAGV
            WORLD.filledAGV = -1 # Reset
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class Wait1Sec(py_trees.behaviour.Behaviour):
    def __init__(self, name="Wait 1 Second"):
        super().__init__(name)
    def update(self):
        self.feedback_message = "Waiting 1 second"
        time.sleep(1)
        self.feedback_message = "Done!"
        return py_trees.common.Status.SUCCESS
    
class MoveAGVToAssembly(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move AGV to Assembly Station"):
        super().__init__(name)
    def update(self):
        if WORLD.AGVAtIntersection != -1:
            self.feedback_message = f"Moving AGV {WORLD.AGVAtIntersection} to Assembly Station"
            time.sleep(2) # Simulate movement time
            self.feedback_message = f"AGV {WORLD.AGVAtIntersection} reached Assembly Station"
            x = WORLD.AGVAtIntersection - 1
            WORLD.AGVs[x][1] = "Assembly"
            WORLD.AGVAtIntersection = -1 # Reset
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE
class MoveAssemblyAGVToInspection(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move Assembly AGV to Inspection Station"):
        super().__init__(name)
    def update(self):
        for x in range(0, 3):
            if WORLD.AGVs[x][1] == "Assembly" and WORLD.AGVs[x][0] == 0:
                self.feedback_message = f"Moving AGV {x+1} back to Inspection Station"
                time.sleep(2) # Simulate movement time
                WORLD.AGVs[x][1] = "Inspection"
                self.feedback_message = f"AGV {x+1} reached Inspection Station"
                return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class UnloadAssemblyAGV(py_trees.behaviour.Behaviour):
    def __init__(self, name="Unload AGV at Assembly Station"):
        super().__init__(name)
    def update(self):
        unloaded = False
        for x in range(0, 3):
            if WORLD.AGVs[x][1] == "Assembly":
                self.feedback_message = f"Unloading AGV {x+1} at Assembly Station"
                time.sleep(2)
                WORLD.AGVs[x][0] = 0 # Clear AGV slots
                self.feedback_message = f"AGV {x+1} unloaded and ready for new cells"
                WORLD.cellsKitted += 4
                unloaded = True
        if unloaded:
            return py_trees.common.Status.SUCCESS
        else:
            self.feedback_message = "No AGV at Assembly to unload"
            return py_trees.common.Status.FAILURE