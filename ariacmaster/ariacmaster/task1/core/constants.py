NORMAL_CELL_VOLTAGE = 12.7 # Normal Voltage for a real cell
ALLOWED_VOLTAGE_TOLERANCE = 7 # NIST ARIAC - Allowed voltage tolerance for a cell

INSPECTION_DEFECT_PROBABILITY = 1000 # Integers 1, 2, 3 represent defects, so values 3 or under will guaruntee defects
# ex. if 10, 3/10 probability of defects 

NORMAL_RETRIES=1000
STARTUP_TIME = 0.1 # Time in seconds to simulate competition start
COMPETITION_DURATION = 5 # Competition duration in minutes