import random
import py_trees
import time
from core.constants import STARTUP_TIME
from world.context import WORLD

class StartCompetition(py_trees.behaviour.Behaviour):
    # Starts the competition
    def __init__(self, name="Start Competition"):
        super().__init__(name)
    def update(self):
        time.sleep(STARTUP_TIME) # Simulate delay for competition start
        self.feedback_message = "Competition started"
        return py_trees.common.Status.SUCCESS
    
class EndCompetition(py_trees.behaviour.Behaviour):
    # Ends the competition
    def __init__(self, name="End Competition"):
        super().__init__(name)
    def update(self):
        time.sleep(3) # Simulate delay for competition end
        self.feedback_message = "Competition ended"
        return py_trees.common.Status.SUCCESS

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
            self.feedback_message = f"Voltage reading {WORLD.voltageReading}V taken from {WORLD.IR2TargetCell}"

            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE
    
class SpawnNewShell(py_trees.behaviour.Behaviour):
    def __init__(self,  name="Spawn New Shell"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time delay for shell spawn
        self.feedback_message = "Spawned a new module shell"
        WORLD.shellSlots = [2, 2] # Reset shell slots to full
        return py_trees.common.Status.SUCCESS

class SpawnTopShell(py_trees.behaviour.Behaviour):
    def __init__(self, name="Spawn Top Shell"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time delay for shell spawn
        self.feedback_message = "Spawned a new top shell"
        # Randomly spawns in world, but won't impact read-only code
        return py_trees.common.Status.SUCCESS

class CallForSensorDisturbances(py_trees.behaviour.Behaviour):
    def __init__(self, name="Call for Sensor Disturbances"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time delay for calling disturbances
        self.feedback_message = "Called for sensor disturbances"
        return py_trees.common.Status.SUCCESS

class MoveModuleToGantry(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move Module to Gantry"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time delay for moving module to gantry
        self.feedback_message = "Module moved to gantry"
        return py_trees.common.Status.SUCCESS
    
class CallWeldService(py_trees.behaviour.Behaviour):
    def __init__(self, name="Call Gantry Weld Service"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time delay for calling weld service
        self.feedback_message = "Called gantry weld service"
        return py_trees.common.Status.SUCCESS

class SUBMIT_MODULE(py_trees.behaviour.Behaviour):
    def __init__(self, name="Submit Module"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time delay for submitting module
        WORLD.SUBMITTED_MODULES += 1
        self.feedback_message = f"Submitted module #{WORLD.SUBMITTED_MODULES}"
        return py_trees.common.Status.SUCCESS