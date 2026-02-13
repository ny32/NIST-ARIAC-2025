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
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE