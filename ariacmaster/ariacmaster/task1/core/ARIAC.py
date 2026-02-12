from core.types import Defects

class Report:
    def __init__(self, DefectType):
        self.Status: bool = (True if DefectType == "None" else False)
        self.DefectType: Defects = DefectType