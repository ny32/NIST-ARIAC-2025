import py_trees
import time
import random
from core.constants import INSPECTION_DEFECT_PROBABILITY
from world.context import WORLD
from core.ARIAC import Report
class ConstructLIDARModel(py_trees.behaviour.Behaviour):
    # Scans the cell using LIDAR and constructs a 3D model
    def __init__(self, name="Construct LIDAR Model"):
        super().__init__(name)

    def update(self):
        time.sleep(1) # Time delay for cell arrival
        time.sleep(0.5)
        self.feedback_message = "LIDAR Model Constructed"
        return py_trees.common.Status.SUCCESS

class PopulateReport(py_trees.behaviour.Behaviour):
    # Populates inspection report based on LIDAR model
    def __init__(self, name="Populate Report"):
        super().__init__(name)
    
    def update(self):
        # Simulate randomness in defect detection
        randomValue = random.randint(1, INSPECTION_DEFECT_PROBABILITY)
        defect = ("Dent" if randomValue == 1 
                        else "Scratch" if randomValue == 2
                        else "Bulge" if randomValue == 3 
                        else "None")
        WORLD.Report = Report(DefectType=defect)
        if defect != "None":
            self.feedback_message = f"Defect Detected: {defect}"
        return py_trees.common.Status.SUCCESS
    
class SubmitReport(py_trees.behaviour.Behaviour):
    # Submits inspection report
    def __init__(self, name="Submit Report"):
        super().__init__(name)
    def update(self):
        self.feedback_message = "Report Submitted."
        return py_trees.common.Status.SUCCESS

class OpenInspectionDoor(py_trees.behaviour.Behaviour):
    # Opens the inspection door
    def __init__(self, name="Open Inspection Door"):
        super().__init__(name)
    def update(self):
        time.sleep(2)  # Simulate time taken to open door and for cell to move past
        self.feedback_message = "Cell  moved to queue. Door closing..."
        WORLD.cellsQueued += 1
        return py_trees.common.Status.SUCCESS