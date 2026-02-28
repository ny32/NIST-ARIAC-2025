Guide
=========

Run Instructions
-----------------
1. Update pip

.. code-block:: bash
    
    python -m pip install --upgrade pip

2. Install project dependencies

.. code-block:: bash
    
    pip install -r requirements.txt

3. Run main file

.. code-block:: bash
    
    python ariacmaster/ariacmaster/task1/main.py

Competiton Parameters
-------------------
*core/constants.py*

``NORMAL_CELL_VOLTAGE (float):`` 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    
    Ideal cell voltage standard.

``ALLOWED_VOLTAGE_TOLERANCE (float)``:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Allowed voltage tolerance for cells to pass.

``INSPECTION_DEFECT_PROBABILITY (int)``:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Represents max integer bound of randomly generated number to determine if a cell is defective. Values [1, 2 3] represent defective cells. Values ≤ 3 will only spawn defective cells.

``NORMAL_RETRIES (int)``:
^^^^^^^^^^^^^^^^^^^^^^^^^^
Number of retry ticks of tree before failing. Recommended not to change default.

``STARTUP_TIME (float)``:
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Time in seconds to simulate competition start.

``COMPETITION_DURATION (float)``:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Competition duration in minutes.

World State
----------------------

*world/state.py*

``self.tick_count`` (int):
    Counts ticks, incremented by 1 every tick.

``self.Report`` (Report):
    Instance of the ``Report`` class. Initialized with ``DefectType="None"``.

``self.IR1Grasping`` (bool):
    True if Inspection Robot 1 is currently grasping a part; False otherwise.

``self.IR1Location`` (IRLocations):
    Current location of Inspection Robot 1. Initialized to ``"Conveyor"``.

``self.IR2Free`` (bool):
    True if Inspection Robot 2 is free and available to grasp a part.

``self.IR2Grasping`` (bool):
    True if Inspection Robot 2 is currently grasping a part; False otherwise.

``self.IR2Location`` (IRLocations):
    Current location of Inspection Robot 2. Initialized to ``"Conveyor"``.

``self.IR2TargetCell`` (Cells):
    Target cell assigned for Inspection Robot 2. Initialized to ``"None"``.

``self.FreeTesters`` (Testers):
    Indicates which testers are free. Initialized to ``"Both"``.

``self.cellsDisposed`` (int):
    Number of cells disposed so far.

``self.cellsKitted`` (int):
    Number of cells successfully kitted.

``self.cellsQueued`` (int):
    Number of cells currently queued for processing.

``self.voltageReading`` (float):
    Current voltage reading of the cell under inspection.

``self.filledAGV`` (int):
    ID of the AGV that is currently filled. Initialized to ``-1``.

``self.AGVAtIntersection`` (int):
    ID of the AGV currently at the intersection. Initialized to ``-1``.

``self.AGVs`` (list[list]):
    List of AGVs and their states. Each AGV is represented as a list:  
    - First element: number of filled slots  
    - Second element: position of AGV (`"Inspection"` or `"Assembly"`)  

    Default initialization:
    
    .. code-block:: python

       [
           [3, "Inspection"],  # AGV 1 (preloaded for demo)
           [0, "Inspection"],  # AGV 2
           [0, "Inspection"]   # AGV 3
       ]

``self.startTime`` (datetime):
    Timestamp of when the WorldState object was initialized. Initialized to ``datetime.now()``.