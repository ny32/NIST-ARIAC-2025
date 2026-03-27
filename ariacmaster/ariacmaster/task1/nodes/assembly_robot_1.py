import py_trees
import time

from py_trees.common import Status
from world.context import WORLD

class MoveToVG4(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move to VG4 Attachment"):
        super().__init__(name)
    def update(self):
        time.sleep(2) #simulate time to move
        WORLD.AR1Location = "Tool Change"
        self.feedback_message = f"Arrived at {WORLD.AR1Location}"
        return py_trees.common.Status.SUCCESS

class AttachVG4(py_trees.behaviour.Behaviour):
    def __init__(self, name="Attach VG4 tool"):
        super().__init__(name)
    def update(self):
        time.sleep(1) #Time to attach tool
        WORLD.AR1Attachment = "VG4"
        self.feedback_message = f"Successfully attached {WORLD.AR1Attachment} to AR1"
        return py_trees.common.Status.SUCCESS

class MoveToAGV(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move AR1 to AGV"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to move to assembly
        WORLD.AR1Location = "AGV"
        self.feedback_message = f"AR1 successfully moved to {WORLD.AR1Location}"
        return py_trees.common.Status.SUCCESS

class GrabAssemblyCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="Grab Cell from AGV"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to grab assembly
        self.feedback_message = "AR1 successfully grabbed cell"
        return py_trees.common.Status.SUCCESS

class PlaceIntoAGVCenter(py_trees.behaviour.Behaviour):
    def __init__(self, name="Place Cell into center of AGV"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to place assembly
        self.feedback_message = "AR1 successfully placed cell into center of AGV"
        return py_trees.common.Status.SUCCESS

class ReGraspAssemblyCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="Regrasp Cell to place into center of AGV"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to regrasp assembly
        self.feedback_message = "AR1 successfully regrasped cell"
        return py_trees.common.Status.SUCCESS

class PlaceInPositiveCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="Place into positive cell slot"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to place into positive cell slot
        WORLD.shellSlots[0] -= 1
        self.feedback_message = "AR1 successfully placed cell into positive cell slot"
        return py_trees.common.Status.SUCCESS

class FlipGrabberOrientation(py_trees.behaviour.Behaviour):
    def __init__(self, name="Flip Grabber Orientation"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to flip grabber orientation
        self.feedback_message = "AR1 successfully flipped grabber orientation"
        return py_trees.common.Status.SUCCESS

class PlaceInNegativeCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="Place into negative cell slot"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to place into negative cell slot
        WORLD.shellSlots[1] -= 1
        self.feedback_message = "AR1 successfully placed cell into negative cell slot"
        return py_trees.common.Status.SUCCESS

class MoveToVG2(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move to VG2 Attachment"):
        super().__init__(name)
    def update(self):
        time.sleep(2) #simulate time to move
        WORLD.AR1Location = "Tool Change"
        self.feedback_message = f"Arrived at {WORLD.AR1Location}"
        return py_trees.common.Status.SUCCESS
    
class AttachVG2(py_trees.behaviour.Behaviour):
    def __init__(self, name="Attach VG2 tool"):
        super().__init__(name)
    def update(self):
        time.sleep(1) #Time to attach tool
        WORLD.AR1Attachment = "VG2"
        self.feedback_message = f"Successfully attached {WORLD.AR1Attachment} to AR1"
        return py_trees.common.Status.SUCCESS

class MoveToDisturbance(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move to area of Sensor disturbances"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to move to sensor trigger
        WORLD.AR1Location = "Sensor Trigger"
        self.feedback_message = f"AR1 successfully moved to {WORLD.AR1Location}"
        return py_trees.common.Status.SUCCESS

class GrabShell(py_trees.behaviour.Behaviour):
    def __init__(self, name="Grab Shell"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to grab shell
        self.feedback_message = "AR1 successfully grabbed shell."
        return py_trees.common.Status.SUCCESS

class MoveToModule(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move to Module"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to move to module
        WORLD.AR1Location = "Assembly"
        self.feedback_message = f"AR1 successfully moved to {WORLD.AR1Location}"
        return py_trees.common.Status.SUCCESS

class PlaceShellOnModule(py_trees.behaviour.Behaviour):
    def __init__(self, name="Place Shell on Module"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to place shell on module
        self.feedback_message = "AR1 successfully placed shell on module."
        return py_trees.common.Status.SUCCESS

class MoveToWeldingModule(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move to Welding Module"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to move to module
        WORLD.AR1Location = "Gantry"
        self.feedback_message = f"AR1 successfully moved to {WORLD.AR1Location} (incomplete module)"
        return py_trees.common.Status.SUCCESS

class GraspModule(py_trees.behaviour.Behaviour):
    def __init__(self, name="Grasp Module"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to grasp module
        self.feedback_message = "AR1 successfully grasped incomplete module."
        return py_trees.common.Status.SUCCESS

class PlaceModuleOnConveyor(py_trees.behaviour.Behaviour):
    def __init__(self, name="Place Module on Conveyor"):
        super().__init__(name)
    def update(self):
        time.sleep(1) # Time to place module on conveyor
        WORLD.AR1Location = "Assembly"
        self.feedback_message = f"AR1 successfully placed incomplete module on conveyor at {WORLD.AR1Location}"
        return py_trees.common.Status.SUCCESS