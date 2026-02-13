import py_trees
import time
from world.context import WORLD

class MoveToPickup(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR1MoveToPickup"):
        super().__init__(name)

    def update(self):
        if WORLD.IR1Location != "Conveyor":
            time.sleep(2)  # Simulate movement time
            WORLD.IR1Location = "Conveyor"
            self.feedback_message = "IR1 reached Conveyor"
        return py_trees.common.Status.SUCCESS
    
class GraspCell(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR1GraspCell"):
        super().__init__(name)

    def update(self):
        if WORLD.IR1Location == "Conveyor":
            if WORLD.cellsQueued > 0:
                WORLD.cellsQueued -= 1
                time.sleep(0.5)  # Simulate grasping time
                WORLD.IR1Grasping = True
                self.feedback_message = "IR1 grasped cell"
                return py_trees.common.Status.SUCCESS
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.FAILURE

class MoveToTester1(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move IR1 to Tester 1"):
        super().__init__(name)
    def update(self):
        if not WORLD.IR1Grasping:
            return py_trees.common.Status.FAILURE
        if WORLD.IR1Location == "Tester 1":
            self.feedback_message = "IR1 already at Tester 1"
            return py_trees.common.Status.SUCCESS
        time.sleep(2)  # Simulate movement time
        WORLD.IR1Location = "Tester 1"
        self.feedback_message = "IR1 reached Tester 1"
        return py_trees.common.Status.SUCCESS

class MoveToTester2(py_trees.behaviour.Behaviour):
    def __init__(self, name="Move IR1 to Tester 2"):
        super().__init__(name)
    def update(self):
        if not WORLD.IR1Grasping:
            return py_trees.common.Status.FAILURE
        if WORLD.IR1Location == "Tester 2":
            self.feedback_message = "IR1 already at Tester 2"
            return py_trees.common.Status.SUCCESS
        time.sleep(2)  # Simulate movement time
        WORLD.IR1Location = "Tester 2"
        self.feedback_message = "IR1 reached Tester 2"
        return py_trees.common.Status.SUCCESS

class PlaceInTester(py_trees.behaviour.Behaviour):
    def __init__(self, name="IR1PlaceInTester"):
        super().__init__(name)

    def update(self):
        if WORLD.IR1Grasping and (WORLD.IR1Location == "Tester 1" or WORLD.IR1Location == "Tester 2"):
            time.sleep(0.5)  # Simulate placing time
            WORLD.IR1Grasping = False
            # Mark the other tester as free (this one is now occupied)
            if WORLD.IR1Location == "Tester 1":
                WORLD.FreeTesters = "Tester 2"
            else:
                WORLD.FreeTesters = "Tester 1"
            self.feedback_message = f"IR1 placed cell in {WORLD.IR1Location}"
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

class Wait1Sec(py_trees.behaviour.Behaviour):
    def __init__(self, name="Wait 1 Second"):
        super().__init__(name)
    def update(self):
        time.sleep(1)
        self.feedback_message = "Done!"
        return py_trees.common.Status.SUCCESS